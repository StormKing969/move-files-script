import os
import shutil

def askQuestion():
    cleanUpLocation = input("Which folder do you want to clean up? ")

    if cleanUpLocation == "":
        print("You did not enter a folder name.")
        exit()

    checkIfExternal = input("Is this an external storage device? Yes or No. ")

    if checkIfExternal == "":
        print("You did not enter an answer.")
        exit()

    if checkIfExternal.lower() == "yes" or checkIfExternal.lower() == "y":
        isExternal = True
        externalStoragePath = input("Enter the path of the folder your want to clean. ")
    else:
        isExternal = False
        externalStoragePath = ""

    # Location that will be cleaned up
    if isExternal:
        directory = os.path.abspath(externalStoragePath)
    else:
        directory = os.path.join(os.path.expanduser("~"), cleanUpLocation)

    # Check if the directory exists
    if not os.path.exists(directory):
        print("The directory does not exist.")
        exit()

    # Check if the directory is empty
    if len(os.listdir(directory)) == 0:
        print("The directory is empty.")
        exit()

    # Check if the directory is a directory
    if not os.path.isdir(directory):
        print("The directory is not a directory.")
        exit()
    
    return directory

def cleanUpLocation(directory):
# The extension of the files.
    extensions = {
        ".jpg": "Images",
        ".jpeg": "Images",
        ".png": "Images",
        ".gif": "Images",
        ".mp4": "Videos",
        ".avi": "Videos",
        ".mov": "Videos",
        ".pdf": "Documents",
        ".txt": "Documents",
        ".doc": "Documents",
        ".docx": "Documents",
        ".ppt": "Documents",
        ".pptx": "Documents",
        ".xls": "Documents",
    }

    for filename in os.listdir(directory):
        # Get the file path of the current file
        file_path = os.path.join(directory, filename)

        # Check if the current file is a file
        if os.path.isfile(file_path):
            # Get the extension of the current file in lowercase
            extension = os.path.splitext(filename)[1].lower()

            if extension in extensions.keys():
                # Check if the directory for the current extension exists
                if not os.path.exists(os.path.join(directory, extensions[extension])):
                    # Create the directory for the current extension
                    os.makedirs(os.path.join(directory, extensions[extension]))
                # Move the current file to the directory for the current extension
                shutil.move(file_path, os.path.join(directory, extensions[extension], filename))
            else:
                if not os.path.exists(os.path.join(directory, "Others")):
                    os.makedirs(os.path.join(directory, "Others"))
                # Move the current file to the directory called "Others" for unknown extension
                shutil.move(file_path, os.path.join(directory, "Others", filename))

    print("All the files have been moved")

def main():
    location = askQuestion()
    cleanUpLocation(location)

if __name__ == "__main__":
    main()