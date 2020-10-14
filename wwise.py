from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint

from pathlib import PureWindowsPath


def main():
        
    try:

        client = WaapiClient()

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

        result = client.call("ak.wwise.core.getInfo")

        print(result)

        client.disconnect()


    except CannotConnectToWaapiException:

        print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")

audioFile = "/Users/redfm/PycharmProjects/WwiseUE_Dir_Manager/New/Metal/Blades/Impact/Metal_Blades_Impact_01.wav"

win_path = PureWindowsPath(audioFile)
win_path = win_path.r#.split(r'\\')

print(win_path)

