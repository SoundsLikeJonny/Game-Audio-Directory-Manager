from project import Project
from dir_ import Dir

from tkinter import Tk, Button, Pack, filedialog, OptionMenu, StringVar, Label, filedialog, messagebox


def main():
    
    root = Tk()
    root.title('Game Audio Manager')

    window_width = 800
    window_height = 300
    
    root.geometry(f"{window_width}x{window_height}+{int((root.winfo_screenwidth()/2)-(window_width/2))}+{int((root.winfo_screenheight()/2)-(window_height/2))}")

    project = Project()
    
    def front_page(open_project_page):


        all_projects = project.get_projects()

        load_project_label = Label(root, text='Load a Project')
        load_project_label.pack()
        selected_project = StringVar(root)
        selected_project.set('--') # default value
        selected_project_menu = OptionMenu(root, selected_project, *all_projects)
        selected_project_menu.pack()
        load_button = Button(root, text="Load",command=lambda: [load_project(), 
                                                            load_button.destroy(),
                                                            selected_project_menu.destroy(),
                                                            load_project_label.destroy(),
                                                            open_project_page()])

        load_button.pack()


        def load_project():
            project.load_project(selected_project.get())
            load_project_label = Label(root, text=project.get_project_data())
            load_project_label.pack()


    def open_project_page():


        def move_files_to_audio_dir():

            audio_files_parent = filedialog.askdirectory(title='Select the parent folder containing your files')
            print(audio_files_parent)

            if audio_files_parent != '':

                confirm = messagebox.askokcancel(message=f'Use files from "{audio_files_parent}" ?')
                
                if confirm:
                    _dir = Dir(audio_files_parent)
                    file_list  = _dir.get_dir()
                    file_list  = _dir.get_dir_files_paths(file_list)
                    file_list  = _dir.get_dir_list_by_file_name(file_list, project.wwise_project_path, project.get_project_abbreviations())
                    file_list  = _dir.create_dir(file_list)
                    _dir.display_dir(project.wwise_project_path)
        
        transfer_daw_files_label = Label(root, text='Transfer Audio Files from DAW to Audio Directory.\n(Generates directory according to file names)')
        transfer_daw_files_label.pack()
        transfer_daw_files_button = Button(root, text='Select Parent Directory...', command=move_files_to_audio_dir)
        transfer_daw_files_button.pack()
        
    
    
    front_page(open_project_page)


    root.mainloop()

if __name__ == '__main__':
    main()

