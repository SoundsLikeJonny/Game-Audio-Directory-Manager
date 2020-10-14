from waapi import WaapiClient, CannotConnectToWaapiException, WaapiRequestFailed
from pathlib import PureWindowsPath

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

        return str(path)


    def import_files_to_wwise(self, file_list: yaml, wwise_parent_dir: str):
        """Takes a list of file paths 

        Args:
            file_list (list): [description]
            wwise_parent_dir (str): [description]
        """


audioFile = "/Users/redfm/PycharmProjects/WwiseUE_Dir_Manager/New/Metal/Blades/Impact/Metal_Blades_Impact_01.wav"

def main():
        
    try:

        waapi = WAAPI(url='ws://127.0.0.1:8081/waapi')

        args = {

        "importOperation": "useExisting", 
        "default": {
            "importLanguage": "SFX"
        }, 
        "imports": [
            {
                "audioFile": "/Users/redfm/PycharmProjects/WwiseUE_Dir_Manager/New/Metal/Blades/Impact/Metal_Blades_Impact_01.wav", 
                "objectPath": "\\Actor-Mixer Hierarchy\\Default Work Unit\\<Sequence Container>Test 0\\<Sound SFX>My SFX 0"
            } 
        ],
        "return": [
            "id", 
            "name", 
            "path"
        ]
    }

        result = waapi.call("ak.wwise.core.getInfo")
        
        print(result)



    except CannotConnectToWaapiException:

        print(f'Unable to connect to the WAAPI.')


        
        

# main()


