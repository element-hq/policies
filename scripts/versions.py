#!/usr/bin/python
from __future__ import print_function
import os
import sys
import argparse
from subprocess import check_output
from collections import namedtuple

parser = argparse.ArgumentParser(
        description=('Should be run from the root of the git repo. Given a source '
                     'policy document, will spelunk the git commit history to find '
                     'the most recent commit for every version number, and generate '
                     'an instance of the document containing the policy text at that'
                     ' point in time. The version number will be inserted into the '
                     'filename (immediately prior to the file extension). Will '
                     'overwrite any existing files blindly. Will not delete output '
                     'from previous executions.'))
parser.add_argument('filepath',
                    help=('File path to the source policy file from which to generate'
                    ' the versions.'))
parser.add_argument('--destination', default='versions',
                    help='Destination root to output the versioned files')
parser.add_argument('--unversioned', default=None,
                    help=('Version number to use for unversioned commits. Defaults to'
                    'None, which causes no file to be generated for policy commits '
                    'without version information'))
args = parser.parse_args()

Version = namedtuple('Version', ['commit', 'meta', 'text'])

# If an old commit represents a given version of the doc, but we didn't include
# the proper metadata at the time:
SPECIAL_CASES = {
    ('docs/matrix-org/privacy_notice.md', u'e18d9496a02f4da40a823adadfefc54c5dd5f3b9'):
        {'version': '1.0.0',
         'title': 'title: {{ policy_homeserver }} Homeserver Privacy Notice'}
}

def list_commits(filepath):
    command_output = check_output(['git',
                                   'log',
                                   '--reverse',
                                   '--format=%H',
                                   filepath]).decode('utf-8')
    commits = [row for row in command_output.split('\n')
               if row.strip()]
    return commits


def parse(text):
    """Metadata, if present, appears at the top of the markdown file, as key/value
    pairs, sandwiched between two rows of `---`, e.g.:
    ```
    ---
    key1: value1
    key2: lorem ipsum
    ---
    ```
    """

    # Remove any preceeding empty lines:"
    while not text[0].strip():
        text.pop(0)
    index = [i for i, j in enumerate(text) if j == '---']

    if len(index) != 2:
        return ({}, text)

    [metastart, metaend] = index
    if metastart != 0:
        return ({}, text)

    # Ladies and gentlemen - we have a file with meta.
    meta = dict([[x.strip() for x in line.split(':')]
                 for line
                 in text[metastart+1:metaend]])
    return (meta, text[metaend+1:])


def get_version(filepath, commit):
    command_output = check_output(['git',
                                   'show',
                                   '%s:%s' % (commit, filepath)]).decode('utf-8')
    # Either subprocess or git show is adding an extra newline at the end; let's
    # get rid of it.
    text = command_output.split('\n')[0:-1]

    if (filepath, commit) in SPECIAL_CASES:
        return Version(commit=commit,
                meta=SPECIAL_CASES[(filepath, commit)],
                text=text)

    meta, metaless_text = parse(text)
    return Version(commit=commit,
                   meta=meta,
                   text=metaless_text)


def versioned_filename(filepath, version):
    """Turns `path/to/filename.txt` into `filename.version.txt`"""
    filename = os.path.basename(filepath)
    name, extension = filename.rsplit('.')
    return '%s-%s.%s' % (name, version, extension)


def compare_version_strings(a, b):
    a = [int(x) for x in a.split('.')]
    b = [int(x) for x in b.split('.')]

    for i in range(len(max(a,b))):
        a_part = a[i] if len(a) > i else 0
        b_part = b[i] if len(b) > i else 0
        if cmp(a_part, b_part) != 0:
            return cmp(a_part, b_part)
    return 0


def write_file(path, filename, version):
    if not os.path.exists(path):
        os.makedirs(path)
    destination_filepath = '%s/%s' % (path, filename)
    with open(destination_filepath, 'w') as f:
        f.write('---\n')
        for key, value in version.meta.items():
            f.write('%s: %s\n' % (key, value))
        f.write('---\n')
        f.writelines(['%s\n' % line.encode('utf-8') for line in version.text])


versions = {}
for commit in list_commits(args.filepath):
    version = get_version(args.filepath, commit)
    version_number = version.meta.get('version', args.unversioned)
    if version_number is not None:
        versions[version_number] = version

max_major_versions = {}
for version_number in versions.keys():
    major_version = version_number.split('.')[0]
    if compare_version_strings(version_number,
            max_major_versions.get(major_version, '0')) > 0:
        max_major_versions[major_version] = version_number

if len(versions) == 0:
    print('%s: no versions found' % args.filepath, file=sys.stderr)
else:
    print('%s:' % args.filepath, file=sys.stderr)
    for version_number, version in versions.items():
        # Stripping 'docs/' from the start of the path so that the directory structure
        # of the output dir (defaulting to `versions`) can mirror the source `docs`
        # directory.
        path = '%s/%s' % (args.destination, os.path.dirname(args.filepath)[len('docs/'):])
        filenames = [versioned_filename(
            args.filepath,
            version_number
            )]
        if version_number in max_major_versions.values():
            filenames.append(versioned_filename(
                args.filepath,
                version_number.split('.')[0])
            )

        for filename in filenames:
            print('%s v%s -> %s/%s' % (
                version.commit,
                version_number,
                path,
                filename), file=sys.stderr)
            write_file(path, filename, version)

