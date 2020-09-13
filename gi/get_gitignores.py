import requests
import json


def main():
    req = requests.get("https://api.github.com/repos/github/gitignore/contents/")

    gitignore_dict = {}

    if req.status_code == 200:
        for file in req.json():
            if ".gitignore" in file["name"]:
                name = file["name"].split(".gitignore")[0]
                gitignore = get_gitignore(name)
                print(name)
                gitignore_dict[name.lower()] = gitignore

        with open("gitignore.json", "w") as f:
            json.dump(gitignore_dict, f)
    else:
        print("Network error")


def get_gitignore(path):
    req = requests.get(f"https://raw.githubusercontent.com/github/gitignore/master/{path}.gitignore?raw=true")
    if req.status_code == 200:
        return req.text
