from project import Project
from dir_ import Dir
import argparse


def main():
    
    # parser = argparse.ArgumentParser(description='DAW -> Wwise -> UE4 Directory Manager!',
    #                                     add_help=True)

    # project = Project()

    # parser.version = '1.0'
    # parser.add_argument('--load', action='store', nargs='?', dest=project.load_project())
    # parser.add_argument('-i', action='store', nargs='?', dest=project.audio_directory)
    
    # parser.add_argument('-p', action='store')

    # parser.add_argument('-v', action='version')

    # args = parser.parse_args()

    # print(args)

    project = Project()
    project.load_project()

    action = None
    while action != 0:

        actions =   f"""
        1. Copy files to Audio Directory: {project.wwise_project_path}\n
        2. \n
        0. Exit\n
        """

        action = int(input(f'\nProject {project.project_name}:\n' + actions))


        if action == 1:

            parent_dir = input('Paste parent directory: ')

            _dir = Dir(parent_dir)
            file_list  = _dir.get_dir()
            file_list  = _dir.get_dir_files_paths(file_list)
            file_list  = _dir.get_dir_list_by_file_name(file_list, project.wwise_project_path, project.get_project_abbreviations())
            file_list  = _dir.create_dir(file_list)
            _dir.display_dir(project.wwise_project_path)

        
            
        if action == 2:
            pass
            

if __name__ == '__main__':
    main()