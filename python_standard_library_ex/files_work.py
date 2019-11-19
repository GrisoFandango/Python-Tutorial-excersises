from pathlib import Path
from time import ctime
import shutil
# refer to a path of a file
path = Path(r"package_example\__init__.py")
path.exists()  # to check if exist
path.rename("init.txt")  # to rename it
path.unlink()  # another way to delete
print(path.stat())  # stat give us stats about file
print(ctime(path.stat().st_ctime))  # ctime is creation time


# the read and write method do not require to open and close the file
path.read_bytes()  # read as a bites giving binary data
print(path.read_text())  # read it as a string

# path.write.text(....)  # to write a text
# path.write.bytes()  # to write as abytes

# how to copy a file
# create a variable with the source file
source = Path(r"package_example\__init__.py")
# create the target location
target = Path(r"\__init__.py")
# read content of the source anbd then write to the target
target.write_text(source.read_text())  # can be a bit tedious

# we can use the shutil module to make it easier
shutil.copy(source, target)
