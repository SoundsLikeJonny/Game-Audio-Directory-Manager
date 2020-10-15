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
        win_path = PureWindowsPath('Z:\\' + path)
        win_path = win_path.joinpath()

        return str(win_path)


    def get_audio_import_list(self, file_list: list, abv_dict: dict) -> list:
        
        audio_import_list = []

        for file in file_list:
            
            filename = os.path.basename(file)
            object_path = '\\Actor-Mixer Hierarchy\\Default Work Unit'

            for ww_folder in filename.split('_'):
                
                if ww_folder[-4:] != '.wav' :

                    ww_folder = abv_dict[ww_folder] if ww_folder in abv_dict else ww_folder
                    object_path += f'\\<Folder>{ww_folder.title()}'

                else:

                    object_path += f'\\<Sound>{filename.strip(".wav")}'


            audio_import_list.append({'audioFile': f'{self.get_wwise_mac_path(file)}',
                                        'objectPath': object_path})
        
        return audio_import_list



# [
#             {
#                 "audioFile": "", 
#                 "objectPath": "\\Actor-Mixer Hierarchy\\Default Work Unit\\"
#             } 
#         ]


    def import_files_to_wwise(self, file_list: list, abv_dict: dict):
        """Takes a list of file paths 

        Args:
            file_list (list): [description]
            wwise_parent_dir (str): [description]
        """
        audio_import_list = self.get_audio_import_list(file_list, abv_dict)

        print(audio_import_list)

        args = {

        "importOperation": "useExisting", 
        "default": {
            "importLanguage": "SFX"
        }, 
        "imports": audio_import_list,
        }

        self.call('ak.wwise.core.audio.import', args)

        



def main():

   pass
    # try:

    #     waapi = WAAPI(url='ws://127.0.0.1:8081/waapi')
    #     result = waapi.call("ak.wwise.core.getInfo")       
    #     print(result)

    # except CannotConnectToWaapiException:

    #     print(f'Unable to connect to the WAAPI.')


