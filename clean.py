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

""" This is the same code as above just written as a function
 so that arguments can be passed into it """

def clean(PSRID,OBS):
    MainDir = "/fred/oz002/users/mmiles/timing/"

    os.chdir(MainDir)

    PSRID = input("Input the pulsar to be investigated:")
    OBSID = input("Input the observation to be investigated:")

    #Change to requested pulsar directory
    PSRID_dir = os.path.join(MainDir,PSRID)
    os.chdir(PSRID_dir)

    #Change to requested observation directory
    OBSID_dir = os.path.join(PSRID_dir, OBSID)

    #Move through beam number directory
    beamno = os.listdir(OBSID_dir)[0]
    beamno_dir = os.path.join(OBSID_dir, beamno)
    os.chdir(beamno_dir)

    #Move through frequency directory
    freq = os.listdir(beamno_dir)[0]
    freq_dir = os.path.join(beamno_dir, freq)
    os.chdir(freq_dir)

    #This uses paz on each subintergration in the directory, and rewrites them with the extension .r

    for files in os.listdir(os.getcwd()):
        if files.ednswith(".ar"):
            os.system("paz -r -e r "+files)
    #Leaves an artefact in the file showing that the observation has been cleaned
    checkfile = freq_dir + "/" + "obs.cleaned"
    with open(checkfile,"w") as x:
        x.write("this process has already been done")






