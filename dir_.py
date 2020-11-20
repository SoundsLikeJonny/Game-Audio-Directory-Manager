# 
# dir_.py
# 
# Author: Jon Evans
# Modified: Oct 19, 2020
# 
# The Dir class works as the engine for the the Game Audio Manager app. 
# Allows the user to automatically create audio directories, copying files into the lowest sub-path


import os
import pathlib
import shutil
from pathlib import Path
from DisplayablePath import DisplayablePath

class Dir():
    """
    Provides functionality for modifying the filesystem. 
    Recursively gets directories and filenames.
    Created directories in the parent path.
    """
    def __init__(self, dir_path):
        self.dir_path = dir_path


    def get_dir(self) -> dict:
        """Get all subdirectories from the parent directory.

        Returns:
            dict: dict with dirpath, dirnames, filenames
        """
        file_list = {}
        if os.path.exists(self.dir_path):
            for index, data in enumerate(os.walk(self.dir_path)):
                file_list[index] = {'dirpath': data[0], 'dirnames': data[1], 'filenames': data[2]}
                
        else:
            print('Directory not found')

        return file_list
    

    def get_dir_files_paths(self, parent: str) -> list:
        """Gets just the file names in a dir

        Args:
            parent ([type]): [description]

        Returns:
            list: [description]
        """
        files_list = []
        for dir_index in range(len(parent)):
            for file in parent[dir_index]['filenames']:
                if file[-4:] == '.wav' and file[0] != '.':
                    files_list.append((parent[dir_index]['dirpath'], parent[dir_index]['filenames']))

        return files_list


    def get_dir_list_by_file_name(self, file_tuple_list: list, dir_destination: str, abv_list={}) -> list:
        """Creates a list of file directories according to the file names
 
        Args:
            file_list (list): List of files to be copied
            dir_ (str): [description]
            dir_destination (str): [description]

        Returns:
            list: 
        """
        change_list = []

        for path, file_list in file_tuple_list:

            for file in file_list:

                current_file_location = os.path.join(path,file)
                assert os.path.exists(current_file_location)

                parsed_filename = file.split('_')

                new_dir = dir_destination
                for folder in parsed_filename:

                    if folder[-4:] != '.wav' :
                        folder = abv_list[folder] if folder in abv_list else folder
                        new_dir += f'{folder.title()}/'
                    

                change_list.append({'current_file_location': current_file_location, 'new_location': new_dir})

        return change_list

    
    def create_dir(self, change_list: list, overwrite=False ) -> list:
        """Create new directories and copy files into appropriate folders.

        Args:
            change_list (list): dictionaries of directories to make and files to move

        Returns:
            list: All modified files
        """
        file_list = []

        for change in change_list: 
            path = os.path.join(change['new_location'], os.path.basename(change['current_file_location']))

            if not overwrite and not os.path.exists(path):
                os.makedirs(change['new_location'], exist_ok=True)
                file_dest = shutil.copy(change['current_file_location'], change['new_location'])

                file_list.append(file_dest)
                print(f'-- Moved: {file_dest} --')

        return file_list


    def display_dir(self, parent_dir: str) -> None:
        """Display directory tree

        Args:
            parent_dir (str): Parent directory
        """
        paths = DisplayablePath.make_tree(Path(parent_dir))

        nice_dir = ''

        for path in paths:
            if path.displayable()[-4:] != '.akd':
                nice_dir += f'{path.displayable()}\n'

        return nice_dir
        

# Running as script not permitted
if __name__ == "__main__":
    pass

