from waapi import WaapiClient, CannotConnectToWaapiException

from pprint import pprint


try:

    client = WaapiClient(allow_exception=True)

    result = client.call("ak.wwise.core.getInfo")

    print(result)

    client.disconnect()


except CannotConnectToWaapiException:

    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")



