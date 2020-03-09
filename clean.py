import os
import glob

#Let a user input a pulsar and observation to do this script indivdually

print("This script will clean the observation data of the pulsars")

#Change the directory into the one holding the pulsar data
MainDir = "/fred/oz002/users/mmiles/timing/"

os.chdir(MainDir)

targets = os.listdir(MainDir)
#Roll through each observation of each pulsar

for pulsar in targets:
    pulsardir = os.path.join(MainDir, pulsar)
    #Move into the specific pulsar directory
    os.chdir(pulsardir)

    for obs in os.listdir(pulsardir):
        obsdir = os.path.join(pulsardir, obs)
        #Move into the specific observation directory
        os.chdir(obsdir)
        
        #Move into the beam number
        curdir1 = os.getcwd()
        contents1 = os.listdir(curdir1)[0]
        os.chdir(os.path.join(curdir1,contents1))

        #Move into the frequency
        curdir2 = os.getcwd()
        contents2 = os.listdir(curdir2)[0]
        os.chdir(os.path.join(curdir2,contents2))

        print("I am in:", os.getcwd())

        for files in os.listdir(os.getcwd()):
            if files.endswith(".ar"):
                #This command will call paz on the observation
                os.system("paz -r -e r "+files)