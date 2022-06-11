#!/usr/bin/env python3

import os

directory = r'/Volumes/enc/notes-test'

# Use underscore? Otherwise defaults to hyphen
is_use_underscore = False
replacement_char = '-'

print("Renaming files now!")
for root, dirs, files in os.walk(directory):
    print(f"root: {root}")
    print(f"dirs: {dirs}")
    print(f"files: {files}")

    for current_filename in files:
        new_filename = current_filename.replace(' ', replacement_char)

        print(f"current filename: {current_filename}")
        print(f"    new filename: {new_filename}")

        os.rename(
            os.path.join(root, current_filename), 
            os.path.join(root, new_filename)
        )   

print("All done!")
