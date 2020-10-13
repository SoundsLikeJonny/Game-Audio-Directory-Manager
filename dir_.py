import os
import pathlib
import shutil
from DisplayablePath import DisplayablePath
from pathlib import Path

class Dir():
    """

    """
    def __init__(self, dir_path):
        self.dir_path = dir_path


    def get_dir(self) -> dict:
        """Get all subdirectories from the parent directory.
        return a dict with dirpath, dirnames, filenames
        """
        file_list = {}
        if os.path.exists(self.dir_path):
            for index, data in enumerate(os.walk(self.dir_path)):
                file_list[index] = {'dirpath': data[0], 'dirnames': data[1], 'filenames': data[2]}
                
        else:
            print('Directory not found')

        return file_list
    

    def get_filenames(self, dir_) -> list:
        """
        """
        files_list = []
        for dir_index in range(len(dir_)):
            files_list += dir_[dir_index]['filenames']

        return [file for file in files_list if file[-4:] == '.wav']


    def create_dir(self, file_list: list, dir_: str, dir_destination: str) -> None:
        """Creates a file directory according to the file names
        """
        for file in file_list:
            filename = file.split('_')
            path = dir_destination

            for folder in filename:

                if folder[-4:] != '.wav':
                    path += f'{folder}/'

            #if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
            shutil.copy(dir_[0]['dirpath']+file, path)
            print(path)

    
    def display_dir(self) -> None:

        paths = DisplayablePath.make_tree(Path(self.dir_path))

        for path in paths:
            if path.displayable()[-4:] != '.akd':
                print(path.displayable())
        



        

if __name__ == "__main__":
    pass

