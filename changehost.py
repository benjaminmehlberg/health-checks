#!/usr/bin/env python3
import os
import re
import csv

filesystem = os.path.expanduser("~/programs/files/filesystem")
os.chdir(filesystem)


def crawl_dirs(dirs_all, dirs_process, files_all):
    """
    Crawl directories beginning from current directory and store them in
    dirs_all and csv-files in files_all
    """

    current_dir = os.listdir()

    # Parse one directory and store directories and files in lists
    if current_dir:
        for item in current_dir:
            if os.path.isdir(item) and item not in dirs_all:
                fullpath = os.path.join(os.getcwd(), item)
                dirs_all.append(fullpath)
                dirs_process.append(fullpath)

            if os.path.isfile(item) and re.search(r".+\.csv$", item) and item not in files_all:
                fullpath = os.path.join(os.getcwd(), item)
                files_all.append(fullpath)
                print("Found csv-file: ",fullpath)
    else:
        os.chdir("../")

    # Recursively crawl through all directories in dirs_process
    if dirs_process:
        os.chdir(dirs_process.pop())
        return crawl_dirs(dirs_all, dirs_process, files_all)
    else:
        return dirs_all, dirs_process, files_all


def change_files(files_all):
    """
    Iterate through csv files and change email data
    """
    while files_all:
        current_file = files_all.pop()
        with open(current_file) as file:
            data = csv.reader(file, delimiter=",")
            for row in data:
                # Skip header line
                if row[0] == "Full Name":
                    continue
                    
                # Update host names in the email addresses    
                result = re.sub(r"(.+@)abc\.edu.*", r"\1" + "newhost.com", row[1])
                if result:
                    print(f"Name: {row[0]:20}  Email: {result}")


def main():

    # Call crawl_dirs function
    dirs_all, dirs_process, files_all = crawl_dirs(list(), list(), list())

    print("Number of csv-files: ", len(files_all), "\n")

    change_files(files_all)

    
main()
