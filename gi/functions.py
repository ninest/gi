from .constants import LANGUAGES_LIST


def gitignore_add(names):
    """
    Adds gitignores to gitignore

    Parameters:
        names (list[string]): Names of langauges/frameworks to add
    """

    gitignore = ""

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
            langauae_gitignore = get_gitignore(language_name)
            gitignore += f"# {language_name}\n{langauae_gitignore}\n\n"

        else:
            print("The gitignore template {name} does not exist")


def get_gitignore(language_name):
    ...
