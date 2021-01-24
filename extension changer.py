import os

dir = input(("Paste the directory you want to work with : "))
chg_ext = input(("Enter the extension to be changed (Eg : .txt) : "))
rep_ext = input(("Enter the extension to be replaced (Eg : .pdf) : "))
print()
print()
print()

os.chdir(dir)

for i in os.listdir():
    # name is the file name , ext is the extension type
    name, ext = os.path.splitext(i)
    if ext == chg_ext:
        new_name = f"{name}{rep_ext}"
        os.rename(i, new_name)
        print(
            f"({name[0:20]}...{chg_ext}) has been changed to ({name[0:20]}...{rep_ext})")
print()
print()
print()
print("renaming process has finished !")
