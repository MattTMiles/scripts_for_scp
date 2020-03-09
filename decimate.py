import os

def decimate(pulsar, obs):
    MainDir = "/fred/oz002/users/mmiles/timing/"

    os.chdir(MainDir)

    pulsar = input("Input the pulsar to be investigated:")
    obs = input("Input the observation to be investigated:")

    #Change to requested pulsar directory
    pulsar_dir = os.path.join(MainDir,pulsar)
    os.chdir(pulsar_dir)

    #Change to requested observation directory
    obs_dir = os.path.join(pulsar_dir, obs)

    #Move through beam number directory
    beamno = os.listdir(obs_dir)[0]
    beamno_dir = os.path.join(obs_dir, beamno)
    os.chdir(beamno_dir)

    #Move through frequency directory
    freq = os.listdir(beamno_dir)[0]
    freq_dir = os.path.join(beamno_dir, freq)
    os.chdir(freq_dir)

    #This uses paz on each subintergration in the directory, and rewrites them with the extension .r

    for files in os.listdir(os.getcwd()):
        if files.endswith(".r"):
            os.system("pam -p -f 32 -e pf32"+files)
            
            #Removes any files left with the .r extension
            os.system("rm"+files)
        
        #Below needs to be "psradd -o" connected to pathname.pf32 then 2*.pf32
        #2.*pf32 means select all that start with 2 and ends with the extension
        if files.startswith("2") and files.endswith("pf32"):
            os.system("psradd -o ")
