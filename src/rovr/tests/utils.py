from os import mkdir
from pathlib import Path
TEST_FILE_CONTENT_1 = "file data"

# Let the exceptions roam wild
def setup_test_dir(*args: Path):
    for dir in args:
        mkdir(dir)   

# Let the exceptions roam wild
def setup_test_files(*args: Path):
    for file in args:
        file.write_text(TEST_FILE_CONTENT_1) 
