#!/usr/bin/env python3
import os
import re
import csv

os.chdir("/home/pi/programs/files/filesystem")

def crawl_dirs(dirs_list, dirs_list_copy, files_list):
    """Crawl directories beginning from current directory and store them in
    dirs_list and csv-files in files_list"""

    current = os.listdir()

    # Parse one directory and store directories and files in lists
    if len(current) > 0:
        for item in current:
            if os.path.isdir(item) and item not in dirs_list:
                fullpath = os.path.join(os.getcwd(), item)
                dirs_list.append(fullpath)
                dirs_list_copy.append(fullpath)

            if os.path.isfile(item) and re.search(r".+\.csv$", item) and item not in files_list:
                fullpath = os.path.join(os.getcwd(), item)
                files_list.append(fullpath)
                print(fullpath)
    else:
        os.chdir("../")

    # Recursively crawl through all directories in dirs_list_copy
    if len(dirs_list_copy) > 0:
        os.chdir(dirs_list_copy.pop())
        return crawl_dirs(dirs_list, dirs_list_copy, files_list)
    else:
        return dirs_list, dirs_list_copy, files_list


def change_files(files_list):
    """Iterate through csv files and change email data"""
    
    while len(files_list) > 0:
        currentfile = files_list.pop()
        with open(currentfile) as file:
            data = csv.reader(file, delimiter=",")
            for row in data:
                # Skip header line
                if row[0] == "Full Name":
                    continue
                    
                # Update host names in the email addresses    
                result = re.sub(r"(.+@)abc\.edu.*", r"\1" + "xyz.com", row[1])
                if result:
                    print(f"name: {row[0]:20}  host: {result}")


def main():

    dirs_list, dirs_list_copy, files_list = [], [], []

    # Call crawl_dirs function
    dirs_list, temp, files_list = crawl_dirs(dirs_list, dirs_list_copy, files_list)

    print("Number of directories: ", len(dirs_list))
    print("Number of csv-files: ", len(files_list))

    change_files(files_list)

    
main()
