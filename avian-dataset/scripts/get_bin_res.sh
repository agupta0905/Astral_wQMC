#!/bin/bash
for m in 0.5 1 2
do
	for t in 10 20 30 40
	do
		for l in $(seq 1 100)
		do
			python /home/agupta80/astral_wqmc/avian-dataset/src/get_bin.py "~/scratch/avian_dataset/avian-"$m"X-1000-500" 1 $l 100 $t
			echo $m $t $l "Done"
		done
	done
done