import requests
from .constants import LANGUAGES_LIST, ERROR_MESSAGE
from .config import GITIGNORE_FILE_PATH


def gitignore_add(names):
    """
    Adds gitignores to gitignore

    Parameters:
        names (list[string]): Names of langauges/frameworks to add
    """

    languages_to_add = []

    for name in names:
        """
        Get the correct case of the name through comparison with with
        constants.py. For the time being, both frameworks and languages will be
        reffered to as languages for simplicity
        """

        lowercase_languages_list = [language_name.lower() for language_name in LANGUAGES_LIST]

        if name.lower() in lowercase_languages_list:
            index = lowercase_languages_list.index(name.lower())

            # Get language name with correct case
            language_name = LANGUAGES_LIST[index]
            languages_to_add.append(language_name)

        else:
            print("The gitignore template {name} does not exist")

    """
    Generate display_string to display which languages are being added.
    TODO: replace last command with (", and")
    """

    display_string = ", ".join(languages_to_add)
    print(f"Adding {display_string} to {GITIGNORE_FILE_PATH}")

    # Add languages to gitignore
    gitignore = ""

    for language in languages_to_add:
        langauge_gitignore = get_gitignore(language_name)
        gitignore += f"# {language_name}\n{langauge_gitignore}\n\n"

    gitignore_file = open(GITIGNORE_FILE_PATH, "a")
    gitignore_file.write(gitignore)
    gitignore_file.close()


def get_gitignore(language_name):
    """
    Get the gitignore as a string from github.com/github/gitignore.

    Parameters:
        language_name (string): The language/framework name. Note that language
        refers to language or framework.
    """

    request = requests.get(
        f"https://raw.githubusercontent.com/github/gitignore/master/{language_name}.gitignore?raw=true"
    )
    if request.status_code == 200:
        return request.text
    else:
        print(ERROR_MESSAGE)


def gitignore_clear():
    open(GITIGNORE_FILE_PATH, "w").close()
    print(".gitignore cleared")
