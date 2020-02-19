import json
from os import path, getcwd

SKIP_CONFIRMATION = ''
REFERER = ''

def load_pref_json( str ):
    global SKIP_CONFIRMATION
    global REFERER
    print(path.join(getcwd(), str))
    if path.exists(path.join(getcwd(), str)):
        with open(path.join(getcwd(), str)) as json_file:
            data_json = json.load(json_file)
            SKIP_CONFIRMATION = data_json["PARAMETERS"]["SKIP_CONFIRMATION"]
            REFERER = data_json["PARAMETERS"]["REFERER"]


if __name__ == '__main__':

    load_pref_json("prefs.json")
    print("SKIP_CONFIRMATION : " + SKIP_CONFIRMATION)
    print("REFERER : " + REFERER)
