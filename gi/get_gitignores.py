import requests


def generate_gitignore_list():
    req = requests.get("https://api.github.com/repos/github/gitignore/contents/")

    if req.status_code == 200:

        languages_list = []

        for file in req.json():
            if ".gitignore" in file["name"]:
                languages_list.append(file["name"].split(".gitignore")[0])

        print(languages_list)

    else:
        # TODO: create and throw and Error
        print("Network error :/")


def get_gitignore(name):
    req = requests.get(f"https://raw.githubusercontent.com/github/gitignore/master/{name}.gitignore?raw=true")
    if req.status_code == 200:
        return req.text
    else:
        # TODO: create and throw and Error
        print("Network error :/")
