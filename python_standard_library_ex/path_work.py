from pathlib import Path

# r stand for raw string to not use escape character
# Path(r"c:\Program Files\Microsoft")
# Path()  # current folder
# Path(r"ecommerce\__init__.py")  # relative folder
# Path() / "ecommerce" / "__init__.py" #combine multiple Path object
# Path.home() #return home dir of current user

path = Path(r"package_example\__init__.py")  # relative folder
print(path.exists())  # check if exist
print(path.is_file())  # check if is a file
print(path.is_dir())  # check if is a directory
print(path.name)  # full name
print(path.stem)  # name with no extension
print(path.suffix)  # only the exetension
print(path.parent)  # parent folder
path = path.with_name("file.txt")
print(path)
print(path.absolute())  # show the absoulte path
