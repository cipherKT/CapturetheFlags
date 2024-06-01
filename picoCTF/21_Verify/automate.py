import os

# print(os.listdir())
os.chdir("/home/r00t3d/Desktop/CapturetheFlags/picoCTF/21_Verify/home/ctf-player/drop-in/files")
all_files = os.listdir()

print(all_files)
os.chdir("/home/r00t3d/Desktop/CapturetheFlags/picoCTF/21_Verify/home/ctf-player/drop-in")
for f in all_files:
    os.system(f"./decrypt.sh files/{f}")