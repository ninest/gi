import json

with open("gitignore.json") as f:
    gitignore_dict = json.load(f)


def gi_add(templates):
    print(f"Adding {templates}")

    string = ""

    for name in templates:
        string += f"# {name.upper()}\n{gitignore_dict[name]}\n\n\n"

    # add to .gitignore
    dot_gitignore = open(".gitignore-test", "a")
    dot_gitignore.write(string)
    dot_gitignore.close()

    print(".gitignore edited")


def gi_clear():
    open(".gitignore-test", "w").close()

    print(".gitignore cleared")
