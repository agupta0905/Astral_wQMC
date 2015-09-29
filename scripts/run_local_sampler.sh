#!/bin/bash
#PBS -l walltime=02:00:00
#PBS -l nodes=1:ppn=1
#PBS -N sampling_taxa
#PBS -q tallis
#PBS -l naccesspolicy=shared
for t in $(seq 1 50)
do
	for k in 10 25 50
	do
		python /Users/agupta/Documents/MS_Thesis/astral_wqmc/src/sample_taxa.py /Users/agupta/Documents/MS_Thesis/astral_wqmc/data/model.100.2000000.0.000001 $t $k 101
	done
done  
