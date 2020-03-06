import os
import numpy as np
#import pandas as pd
import glob
#from pathlib import Path
import errno
#from astropy.table import Table
#from astropy.io import ascii

print('this is the update script')

#Changing directory
chdirpath1 = "/fred/oz002/users/mmiles/timing"
os.chdir(chdirpath1)

cwd = os.getcwd()
print('searching for targets.dat in:',cwd)
targets = open("targets.dat")

for pulsar in targets:
    pulsar = pulsar.strip(' \n')
    print({pulsar})
    #Make a directory for the data under MATTIME
    mkdirpath1 = os.path.join(chdirpath1, pulsar)
    #This is just to get rid of the problem where it detects that the directory already exists
    
    try:
        os.mkdir(mkdirpath1)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
    #Change into the directory where all the data is
    timing = "/fred/oz005/timing/"

    #Move into the MEERTIME timing directory
    os.chdir(timing)
    print('In this directory',os.getcwd())
    pulsarpath = os.path.join(timing, pulsar)

    #Move into the pulsar directory with command below
    os.chdir(pulsarpath)
    print('In this directory', os.getcwd())

    #Create a for loop for the observations and roll through these
    for obs in os.listdir(pulsarpath):
        observationpath = os.path.join(pulsarpath,obs)
        #Move into the direcotry for the individual observation
        os.chdir(observationpath)
        print('In this directory', os.getcwd())

        #Move into the beamno directory
        beamno = os.listdir(observationpath)[0]
        beamnopath = os.path.join(observationpath, beamno)
        os.chdir(beamnopath)
        print('In this directory', os.getcwd())

        #Move into the frequency directory
        freq = os.listdir(beamnopath)[0]
        freqpath = os.path.join(beamnopath, freq)
        os.chdir(freqpath)
        print('In this directory', os.getcwd())

        #Set up file count system
        filecount = len(glob.glob1(freqpath, "*.ar"))
        print(f'there are {filecount} files in observation {obs} for pulsar {pulsar}')

        #Okay, now create the symbolic links
        print('creating soft links and directory')

        #Make a directory in MATTIME based on the information in the MEERTIME directory traced above
        mkdirpath2 = os.path.join(mkdirpath1, obs, beamno, freq)
        os.makedirs(mkdirpath2)
        
        #Make an if path to detect if there is already a .linked file present
        if glob.glob('*.linked'):
            print('already copied/linked %s archives for %s', filecount, obs)
        else:
            #Creating soft links to the MEERTIME directory from MATTIME
            for archive in os.listdir(freqpath):
                os.symlink(os.path.join(freqpath, archive), os.path.join(mkdirpath2, archive))
            checkfile = os.path.join(mkdirpath2, ".linked")
