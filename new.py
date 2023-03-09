import os
import sys
import shutil

folderpath = sys.argv[1]
filename = sys.argv[2] + ".tex"

if not os.path.exists(folderpath):
    os.makedirs(folderpath)

if not os.path.exists(filename):
    shutil.copy("template.tex", os.path.join(folderpath, filename))
