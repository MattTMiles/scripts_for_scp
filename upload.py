#Script to upload the files in  question to the webserver

import os

pulsar = input("Put in the name of the pulsar to upload:")

#This should secure copy the file directly on to the server - unsure if I can automatically give it my password yet
os.system("scp -r mmiles@ozstar.swin.edu.au:'/fred/oz002/users/mmiles/timing/"+pulsar+"/*.{png}' mmiles@asv1.cc.swin.edu.au:/home/mmiles/public_html/"+pulsar)
