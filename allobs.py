"""
This is just information on how to tackle the plots - not to do with the code:

# -g png at the end of the plot to save a png
#-g f.png/png will create a png file called f.png
#-g \? will give you all the different plot types that are supported

#-Yd means dedisperse

#-DF filename.T -g filename.D.png/png will givethe shape of the profile 
#-Gd will give the greyscale version

#asv1.cc.swin.edu.au is the website
"""
import os
from clean import clean
from decimate import decimate
import sys


print("pulsar is:", str(sys.argv[1]))
#This script will activate clean and decimate on all observations for a single pulsar.
raise a 
mainDir = "/fred/oz002/users/mmiles/timing"

#Specify which pulsar you want to investigate
pulsar = input("Input the pulsar that you want to analyse: ")
#First pass script: unsure if this will work

#Call the clean.py function on the pulsar and all of its observations
for obs in os.listdir(os.path.join(mainDir, pulsar)):
    clean(pulsar, obs)

#Call the decimate.py function on the cleaned pulsar and all of its observations
for obs in os.listdir(os.path.join(mainDir, pulsar)):
    decimate(pulsar, obs)

