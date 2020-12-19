import sys
import webbrowser

from .constants import HELP_TEXT, LANGUAGES_LIST
from .functions import gitignore_add, gitignore_clear


def main():
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        args = sys.argv[2:]
        run(command, args)
    else:
        print(HELP_TEXT)


def run(command, args):
    if command == "help":
        print(HELP_TEXT)

    elif command in ["add", "a"]:
        gitignore_add(args)

    elif command in ["list"]:
        print(", ".join(LANGUAGES_LIST))

    elif command in ["clear"]:
        gitignore_clear()
    elif command in ["source", "github"]:
        webbrowser.open("https://github.com/ninest/gi/")


if __name__ == "__main__":
    main()
