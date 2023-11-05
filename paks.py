import os
import shutil
import zipfile

directory_path = os.path.join(os.environ['LOCALAPPDATA'], 'Larian Studios', "Baldur's Gate 3", 'Mods')

# Create a temporary directory for smaller files
smaller_files_dir = os.path.join(directory_path, 'small')
os.makedirs(smaller_files_dir, exist_ok=True)

# Iterate through files in the directory
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)

    if os.path.isfile(file_path):
        # Check if it's not a .pak file and delete it
        if not filename.endswith('.pak'):
            os.remove(file_path)
            print(f"Deleted: {filename}")
        else:
            file_size = os.path.getsize(file_path)
            if file_size <= 10 * 1024 * 1024:  # 10 MB
                # Move smaller files to temp directory
                shutil.move(file_path, os.path.join(smaller_files_dir, filename))

# Zip smaller files
shutil.make_archive('Mods', 'zip', smaller_files_dir)

# Zip large files = everything except "small" subfolder
def big():
    with zipfile.ZipFile('Big_Mods.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        for root, dirs, files in os.walk(directory_path):
            if root != smaller_files_dir:
                for file in files:
                    file_path = os.path.join(root, file)
                    archive.write(file_path, os.path.relpath(file_path, directory_path))
# big()

# Move the contents of  "small" back
for filename in os.listdir(smaller_files_dir):
    shutil.move(os.path.join(smaller_files_dir, filename), os.path.join(directory_path, filename))

# Remove "small" subfolder
shutil.rmtree(smaller_files_dir)

# This will create "Mods.zip" for smaller files and "Big_Mods.zip" for larger files.


# Copy Public_Current.json from BG3ModManager
source_json = r"C:\Users\Evan\Desktop\Baldur's Gate 3\BG3ModManager_Latest\Orders\Public_Current.json"
destination_json = os.path.join(os.getcwd(), 'Public_Current.json')
shutil.copy(source_json, destination_json)