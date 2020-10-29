import sys
import webbrowser

from .consts import HELP_TEXT
from .functions import gi_add, gi_clear


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
        gi_add(args)
    elif command == "clear":
        gi_clear()
    elif command in ["source", "github"]:
        webbrowser.open("https://github.com/ninest/gi/")


if __name__ == "__main__":
    main()
