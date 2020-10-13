from project import Project
from dir_ import Dir
import argparse


def main():

    project = Project()
    project.load_project()

    protools_session_folder = '/Users/jonevans/PycharmProjects/WwiseUE_Dir_Manager/Metal_Blades/'

    directory = Dir(project.audio_directory)
    directory.display_dir()

    


    """

    dest_path = '/Users/jonevans/PycharmProjects/WwiseUE_Dir_Manager/New/'

    dir_ = Dir(protools_session_folder)
    directory = dir_.get_dir()
    file_names = dir_.get_filenames(directory)
    print(file_names)
    dir_.create_dir(file_names, directory, dest_path)




    project_name = 'Survival'
    project_path = 'Projects'
    wwise_project_path = '/Users/jonevans/Documents/Unreal Projects/Survival/Survival_WwiseProject/Survival_WwiseProject.wproj'
    ue4_project_path = '/Users/jonevans/Documents/Unreal Projects/Survival'
    audio_directory = '/Users/jonevans/Documents/Unreal Projects/Survival/Survival_WwiseProject/Originals/SFX'

    project = Project()
    project.create_project(project_name, project_path, audio_directory, wwise_project_path, ue4_project_path)
    project.set_audio_directory('/Users/jonevans/Documents/Unreal Projects/Survival/')

    """

if __name__ == '__main__':
    main()