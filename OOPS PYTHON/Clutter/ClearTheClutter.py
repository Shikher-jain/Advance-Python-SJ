import os
import sys

# print(os.path)
# print("sys.executable",sys.executable)
# print("os.getcwd     ",os.getcwd())
# files=os.listdir("Clutter")
files=os.listdir("c:/C programs/Shikher-jain/.vscode/Shikher-jain/.vscode/OOPS PYTHON/Clutter")
i=1
for file in files:
    # if file.endswith(".png"):
    if not file.endswith(".png"):
        print(file)
        # os.rename(f"C:/C programs/Shikher-jain/.vscode/Shikher-jain/.vscode/OOPS PYTHON/Clutter/{file}",f"C:/C programs/Shikher-jain/.vscode/Shikher-jain/.vscode/OOPS PYTHON/Clutter/{i}")
        os.rename(f"C:/C programs/Shikher-jain/.vscode/Shikher-jain/.vscode/OOPS PYTHON/Clutter/{i}",f"C:/C programs/Shikher-jain/.vscode/Shikher-jain/.vscode/OOPS PYTHON/Clutter/TestPicture {i}.png")
        i=i+1
# os.rename("C:/C programs/Shikher-jain/.vscode/Shikher-jain/.vscode/OOPS PYTHON/Clutter/pngegg(0).png","C:/C programs/Shikher-jain/.vscode/Shikher-jain/.vscode/OOPS PYTHON/Clutter/pngegg (0).png")
# print(file)

 