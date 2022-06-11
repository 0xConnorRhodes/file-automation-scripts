#!/usr/bin/env python3
# Script to format markdown notes created on my phone. Replace spaces with hyphens in filenames and relative links
# Inspired by https://stackoverflow.com/a/62458031
# Author: Connor Rhodes (connor.engineer)

import os

notes_dir = r'/Volumes/enc/notes-test'

replacement_char = '-'

for root, dirs, files in os.walk(notes_dir):

    for current_filename in files:
        new_filename = current_filename.replace(' ', replacement_char)

        print(f"current filename: {current_filename}")
        print(f"    new filename: {new_filename}")

        os.rename(
            os.path.join(root, current_filename), 
            os.path.join(root, new_filename)
        )   
