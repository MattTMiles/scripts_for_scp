""" This code will go into the files that have been cleaned and decimated and make 
relevant plots to them"""

#c-shell sudo code for reference is as follows:
    #pav -Yd filename.F -g filename.F.png/png
    #pav -Df filename.T -g filename.D.png/png
    #pav -Gd filename.T -g filename.G.png/png

import os

#Define a main directory for reference ($MATTIME)
mainDir = "/fred/oz002/users/mmiles/timing"

#Retrieve the pulsar name
pulsar = input("Input the pulsar you want to make plots for:")

#Change into the pulsar's directory
os.chdir(os.path.join(mainDir, pulsar))

#Run through the observations and create png files where relevant
for obs in os.listdir(os.path.join(mainDir, pulsar)):
    if obs.endswith(".F"):
        os.system("pav -Yd "+obs+" -g "+obs+".png/png")

    if obs.endswith(".T"):
        os.system("pav -Df "+obs+" -g "+obs+".D.png/png")
        
        os.system("pav -Gd "+obs+" -g "+obs+".G.png/png")

