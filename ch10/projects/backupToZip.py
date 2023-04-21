#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.


import zipfile, os


def backupToZip(folder):
    # back up the entire contents of "folder" into a ZIP file


    folder = os.path.abspath(folder)        # make sure folder is absolute


    # figure out the filename this code should use based on existing files
    number = 1
    while True:
        zipFilename = f'{os.path.basename(folder)}_{str(number)}.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1


    # create the ZIP file
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')


    # TODO: walk the entire folder tree and compress the files in each folder.
    print('Done.')


backupToZip('C:\\delicious')