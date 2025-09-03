import tempfile
import dataclasses 
import pytest

from os import path, getcwd, chdir
from pathlib import Path

import rovr.tests.utils as testutils
from rovr.app import Application
from rovr.core.file_list import FileList
from rovr.functions import path as path_utils

@dataclasses.dataclass
class TestCase:
    name: str
    init_directory: Path  
    startup_arg: str
    expected_cwd: Path
    expected_focus: str

@pytest.mark.asyncio
async def test_app_init_with_path():
    # Create a temporary directory with a test file
    with tempfile.TemporaryDirectory() as temp_dir:
        # Todo: Do we need realpath here to resolve symlinks ?
        temp_dir = Path(path.realpath(temp_dir))
        dir1 = Path(temp_dir) / "dir1"
        file1_a = Path(temp_dir) / "file1.txt"
        file1_b = dir1 / "file1.txt"
        file2_a = dir1 / ".file2"
        testutils.setup_test_dir(dir1)
        testutils.setup_test_files(file1_a, file1_b, file2_a)
        
        # Dataclass tests > parameterized test  
        # more readable, more type safe
        test_cases: list[TestCase] = [
            TestCase(
                name="No argument",
                init_directory=dir1,
                startup_arg="",
                expected_cwd=dir1,
                expected_focus=path.basename(file2_a),
            ),
            TestCase(
                name="Absolute Path",
                init_directory=temp_dir,
                startup_arg=str(dir1),
                expected_cwd=dir1,
                expected_focus=path.basename(file2_a),
            ),
            TestCase(
                name="Relative path",
                init_directory=dir1,
                startup_arg="..",
                expected_cwd=temp_dir,
                expected_focus=path.basename(dir1),
            ),
            TestCase(
                name="Relative path of file",
                init_directory=temp_dir,
                startup_arg="dir1/.file2",
                expected_cwd=dir1,
                expected_focus=path.basename(file2_a),
            ),
            TestCase(
                name="Non existing directory",
                init_directory=temp_dir,
                startup_arg="dir1/not/existing/path",
                expected_cwd=dir1,
                expected_focus=path.basename(file2_a),
            ),
        ]            
        for t in test_cases:
            await run_test(t)
            print("Passed ", t.name)

async def run_test(t: TestCase) -> None:
    chdir(t.init_directory)
    app = Application(startup_path=t.startup_arg)
    
    async with app.run_test() as pilot:
        # Wait for the app to fully initialize
        await pilot.pause()
        assert getcwd() == str(t.expected_cwd), "cwd not changed as expected"
        
        file_list: FileList = app.query_one("#file_list")
        assert file_list.option_count > 0, "File list is not populated"
        assert file_list.highlighted is not None, "No highglighted object in non empty directory"
        # Verify the target file is highlighted
        highlighted_option = file_list.get_option_at_index(file_list.highlighted)
        highlighted_id: str = highlighted_option.id
        actual_filename = path_utils.decompress(highlighted_id)
        
        assert actual_filename == t.expected_focus, "Wrong item is highlighted"
