#This code runs through all the pulsars and creates batch files for them acting on the
# previously created singleslurm script

#!/bin/csh

# megaslurm2.csh slurmname.csh directory start end gulpsize

set slurm = $1
set dirname = $2
#set start = $3
#set theend = $4
#set ngulp = $5
set base = $PWD

#set test = $start
#set final = `echo $start $ngulp|awk '{ print $1+$2}'`

#while ( $test < $theend )
#  sbatch $slurm $dirname $test $final
#  set test = `echo $test $ngulp | awk '{ print $1+$2}'`
#  set final = `echo $test $ngulp| awk '{ print $1+$2}'`

#end
foreach pulsar (`ls -1 $2`)
    sbatch $slurm $pulsar
end