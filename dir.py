import os

class Dir():
    """
    """
    def __init__(self, dir_):
        self.dir = dir_


    def get_dir(self) -> dict:  
        
        file_list = {}

        if os.path.exists(self.dir):
            for index, data in enumerate(os.walk(self.dir)):
                file_list[index] = {'dirpath': data[0], 'dirnames': data[1], 'filenames': data[2]}

        return file_list


# TODO : 
if __name__ == "__main__":

    protools_session_folder = '/Users/jonevans/Documents/Clients/Jon Evans/Bubluv/Bounced Files/IMPACT'

    directory = Dir(protools_session_folder).get_dir()

    files_list = []
    for dir_index in directory:
        files_list += directory[dir_index]['filenames']
        
    files_list = [file for file in files_list if file[-4:] != '.wav']

print(files_list)
    

    



