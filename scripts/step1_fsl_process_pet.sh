#!/bin/bash
echo "This is a processing about skull remove and linear registrition only 2 step"

mni152="/usr/local/fsl/data/standard/MNI152_T1_1mm_brain"
brain="_brain"
registration="_registration"
mat=".mat"
inial="/media/ADNI1_baseline_AD/" # Path of source data
filelist=`ls /media/ADNI1_baseline_Processed_AD/` # Path of save to 

for dir in ${filelist};do
	dir_=${inial}${dir}
	if [ -d ${dir_} ];then
		echo ${dir_}
		cd ${dir_}
		name=$(find pet.nii)
		bet ${name%.*} ${name%.*}${brain} -f 0.65 -g 0

		flirt -in ${name%.*}${brain} -ref ${mni152} -out ${name%.*}${registration} -omat ${name%.*}${registration}${mat} \
		      -bins 256 -cost corratio -searchrx -90 90 -searchry -90 90 -searchrz -90 90 -dof 12 -interp trilinear

	fi
done
