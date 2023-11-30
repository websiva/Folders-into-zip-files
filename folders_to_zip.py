import os, subprocess
import zipfile

exe_file_location= os.getcwd()
print(f"Current directory: {exe_file_location}")

def zip_folder():
    
    directory_path = exe_file_location
    
    for foldername in os.listdir(directory_path):
        folder_path = os.path.join(directory_path, foldername)
    
        if os.path.isdir(folder_path):
            zip_file_name = f'{foldername}.zip'
            zip_file_path = os.path.join(directory_path, zip_file_name)

            with zipfile.ZipFile(zip_file_path, 'w') as zipf:
                for root, dirs, files in os.walk(folder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, folder_path)
                        zipf.write(file_path, arcname=arcname)

def exe_file():
    trail_creation_args = zip_folder()
    if trail_creation_args:
            subprocess.run(trail_creation_args)


def main():
    exe_file()

if __name__ == "__main__":
    main()
