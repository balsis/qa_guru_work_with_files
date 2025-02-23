import os


class Paths:
    CURRENT_FILE = os.path.abspath(__file__)
    CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE)
    PARENT_DIRECTORY = os.path.dirname(CURRENT_DIRECTORY)
    TMP_DIR = os.path.join(PARENT_DIRECTORY, "temp")
    ARCHIVE_PATH = os.path.join(PARENT_DIRECTORY, "archive")
    ARCHIVE_FILE = os.path.join(ARCHIVE_PATH, "archive.zip")
    FILES = os.listdir(TMP_DIR)
