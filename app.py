import os
source='D:/Whitehatjr/class115/project/main.txt'
dest='D:/Whitehatjr/class115/project/newfile.txt'
os.rename(source,dest)
print(f"File rename successfully to {dest}")
