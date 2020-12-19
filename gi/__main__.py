import sys
import webbrowser

# from .config import GITIGNORE_FILE_PATH


def main():
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        args = sys.argv[2:]
        run(command, args)
    else:
        print("Help text")


def run(command, args):
    if command == "help":
        print("help text")
    elif command in ["add", "a"]:
        print("add")
        print(args)
    elif command in ["source", "github"]:
        webbrowser.open("https://github.com/ninest/gi/")


if __name__ == "__main__":
    main()
