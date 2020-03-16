#This code creates a batch file for the supercomputer to run through the pulsars 
#when is best for it to do so


#!/bin/bash
#SBATCH --cpus-per-task=1
#SBATCH --time=12:00:00
#SBATCH --job-name=single.pulses
#SBATCH --mem=20g
#SBATCH --tmp=20g

#This should run allobs.py as a batch file
#cd /fred/oz002/users/mmiles/timing/
touch ${1}".job"
#csh combiner.csh $1 $2 $3
if $1 == J*
then
        python allobs.py $1

rm -f ${1}".job"
echo done