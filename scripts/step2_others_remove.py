import os
import numpy as np
import nibabel as nib
import scipy.io as sio
import cv2

#template mask
path_mask = "./script"
mask = os.path.join(path_mask, 'mask.nii.gz')
img_mask = nib.load(mask).get_fdata()


# MRI data preprocess
path = "./media/ADNI1_baseline_Processed_AD" 
files = os.listdir(path)

for fi in files:
    path_son = os.path.join(path, fi)
    fmri = os.path.join(path_son, 'mri_registration2.nii.gz')
    img_mri_add = nib.load(fmri)
    affine = img_mri_add.affine.copy()
    hdr = img_mri_add.header.copy()
    img_mri = nib.load(fmri).get_fdata() 
    img_mri_r =  img_mri * img_mask
    nii_mri = nib.Nifti1Image(img_mri_r, affine, hdr)
    save_mri = os.path.join(path_son, 'mri_registration_better.nii.gz')
    nib.save(nii_mri, save_mri)
print('MRI OK')


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
