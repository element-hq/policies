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

def list_commits(filepath):
    command_output = check_output(['git',
                                   'log',
                                   '--reverse',
                                   '--format=%H',
                                   filepath]).decode('utf-8')
    commits = [row for row in command_output.split('\n')
               if row.strip()]
    return commits


def get_meta(text):
    """Metadata, if present, appears at the top of the markdown file, as key/value
    pairs, sandwiched between two rows of `---`, e.g.:
    ```
    ---
    key1: value1
    key2: lorem ipsum
    ---
    ```
    """

    # We want to ignore empty lines for the purposes of extracting metadata
    text = [line for line in text
            if line.strip()]
    index = [i for i, j in enumerate(text) if j == '---']

    if len(index) != 2:
        return {}

    [metastart, metaend] = index
    if metastart != 0:
        return {}

    # Ladies and gentlemen - we have a file with meta.
    meta = dict([[x.strip() for x in line.split(':')]
                 for line
                 in text[metastart+1:metaend]])
    return meta


def get_version(filepath, commit):
    command_output = check_output(['git',
                                   'show',
                                   '%s:%s' % (commit, filepath)]).decode('utf-8')
    # Either subprocess or git show is adding an extra newline at the end; let's
    # get rid of it.
    text = command_output.split('\n')[0:-1]
    meta = get_meta(text)
    return Version(commit=commit,
                   meta=meta,
                   text=text)


def versioned_filename(filepath, version):
    """Turns `path/to/filename.txt` into `filename.version.txt`"""
    filename = os.path.basename(filepath)
    name, extension = filename.rsplit('.')
    return '%s-%s.%s' % (name, version, extension)


versions = {}
for commit in list_commits(args.filepath):
    version = get_version(args.filepath, commit)
    version_number = version.meta.get('version', args.unversioned)
    if version_number is not None:
        versions[version_number] = version

if len(versions) == 0:
    print('%s: no versions found' % args.filepath, file=sys.stderr)
else:
    print('%s:' % args.filepath, file=sys.stderr)
    for version_number, version in versions.items():
        # Stripping 'docs/' from the start of the path so that the directory structure
        # of the output dir (defaulting to `versions`) can mirror the source `docs`
        # directory.
        path = '%s/%s' % (args.destination, os.path.dirname(args.filepath)[len('docs/'):])
        if not os.path.exists(path):
            os.makedirs(path)
        destination_filepath = '%s/%s' % (
                path,
                versioned_filename(args.filepath, version_number)
                )
        with open(destination_filepath, 'w') as f:
            print('%s v%s -> %s' % (
                version.commit,
                version_number,
                destination_filepath), file=sys.stderr)
            f.writelines(['%s\n' % line for line in version.text])
