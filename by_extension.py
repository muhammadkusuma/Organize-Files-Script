import os
import shutil


def sort_files_by_extension(directory):
    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1][1:].lower()

            if file_extension:
                extension_folder = os.path.join(directory, file_extension)

                if not os.path.exists(extension_folder):
                    os.makedirs(extension_folder)

                shutil.move(file_path, os.path.join(extension_folder, filename))

    print(f"Files in '{directory}' have been sorted by extension.")


def main():
    print("File Sorter Based on Extension")
    directory = input("Enter the full path of the folder you want to sort: ")
    sort_files_by_extension(directory)


if __name__ == "__main__":
    main()
