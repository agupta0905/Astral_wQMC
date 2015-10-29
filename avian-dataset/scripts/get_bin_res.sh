#!/bin/bash
for t in 10 20 30 40
do
	for l in $(seq 1 100)
	do
		python /home/agupta80/astral_wqmc/avian-dataset/src/get_bin.py /home/agupta80/scratch/avian_dataset/avian-0.5X-1000-500 1 $l 100 $t
		echo $t $l "Done"
	done
done