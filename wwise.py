# 
# wwise.py
# 
# Author: Jon Evans
# Modified: Oct 19, 2020
# 
# This document provides the a custom OOP approach to the use of the Wise Authoring API. 
# 
# 

from waapi import WaapiClient, CannotConnectToWaapiException, WaapiRequestFailed
from pathlib import PureWindowsPath

import os
from dir_ import Dir


class WAAPI(WaapiClient):
    """
    
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('WAAPI initialised')
        

    def __del__(self):
        self.disconnect()
        print('WAAPI closed safely')
  

    def get_wwise_mac_path(self, path: str) -> str:
        """Convert path to Wwise for Mac

        Args:
            path (str): Any path in any format

        Returns:
            str: Windows path formatted for Wwise for mac
        """
        win_path = PureWindowsPath(f'Y:/{path.strip("../")}')
        win_path = win_path.joinpath()

        return str(win_path)


    def get_audio_import_list(self, file_list: list, abv_dict: dict) -> list:
        """Create a list of dictionaries containing the audio files to be handed
        to the import_files_to_wwise() function

        Args:
            file_list (list): A list of all the audio file paths
            abv_dict (dict): A dictionary of common audio abbreviations

        Returns:
            list: list of dictionaries containing the audio files and target Wwise object paths
        """
        audio_import_list = []

        for file in file_list:
            assert os.path.exists(file)

            file = os.path.relpath(file)

            assert os.path.exists(file)

            filename = os.path.basename(file)
            object_path = '\\Actor-Mixer Hierarchy\\Default Work Unit'

            # Split the filename at the '_', check to see if the element is an abbreviation,
            # Add it to the object_path with the Wwise container type, titled
            for ww_folder in filename.split('_'):    
                if ww_folder[-4:] != '.wav' :
                    ww_folder = abv_dict[ww_folder] if ww_folder in abv_dict else ww_folder
                    object_path += f'\\<Folder>{ww_folder.title()}'

                else:
                    object_path += f'\\<Sound>{filename.strip(".wav")}'

            assert os.path.exists(file)
            audio_import_list.append({'audioFile': f'{self.get_wwise_mac_path(file)}',
                                        'objectPath': object_path})
        
        return audio_import_list


    def import_files_to_wwise(self, file_list: list, abv_dict: dict) -> None:
        """Sends a json of all the files to Wwise to be imported

        Args:
            file_list (list): A list of dictionaries of all the files that need to be added to Wwise
            abv_dict (dict): A dictionary of common audio abbreviations
        """
        audio_import_list = self.get_audio_import_list(file_list, abv_dict)

        args = {

            "importOperation": "useExisting", 
            "default": {
                "importLanguage": "SFX"
            }, 
        "imports": audio_import_list,
        }

        self.call('ak.wwise.core.audio.import', args)


# Running as script not permitted
if __name__ == "__main__":
    pass