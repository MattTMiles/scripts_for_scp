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

    for files in os.listdir(freq_dir):
        if files.endswith(".r"):
            #p scrunches and f scrunches into 32 bins, then changes the extension to pf32
            os.system("pam -p -f 32 -e pf32"+files)
            
            #Removes any files left with the .r extension
            os.system("rm"+files)
        
        if files.startswith("2") and files.endswith(".pf32"):
            
            #Below joins all 8 second periods into a single file
            os.system("psradd -o"+freq_dir+".pf32"+files)

            #Removes the files that started with 2 and end with .pf32
            os.system("rm"+files)

        #Creates a version that is integrated in frequency and given the extension F
        os.system("pam -F"+freq_dir+".pf32 -e F")

        #Creates a version that is integrated in time and given the extension T
        os.system("pam -T"+freq_dir+".pf32 -e T")

        checkfile = freq_dir + "/" + "obs.decimated"
        with open(checkfile,"w") as x:
            x.write("this process has already been done")
