#!/bin/sh

#$ -N nabrs0.2

# Request here the number of cores in multiple fo 36, e.g. 36, 72,108
#$ -pe mpi-16 16 
##$ -pe smp 36

#$ -V
#$ -cwd

python ./na_br.py


