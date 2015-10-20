#!/bin/bash
for t in $(seq 1 1000)
do
	y=$((t-1))
	x=`printf %03d $y`
	python /home/agupta80/astral_wqmc/src/induced_subtree.py \
	/home/agupta80/scratch/model.100.2000000.0.000001/01/truegenetree_$x\
	/home/agupta80/scratch/model.100.2000000.0.000001/01_sampled_76/gene_$t".tree"\
	/home/agupta80/scratch/model.100.2000000.0.000001/01/truegenetree_induced_$x".tree"
done
