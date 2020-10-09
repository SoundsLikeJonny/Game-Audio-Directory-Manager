import argparse
import yaml
import shutil

class Project():

    def __init__(self, project_path, wwise_project_path, ue4_project_path, audio_directory):
        self.project_path = self.set_project_path(project_path) or None
        self.wwise_project_path = self.set_wwise_project_path(wwise_project_path) or None
        self.ue4_project_path = self.set_ue4_project_path(ue4_project_path) or None
        self.audio_directory = self.set_audio_directory(audio_directory) or None
        


    def __repr__(self):
        return repr(self.__dict__)


    def set_project_path(self, project_path):
        """[summary]

        Args:
            project_path ([type]): [description]
        """
        pass


    def set_wwise_project_path(self, project_path: str) -> None:
        """[summary]

        Args:
            project_path (str): [description]
        """
        pass


    def set_ue4_project_path(self, project_path: str) -> None:
        """[summary]

        Args:
            project_path (str): [description]
        """
        
        pass


    def set_audio_directory(self, audio_dir_path: str) -> None:
        """[summary]

        Args:
            audio_dir_path (str): [description]
        """
        
        pass


    def get_abbreviations(self) -> dict:
        """

        Args:
            path ([type]): [description]

        Returns:
            yaml: [description]
        """
        try:
            file = open(f'{self.project_path}/audio_abbreviations.yaml')
            return yaml.load(file)
        except FileNotFoundError as e:
            assert e


    def copy_abbreviations_dir(self,source_path: str, destination_path: str):
        """[summary]

        Args:
            source_path (str): [description]
            destination_path (str): [description]
        """
        shutil.copyfile(f'{self.project_path}/audio_abbreviations.yaml', destination_path)
        pass
          


    def create_project(self) -> None:
        """[summary]
        """
        pass


def main():
    project_path = ''
    wwise_project_path = '/Users/jonevans/Documents/Unreal Projects/Survival/Survival_WwiseProject'
    ue4_project_path = '/Users/jonevans/Documents/Unreal Projects/Survival'
    audio_directory = '/Users/jonevans/Documents/Unreal Projects/Survival/Survival_WwiseProject/Originals/SFX'

    project = Project(project_path, audio_directory, wwise_project_path, ue4_project_path)

    print(project.get_abbreviations_yaml())


if __name__ == "__main__":
    main()