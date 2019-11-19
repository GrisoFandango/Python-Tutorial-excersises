from pathlib import Path

path = Path("python_standard_library_ex")
# path.exists()
# path.mkdir() #to create a directory
# path.rmdir() # to remove it
# path.rename("package_example2") # to rename it

# Another method
path.iterdir()  # get list of files and directories in this path
print(path.iterdir())  # give us a generator object that can be iterated
for p in path.iterdir():
    print(p)

# we cannot search with a pattern with this method
# do not research recursively
# give us a list with WindowsPath
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

py_files = [p for p in path.glob("*.py")]
print("not recur", py_files)
# to do recusively, so it shows all the files in sub dir as well
py_files = [p for p in path.rglob("*.py")]
print("recur", py_files)
