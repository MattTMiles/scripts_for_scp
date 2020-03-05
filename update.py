import os
import numpy as np 
import pandas as pd
import glob
from pathlib import Path

print('this is the udpate script')

#Replace all paths with actual paths before this is finished.

#Changing directory
chdirpath1 = "/fred/oz002/.....MATTIME"
os.chdir(chdirpath1)

cwd = os.getcwd()
print('searching for targets.dat in:',cwd)

for pulsar in targets.dat:
    #Make a directory for the data under MATTIME
    mkdirpath1 = os.path.join(chdirpath1,"pulsar")
    os.mkdir(mkdirpath1)

    #Change into the directory where all the data is
    timing = "/fred/oz002/.....MEERTIME/timing/"
    
    #Move into the MEERTIME timing directory
    os.chdir(timing)
    #In MEERTIME timing directory
    for pulsar in os.chdir(timing):
        pulsarpath = os.path.join(timing, pulsar)
        
        #Move into the pulsar directory with command below
        os.chdir(pulsarpath)
        #In individual pulsar directory

        #observationpath = os.chdir(chdirpath3)

        ##input here a way to set the beamno? Required?##
        
        #Create a for loop for the observations and roll through these
        for obs in pulsarpath:
            observationpath = os.path.join(pulsarpath,obs)
            #Move into the direcotry for the individual observation
            os.chdir(observationpath)
            #In individual pulsar directory
            
            #Move into the beamno directory
            beamno = os.listdir(observationpath)
            beamnopath = os.path.join(observationpath, beamno)
            #Move into the directory for the beam number
            os.chdir(beamnopath)

            #Move into the frequency directory
            freq = os.listdir(beamnopath)
            freqpath = os.path.join(beamnopath, freq)
            #Move into the directory for the frequency
            os.chdir(freqpath)

            #Set up file count system
            filecount = len(glob.glob1(freqpath, "*.ar"))
            print('there are %s files in observation %s for pulsar %s', filecount, obs, pulsar)

            #Okay, now create the symbolic links
            print('creating soft links and directory')
            
            #Make a directory in MATTIME based on the information in the MEERTIME directory traced above
            mkdirpath2 = os.path.join(mkdirpath1, obs, beamno, freq)
            os.mkdir(mkdirpath2)

            #Make an if path to detect if there is already a .linked file present
            if glob.glob('*.linked'):
                print('already copied/linked %s archives for %s', filecount, obs)
            else:
                #Crating soft links to the MEERTIME directory from MATTIME
                for archive in os.listdir(freqpath):
                    os.symlink(os.path.join(freqpath, archive), mkdirpath2)
                #Adding a .linked file to identify if this process needs to be done
                Path(mkdirpath2/.linked).touch()
                

            







