import os
from os.path import join
import requests
import sys

imgData = {
    "19A91A05C2":"Jiya",
    "19A91A0570":"Sameera",
    "19A91A05G7":"Ishitaq",
    "19A91A0553":"Jaidheer",
    "19A91A0597":"RamReddy",
    "19A91A05E4":"Sankar",
    "19A91A05B1":"Piyush",
    "19A91A05B6":"Banerjee",
    "21A95A0517":"Nani",
    "21A95A0514":"Sandeep"
}

filePath = join(sys.path[0], "..")
url = "https://info.aec.edu.in/aec/StudentPhotos/{sid}.jpg"

for (sid, name) in imgData.items():
    fileName = (name + ".jpg")

    if not os.path.exists(join(filePath, fileName)):
        try:
            with open(join(filePath, fileName), 'wb') as fileHandle:
                res = requests.get(url = url.format(sid = sid))

                if res.status_code != 200:
                    raise Exception("Couldn't get {0} image".format(sid))
                
                fileHandle.write(res.content)
                print("Got", sid)
        except Exception as exp:
            print(exp)

