import os
import sys
# print(os.path)
print("sys.executable",sys.executable)
print("os.getcwd     ",os.getcwd())
# os.chdir("/users")
print("os.getcwd     ",os.getcwd())
if(not os.path.exists("os MOdule")):
    os.mkdir("os MOdule")

# for i in range(1,101):
#     # os.mkdir(f"os MOdule/dayAS {i}")
    # os.rename(f"os MOdule/Remane {i}",f"os MOdule/Remane {i}",)
# folders=os.listdir("os MOdule")
# print(folders)
# for folder in folders:
#     print(folder)
#     print(os.listdir(f"os MOdule/{folder}"))
# os.rmdir("os MOdule") #only dlt when it is empty