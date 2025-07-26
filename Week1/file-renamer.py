import os

folder = "C:/Users/Anass/Desktop/test"
for count, filename in enumerate(os.listdir(folder)):
    dst = f"file_{count}.txt"
    src = f"{folder}/{filename}"
    dst = f"{folder}/{dst}"
    os.rename(src, dst)
