import os

def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir("/home/air-walk/workspaces/udacity-programming-foundations-with-python/lesson-2/secret-message")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory: " + saved_path)
    os.chdir("/home/air-walk/workspaces/udacity-programming-foundations-with-python/lesson-2/secret-message")
    
    # (2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))

    os.chdir(saved_path)
rename_files()
