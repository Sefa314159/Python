import os
from glob import glob

extensions = ['txt','pdf','mp4']
root_dir = "C:/Users/Sefa3/Desktop"

for extension in extensions:
    with open("{}_file.txt".format(extension), "w", encoding = "utf-8") as file: 
        for filename in glob(root_dir + "/*.{}".format(extension)):
            file.write("{}\n".format(filename))
