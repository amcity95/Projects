import json
import os


def make(x):
    path = "user_data.json"
    if not os.path.isfile(path):
        with open("user_data.json", "w") as f:
            json.dump(x, f, indent=4)

    with open("user_data.json", "r") as f:
        read = json.load(f)

    with open(path, "w") as r:
        new_dict={**read}

        json.dump(x, r, indent=4)
def newup():
    pass