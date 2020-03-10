import os
from clean import clean
from decimate import decimate

""" The purpose of this script is to activate the clean.py script and the decimate.py
scripts for all pulsars that have been updated as per the update.py script (therefor
the targets.dat file). """

#Need for loops to specify all observations in all pulsars while moving through the directories.

#Probably best to separate this into clean all then decimate all rather than have them going
# straight after each other.

#This runs the update.py script so everthing is updated every time it's run.
os.system("python update.py")

#This specifies the main directory so the pulsar and obs information can be pulled out.
mainDir = "/fred/oz002/users/mmiles/timing"

#Loop through the pulsars dropped in the $MATTIME directory following the update script run
for pulsar in os.listdir(mainDir):
    #Loop through each obs in each pulsar
    for obs in os.listdir(os.path.join(mainDir,pulsar)):
        #Cleans the pulsar data following the loops
        clean(pulsar, obs)

#This does the same thing as above but decimates the cleaned pulsar data.
for pulsar in os.listdir(mainDir):
    for obs in os.listdir(os.path.join(mainDir, pulsar)):
        decimate(pulsar, obs)
