# cross compatible Game Audio pipeline optimization script 
# pseudocode

import os  # For directory changes and gui scripting
import ue4plugin  # To script in ue4 //not sure about this
import requests  # For performing http curl commands with Wwise

POSSIBLE_OS = ['PC', 'MAC', ''] # Linux is unlikely
ABBREVIATIONS = {'PLY': 'Player',
                 'CHR': 'Character,
                 'ENV': 'Environment Sounds',
                 'FS': 'Footsteps',
                 'UI': 'UI Sounds',
                 .... etc ....
                 } # This could be contained in a .txt and read to the script at runtime

os_type = None #  global variable with the current OS type


def function to get the os type:
    get the type of os (mac, pc, linux)
    return current os


def function to set the os type:
    
    for each item in POSSIBLE_OS:
        if os is equal to index of POSSIBLE_OS then:
            set os_type to the os type
            return


def function export pro tools marker .txt:
    
    if os_type  then:
        is Pro Tools running:
            click menu item 'export timeline markers as .txt'
            save to within Pro Tools session
    check against other os types

    return the filepath of the .txt

# filepath to timeline_markers.txt as argument
def function bounce audio files to Pro Tools bounced files folder:
    
    if os_type  then:
        is Pro Tools running:
            
            read the timeline_markers.txt file
            determine where to bounce and what file names
            for each marker:
                put these into marker_list of tuples
                    
            for each item in marker_list:
                read 0 of tuple of current marker_list index # The time in the Pro Tools session
                go to that marker in pro Tools
                select the region
                bounce using 1 of tuple current marker_list index # the marker name

    check against other os types
    
    return the filepath to the bounced files folder 


def create_folder_directory(a list of .wav files file_list, filepath):

    updated_filepaths_list = [] # a list of the filepaths with new files
        
    for each file:
        set file_hierarchy_list to split the file name, seperating by '_'

        current_filepath = filepath
        for each item in file_hierarchy_list:

            if index item is in ABBREVIATIONS then:
                set current_filepath to current_filepath and the value of ABBREVIATIONS using index item as key

            else if it is the last item in file_hierarchy_list then:
                copy files into the current_filepath
                append file path to updated_filepaths_list

            else:
                create the folder using the the value of ABBREVIATIONS using index item as key

    return updated_filepaths_list
            


# filepath to Pro Tools bounced files folder as argument
def function copy the files into the wwise project folder:

    .wav_list = all the .wav files at the file location
    send .wav_list and the wwise project filepath to create_folder_directory function
    set previous result to updated_filepaths_list

    return updated_filepaths_list


def create wwise containers (updated_filepaths_list):
    prompt user to determine where in Wwise to create container names for the new files 
    for each file in updated_filepaths_list:
        create a container


def create wwise events:
    prompt user to determine the containers to be created into events
    for each container:
        creat an event, using the naming convention used when importing


def create_UE4_folder_directory(a list of wwise event path file_list, filepath):
    similar to create_folder_directory but would be created in unreal
    copies the wwise events from the wwise project into the unreal project 
        


    
