import yaml
import shutil
import os

class Project():

    def __init__(self):
        self.project_path = None
        self.wwise_project_path = None
        self.ue4_project_path = None
        self.audio_directory = None
        self.project_name = None


    def __repr__(self):
        return repr(self.__dict__)


    def set_wwise_project_path(self, dir_path: str) -> None:
        """[summary]

        Args:
            project_path (str): [description]
        """
        self.set_yaml_dict_value_by_key(self.project_path, 'wwise_project_path', dir_path)


    def set_ue4_project_path(self, dir_path: str) -> None:
        """[summary]

        Args:
            project_path (str): [description]
        """  
        self.set_yaml_dict_value_by_key(self.project_path, 'ue4_project_path', dir_path)        


    def set_audio_directory(self, dir_path: str) -> None:
        """[summary]

        Args:
            dir_path (str): [description]
        """        
        self.set_yaml_dict_value_by_key(self.project_path, 'audio_directory', dir_path)
        
        
    def set_yaml_dict_value_by_key(self, yaml_file_path: str, dict_key: str, dict_value: str):
        """Opens a .yaml file and allows a value to be changed 

        Args:
            yaml_file_path (str): [description]
            directory_path (str): [description]
        """               
        try:
            with open(yaml_file_path, 'r') as file:
                data = yaml.load(file)
                data[dict_key] = dict_value
                
            with open(yaml_file_path, 'w') as file:
                yaml.dump(data, file, default_flow_style=False)
                
        except FileNotFoundError as e:
            print(e)


    def get_project_abbreviations(self) -> dict:
        """calls the get_yaml_data method to get the data from the project /audio_abbreviations.yaml 

        Returns:
            dict: 
        """        
        return self.get_yaml_data(f'{self.project_path}/audio_abbreviations.yaml')


    def get_yaml_data(self, file_path) -> dict:
        try:
            file = open(file_path, 'r')
            return yaml.load(file)
        except FileNotFoundError as e:
            print(e)


    def copy_abbreviations_dir(self, destination_path: str):
        """Copy a the 'audio_abbreviations.yaml' file to the target directory

        Args:
            destination_path (str): Directory to copy the .yaml file into
        """        
        shutil.copyfile('audio_abbreviations.yaml', f'{destination_path}/audio_abbreviations.yaml')    


    def create_project(self, project_name, project_path, wwise_project_path, ue4_project_path, audio_directory) -> None:
        """[summary]
        """
        self.project_path = project_path
        self.wwise_project_path = wwise_project_path
        self.ue4_project_path = ue4_project_path
        self.audio_directory = audio_directory
        self.project_name = project_name

        try:
            self.project_path = f'{self.project_path}/{self.project_name}'
            os.makedirs(self.project_path, exist_ok=True)

            paths_dict = {'project_name': self.project_name, 
                            'wwise_project_path': self.wwise_project_path,
                            'ue4_project_path'  : self.ue4_project_path,
                            'audio_directory'   : self.audio_directory}

            self.project_file = f'{self.project_path}/project.yaml'
            
            with open(f'{self.project_path}/project.yaml', 'w') as file:
                yaml.dump(paths_dict, file, default_flow_style=False)

            self.copy_abbreviations_dir(self.project_path)
        
        except:
            assert 'Error creating project file'


    def load_project(self):
        # TODO: project = input(f'Select a project {os.listdir("./Projects")}')
        project = 'Survival'


        project = self.get_yaml_data(f'./Projects/{project}/project.yaml')
        
        self.project_name = project['project_name']
        self.wwise_project_path = project['wwise_project_path']
        self.ue4_project_path = project['ue4_project_path']
        self.audio_directory = project['audio_directory']


if __name__ == "__main__":
    pass