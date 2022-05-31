#!/bin/bash
echo "This is a processing about skull remove and linear registrition only 2 steps"

mni152="/usr/local/fsl/data/standard/MNI152_T1_1mm"
mni152_brain="/usr/local/fsl/data/standard/MNI152_T1_1mm_brain"
brain="_brain"
registration="_registration"
registration2="_registration2"
mat=".mat"
inial="/media/ADNI1_baseline_AD/" # Path of source data
filelist=`ls /media/ADNI1_baseline_Processed_AD/` # Path of save to 

for dir in ${filelist};do
	dir_=${inial}${dir}
	if [ -d ${dir_} ];then
		echo ${dir_}
		cd ${dir_}
		name=$(find mri.nii)
		echo ${name%.*}

		bet ${name%.*} ${name%.*}${brain} -B -f 0.2 -g 0

		flirt -in ${name%.*}${brain} -ref ${mni152_brain} -out ${name%.*}${registration} -omat ${name%.*}${registration}${mat} \
		      -bins 256 -cost corratio -searchrx -90 90 -searchry -90 90 -searchrz -90 90 -dof 12 -interp trilinear
		# why twice flirt? once is ok, I think the results of one-time process have a little slant.
		flirt -in ${name%.*}${registration} -ref ${mni152_brain} -out ${name%.*}${registration2} -omat ${name%.*}${registration2}${mat} \
      		      -bins 256 -cost corratio -searchrx -90 90 -searchry -90 90 -searchrz -90 90 -dof 12 -interp trilinear


	fi
done
