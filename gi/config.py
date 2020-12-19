from dotenv import load_dotenv
import os

load_dotenv()

GITIGNORE_FILE_PATH = os.getenv("GITIGNORE_FILE_PATH") or ".gitignore"
