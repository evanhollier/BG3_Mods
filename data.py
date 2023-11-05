import os
import shutil
import zipfile

source_directory = r'C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data'

directories_to_zip = ['Generated', 'Public']

destination_directory = os.getcwd()

with zipfile.ZipFile(os.path.join(destination_directory, 'Data.zip'), 'w', zipfile.ZIP_DEFLATED) as archive:
    for directory in directories_to_zip:
        dir_path = os.path.join(source_directory, directory)
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                archive.write(file_path, os.path.relpath(file_path, source_directory))

# This will create Data.zip containing Generated, Public from BG3/Data.