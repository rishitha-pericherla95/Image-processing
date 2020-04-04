import sys
import os
from PIL import Image

#grab the first and second arguments
inputloc = sys.argv[1]
outputloc = sys.argv[2]

#check if it exists or else create
if os.path.exists(inputloc):
    print("Path Exists")
else:
    print("Enter valid input location")
if os.path.exists(outputloc):
    print("Path Exists")
else:
    os.makedirs("new")

#loop through the folder pokedex and convert into png
for f in os.listdir(inputloc):
   image = Image.open(inputloc +"/" +f)
   clean_name  = os.path.splitext(f)[0]
   image.save(outputloc + "/" +clean_name+".png",'PNG')
#save into new folder