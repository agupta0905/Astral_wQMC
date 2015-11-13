#!/bin/bash
mkdir /home/agupta80/scratch/avian_dataset/avian-2X-1000-500/R1-binning/genes
for l in $(seq 1 100)
do
	mkdir "/home/agupta80/scratch/avian_dataset/avian-2X-1000-500/R1-binning/genes/"$l
	cp "/home/agupta80/scratch/avian_dataset/avian-2X-1000-500/R1/"$l"/raxmlboot.gtrgamma/RAxML_bipartitions.final.f200" \
	"/home/agupta80/scratch/avian_dataset/avian-2X-1000-500/R1-binning/genes/"$l"/"
	echo $l
done