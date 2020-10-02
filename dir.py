import os
import yaml
import pathlib

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

    def get_filenames(self, dir_):
        """
        """
        files_list = []
        for dir_index in range(len(dir_)):
            files_list += dir_[dir_index]['filenames']
            
        return [file for file in files_list if file[-4:] == '.wav']


    def create_dir(self, file_list: list, dir_destination: str) -> None:
        """Creates a file directory according to the file names
        """
        for file in file_list:
            if file[-4:] != '.wav':
                filename = file.split('_')
                print(filename)
                path = dir_destination

            for folder in filename:
                path += f'{folder}/'
                print(path)
            



# TODO : 
if __name__ == "__main__":

    protools_session_folder = '/Users/redfm/PycharmProjects/WwiseUE_Dir_Manager/Metal_Blades'

    dest_path = '/Users/redfm/PycharmProjects/WwiseUE_Dir_Manager/New'

    dir_ = Dir(protools_session_folder)

    directory = dir_.get_dir()

    file_names = dir_.get_filenames(directory)

    dir_.create_dir(file_names, dest_path)
    
    

