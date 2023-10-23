import os
import shutil
import zipfile

# Set the path to the directory containing the files
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
            print(f"Deleted: {filename}")  # Print when a file is deleted
        else:
            file_size = os.path.getsize(file_path)
            if file_size <= 10 * 1024 * 1024:  # Smaller than or equal to 10 MB
                shutil.move(file_path, os.path.join(smaller_files_dir, filename))

# Create a zip archive for smaller files
shutil.make_archive('Mods', 'zip', smaller_files_dir)

# Create a zip archive for larger files, excluding the "small" directory
with zipfile.ZipFile('Big_Mods.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
    for root, dirs, files in os.walk(directory_path):
        if root != smaller_files_dir:
            for file in files:
                file_path = os.path.join(root, file)
                archive.write(file_path, os.path.relpath(file_path, directory_path))

# Move the contents of the "small" directory back to the current working directory
for filename in os.listdir(smaller_files_dir):
    shutil.move(os.path.join(smaller_files_dir, filename), os.path.join(directory_path, filename))

# Remove the temporary "small" directory
shutil.rmtree(smaller_files_dir)

# This will create "Mods.zip" for smaller files and "Big_Mods.zip" for larger files.
