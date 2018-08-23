import os
import codecs
import argparse

from markdown import markdown

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.settings import LoadSettingsFile

parser = argparse.ArgumentParser()
parser.add_argument('source')
parser.add_argument('destination')
args = parser.parse_args()

file = args.source
destination_folder = args.destination

filename = os.path.basename(file)

WARNING = ['**WARNING: THIS IS A GENERATED FILE.**\nCHANGES ARE NOT AUTOMATICALLY PERSISTED AND MIGHT BE OVERWRITTEN.\nSOURCE: %s\n' % file]

with codecs.open(file, 'r', 'utf-8') as input:
    html = markdown(''.join(WARNING + input.readlines()))

gauth = GoogleAuth()
gauth.settings = LoadSettingsFile('google__credentials.yaml')
gauth.CommandLineAuth()

drive = GoogleDrive(gauth)

# Check to see if the file already exists
#file_list = drive.ListFile({'q': '"%s" in parents and title="%s" and trashed=false'
#                                       % (destination_folder, filename)}).GetList()

# If file is found, update it, otherwise create new file
#if len(file_list) == 1:
#    file_to_write_to = file_list[0]
#else:

# Updating isn't honouring the convert param for some reason, so ditch it for now.
file_to_write_to = drive.CreateFile({'parents': [{'kind': 'drive#fileLink',
                                                  'id': destination_folder}],
                                     'mimeType':'text/html'})

file_to_write_to.SetContentString(html)
file_to_write_to['title'] = filename
file_to_write_to.Upload({'convert': True})
