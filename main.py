# 
# 
# 
# 
# 
# 
# 
# 
# 


from project import Project
from dir_ import Dir
from wwise import WAAPI

from tkinter import Tk, Button, Pack, filedialog, OptionMenu, StringVar, Label, filedialog, messagebox
import tkinter


def main():
    
    # Create the main window
    root = Tk()
    root.title('Game Audio Manager')

    window_width = 800
    window_height = 300
    
    # Set the window size and center on screen
    root.geometry(f"{window_width}x{window_height}"\
        f"+{int((root.winfo_screenwidth()/2)-(window_width/2))}"\
            f"+{int((root.winfo_screenheight()/2)-(window_height/2))}")

    # Create an empty project object to either create a new or load an existing project
    project = Project()
    
    def front_page(open_project_page: object) -> None:
        """Creates the tkinter widgets and provides functions for the front page

        Args:
            open_project_page (function): Function opening the next project page
        """

        all_projects = project.get_projects()

        # Create the load project widgets
        load_project_label = Label(root, text='Load a Project')
        load_project_label.pack()
        selected_project = StringVar(root)
        selected_project.set('--') # default value
        selected_project_menu = OptionMenu(root, selected_project, *all_projects)
        selected_project_menu.pack()
        load_button = Button(root, text="Load",command=lambda: [load_project(), 
                                                            destroy_main_page(),
                                                            open_project_page()])

        load_button.pack()

        # Create the new project widgets
        new_project_label = Label(root, text='Start A New Project')
        new_project_label.pack()
        new_project_button = Button(root, text="New Project",command=lambda: [new_project(), 
                                                            destroy_main_page()])
        new_project_button.pack()
    

        def destroy_main_page() -> None:
            """Destroy all widgets from the main page
            """
            load_button.destroy()
            selected_project_menu.destroy()
            load_project_label.destroy()
            new_project_button.destroy()
            new_project_label.destroy()
        

        def new_project() -> None:
            # TODO: Setup new project prompts and filedialog.askdirectory

            
            pass


        def load_project() -> None:
            """Load the project information into the project object and display the project data
            """
            project.load_project(selected_project.get())
            load_project_label = Label(root, text=project.get_project_data())
            load_project_label.pack()


    def open_project_page() -> None:
        """Creates the tkinter widgets and provides functions for the project page
        """

        def move_files_to_audio_dir() -> None:
            """Prompts the user to select the parent audio directory, then prompts confirmation of actions.
            Creates the audio directory
            """
            audio_files_parent = filedialog.askdirectory(title='Select the parent folder containing your files')

            if audio_files_parent != '':
                confirm = messagebox.askokcancel(message=f'Use files from "{audio_files_parent}" ?')
                
                # Initialises a Dir() object, and creates a directory of subfolders under the parent
                if confirm:
                    _dir = Dir(audio_files_parent)
                    file_list  = _dir.get_dir()
                    file_list  = _dir.get_dir_files_paths(file_list)
                    file_list  = _dir.get_dir_list_by_file_name(file_list, project.wwise_project_path, project.get_project_abbreviations())
                    file_list  = _dir.create_dir(file_list)

                    project.set_wwise_audio_changelist(file_list)
                    

        def import_to_wwise() -> None:
            """Establishes a connection with the Wwise Authoring API and imports the files
            """
            confirm = messagebox.askokcancel(message=f'Import files to Wwise?')

            if confirm:
                url='ws://127.0.0.1:8081/waapi'
                
                waapi_label = Label(root, text=f'Connecting to WAAPI on {url}...')
                waapi_label.pack()

                wwise = WAAPI(url=url)

                waapi_label.configure(text=f'WAAPI connected on {url}')
                waapi_label.pack()

                wwise.import_files_to_wwise(project.get_wwise_audio_changelist(), project.get_project_abbreviations())

                    
        def view_change_list(change_list: list) -> None:
            """Displays the changelist to the user

            Args:
                change_list (list): List of files to be displayed
            """
            change_list_str = ''
            for file in change_list:
                change_list_str += f'...{file[-40:]}\n\n' 

            messagebox.showinfo(title='Audio Files to Move to Wwise', message=change_list_str)

        # Create the widgets for transfering files
        move_files_to_audio_dir_label = Label(root, text='Transfer Audio Files from DAW to Audio Directory.\n'
                                                        +'(Generates directory according to file names)')
        move_files_to_audio_dir_label.pack()
        move_files_to_audio_dir_button = Button(root, text='Select Parent Directory...', command=move_files_to_audio_dir)
        move_files_to_audio_dir_button.pack()

        # Widgets for Importing to Wwise
        import_to_wwise_label = Label(root, text='Import audio files to Wwise project from changelist')
        import_to_wwise_label.pack()
        
        # If there is a changelist available, then create the widgets
        if (change_list := project.get_wwise_audio_changelist()) != None:
            change_list_label = Label(root, text='Changelist Available')
            change_list_label.pack()
            change_list_button = Button(root, text='See change list', command=lambda: view_change_list(change_list))
            change_list_button.pack()

        import_to_wwise_button = Button(root, text='Import to Wwise', command=import_to_wwise)
        import_to_wwise_button.pack()


    # Open the front page, passing the functions as parameters for other widgets to make
    front_page(open_project_page)

    root.mainloop()


# Call main function
if __name__ == '__main__':
    main()

