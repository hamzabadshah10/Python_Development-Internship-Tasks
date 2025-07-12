import os
import re

folder_path = input("\nEnter folder path: ")

if os.path.isdir(folder_path):

    print("\nMatching .txt files that start with 'report':")

    for file_name in os.listdir(folder_path):

        if file_name.endswith(".txt") and re.match(r'^report.*\.txt$', file_name):
            print(file_name)
else:

    print("Folder not found. Invalid path entered!")
