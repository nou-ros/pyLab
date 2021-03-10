# we can't use zipfile module for z-zip files. We can use shutil for both type of files. Shutil allows to zip and unzip directories

import shutil
# zipping zip files
# shutil.make_archive('another', 'zip', 'files')
# extraction
# shutil.unpack_archive('another.zip', 'another')
# archiving tar file
# shutil.make_archive('another', 'gztar', 'files')

