import os
import numpy as np
import nibabel as nib
import scipy.io as sio
import cv2

#template mask
path_mask = "./script"
mask = os.path.join(path_mask, 'mask.nii.gz')
img_mask = nib.load(mask).get_fdata()

# PET data preprocess
path = "./media/ADNI1_baseline_Processed_AD" 
files = os.listdir(path)

for fi in files:
    path_son = os.path.join(path, fi)
    fpet = os.path.join(path_son, 'pet_registration.nii.gz')
    img_pet_add = nib.load(fpet)
    affine_ = img_pet_add.affine.copy()
    hdr_ = img_pet_add.header.copy()
    img_pet = nib.load(fpet).get_fdata()
    img_pet_r =  img_pet * img_mask
    nii_pet = nib.Nifti1Image(img_pet_r, affine_, hdr_) #np.eye(4)
    save_pet = os.path.join(path_son, 'pet_registration_better.nii.gz')
    nib.save(nii_pet, save_pet)        
print('PET OK')
