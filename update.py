import os
import numpy as np
#import pandas as pd
import glob
from pathlib import Path
import errno
from astropy.table import Table
from astropy.io import ascii

print('this is the update script')

#Changing directory
chdirpath1 = "/fred/oz002/users/mmiles/timing"
os.chdir(chdirpath1)

cwd = os.getcwd()
print('searching for targets.dat in:',cwd)
targets = open("targets.dat", newline="\n")

for pulsar in targets:
    #Make a directory for the data under MATTIME
    mkdirpath1 = os.path.join(chdirpath1, pulsar)
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
    #In MEERTIME timing directory
        for obs in os.listdir(pulsarpath):
            observationpath = os.path.join(pulsarpath,obs)
            #Move into the direcotry for the individual observation
            os.chdir(observationpath)
            print('In this directory', os.getcwd())
            #In individual pulsar directory

            #The curent bug below is that the beamno comes out as a list and it can't be put into the
            # the path line even when it I splat it, so I'll have to try a for loop fix which is a
            # really bad way to do it probably.

            #Move into the beamno directory
            beamno = os.listdir(observationpath)[1:-1]
            beamnopath = os.path.join(observationpath, beamno)
            #Move into the directory for the beam number
            os.chdir(beamnopath)
            print('In this directory', os.getcwd())

            #Move into the frequency directory
            freq = os.listdir(beamnopath)
            freqpath = os.path.join(beamnopath, str(freq))
            #Move into the directory for the frequency
            os.chdir(freqpath)
            print('In this directory', os.getcwd())

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
                Path('mkdirpath2/.linked').touch()
