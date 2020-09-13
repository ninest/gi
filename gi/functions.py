import json
from .get_gitignores import get_gitignore


gitignore_path = ".gitignore-test"
languages_list = []


with open("gitignores.json") as f:
    languages_list = json.load(f)


def gi_add(names, gitignore_path=gitignore_path):
    print(f"Adding {names}")

    gitignore_string = ""

    for name in names:
        # get correct case (good use of walrus?)
        lowercase_languages_list = [language.lower() for language in languages_list]
        if name.lower() in lowercase_languages_list:
            index = lowercase_languages_list.index(name.lower())

            # language name with correct case
            language_name = languages_list[index]
            gitignore = get_gitignore(language_name)
            gitignore_string += f"# ${name}\n" + gitignore + "\n\n"

    # add to .gitignore
    dot_gitignorefile = open(gitignore_path, "a")
    dot_gitignorefile.write(gitignore_string)
    dot_gitignorefile.close()

    print(".gitignore edited")


def gi_clear(gitignore_path=gitignore_path):
    open(gitignore_path, "w").close()

    print(".gitignore cleared")
