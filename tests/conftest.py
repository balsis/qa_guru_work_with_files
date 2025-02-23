import os.path
import shutil
from enum import Enum

import pytest
from zipfile import ZipFile

from helpers.Paths import Paths


class FileExtension(Enum):
    CSV = ".csv"
    XLSX = ".xlsx"
    PDF = ".pdf"


@pytest.fixture(scope = "class", autouse = True)
def create_archive():
    if not os.path.exists(Paths.ARCHIVE_PATH):
        os.mkdir(Paths.ARCHIVE_PATH)
    with ZipFile(Paths.ARCHIVE_FILE, "w") as zf:
        for file in Paths.FILES:
            add = os.path.join(Paths.TMP_DIR, file)
            zf.write(add, os.path.basename(add))
    yield
    shutil.rmtree(Paths.ARCHIVE_PATH)


@pytest.fixture
def csv_file():
    with ZipFile(Paths.ARCHIVE_FILE) as zf:
        for current_file_name in zf.namelist():
            if current_file_name.endswith(FileExtension.CSV.value):
                return zf.open(current_file_name)
    return None


@pytest.fixture
def pdf_file():
    with ZipFile(Paths.ARCHIVE_FILE) as zf:
        for current_file_name in zf.namelist():
            if current_file_name.endswith(FileExtension.PDF.value):
                return zf.open(current_file_name)
    return None


@pytest.fixture
def xlsx_file():
    with ZipFile(Paths.ARCHIVE_FILE) as zf:
        for current_file_name in zf.namelist():
            if current_file_name.endswith(FileExtension.XLSX.value):
                return zf.open(current_file_name)
    return None
