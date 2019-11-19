from pathlib import Path
from zipfile import ZipFile

# zip = ZipFile("files.zip", "w")  # create (w) the file in the current folder

# now i want to take all the file in the package_example dir
# and put in the zip file
# with ZipFile("files.zip", "w") as zip:
#     for path in Path("package_example").rglob("*.*"):
#         zip.write(path)

with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("package_example/creating_modules.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")
