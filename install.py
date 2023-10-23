# Curls:
#  Mods.zip
#  Public_Current.json

# Run in directory with:
#  Big_Mods.zip
#  Data.zip

import urllib.request
import os
import zipfile
import sys
import datetime
import shutil

def mods():
    url = "https://drive.google.com/uc?export=download&id=18TEcqs01IAJxqG0z1B4PttfelCk8lPov"
    file_name = "Mods.zip"
    print("Downloading Mods.zip...")
    urllib.request.urlretrieve(url, file_name)
    print("Mods.zip downloaded.")

    destination_directory = os.path.join(os.environ['LOCALAPPDATA'], 'Larian Studios', "Baldur's Gate 3", 'Mods')

    # Clean out old mods
    files = os.listdir(destination_directory)
    for file in files:
        file_path = os.path.join(destination_directory, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall(destination_directory)

    print(f"{file_name} has been extracted to:\n{destination_directory}")
    print()

def order():
    url = "https://drive.google.com/uc?export=download&id=1xdA56-3QssIjSS7ja1pza4WTVzB-ElxY"
    destination = "Public_Current.json"
    print("Downloading Public_Current.json...")
    urllib.request.urlretrieve(url, destination)
    print("Public_Current.json downloaded.")
    print()

def data(a):
    file_name = "Data.zip"
    if os.path.exists(file_name):
        print(f"{file_name} exists in the current working directory. Extracting to BG3/Data...")

        destination_directory = r'C:\Program Files (x86)\Steam\steamapps\common\Baldurs Gate 3\Data'

        # Clean out old mods
        subfolders_to_delete = ['Generated', 'Public', 'Video']
        for subfolder in subfolders_to_delete:
            subfolder_path = os.path.join(destination_directory, subfolder)
            if os.path.exists(subfolder_path):
                shutil.rmtree(subfolder_path)


        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall(destination_directory)

        print(f"{file_name} has been extracted to:\n{destination_directory}")
    else:
        print()
        print(f"{file_name} does not exist in the current working directory.")
        print(f"Place {file_name} in this folder after downloading it from:")
        print("https://drive.google.com/file/d/1CpOePd0otZRvf9-WDtNWf5O0Yqi5GI3D/view")
        input("Press Enter to continue...")
        # Attempt data() 5 times to avoid infinite recursion.
        if(a<5):
            data(a+1)
        else:
            sys.exit()
    print()

def big(a):
    file_name = "Big_Mods.zip"
    if os.path.exists(file_name):
        print(f"{file_name} exists in the current working directory. Extracting to BG3/Mods...")
        print("This may take a while...")

        destination_directory = os.path.join(os.environ['LOCALAPPDATA'], 'Larian Studios', "Baldur's Gate 3", 'Mods')

        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall(destination_directory)

        print(f"{file_name} has been extracted to:\n{destination_directory}")
    else:
        print()
        print(f"{file_name} does not exist in the current working directory.")
        print(f"Place {file_name} in this folder after downloading it from:")
        print("https://drive.google.com/file/d/1-vaDlDfWMtrBuCY9eWxykDsK6yLYYzZX/view?usp=sharing")
        input("Press Enter to continue...")
        # Attempt big() 5 times to avoid infinite recursion.
        if(a<5):
            big(a+1)
        else:
            sys.exit()
    print()

def stamp():
    # Remove previous stamp() files
    files = os.listdir()
    for file in files:
        if file.startswith("UPDATED") and file.endswith(".txt"):
            os.remove(file)

    # Create a txt with date install.exe was run
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    file_name = f"UPDATED_{current_date}.txt"

    with open(file_name, "w") as file:
        pass


def main():
    mods()
    order()

    data(0)
    big(0)
   
    stamp()
    print("Done.")

main()