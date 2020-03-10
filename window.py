""" This code will go into the files that have been cleaned and decimated and make 
relevant plots to them"""

#c-shell sudo code for reference is as follows:
    #pav -Yd filename.F -g filename.F.png/png
    #pav -Df filename.T -g filename.D.png/png
    #pav -Gd filename.T -g filename.G.png/png

mainDir = "/fred/oz002/users/mmiles/timing"

pulsar = input("Input the pulsar you want to make plots for:")

for obs in os.listdir(os.path.join(mainDir, pulsar)):
    if obs.endswith(".F"):
        os.system("pav -Yd "+obs+" -g "+obs+".png/png")