# MRI-and-PET-data-from-ADNI
Pre-processed MRI and PET images from ADNI-1/ADNI-2(https://adni.loni.usc.edu/)

## Advanced Search (beta)
<p align="center">
  <img src="https://github.com/xiaoxingxingkz/MRI-and-PET-data-from-ADNI/blob/main/img/Fig1.png" width="1000">
</p>

## Description of Downloaded MRI
```python
if exist("MPR; GradWarp; B1 Correction; N3"):
  select
elif exist("MPR-R; GradWarp; B1 Correction; N3"):
  select
elif exist("MPR; GradWarp; N3"):
  select
elif exist("MPR-R; GradWarp; N3"):
  select
 elif exist("MPR; ; N3"):
  select
```
For the subjects with format of "MPR; ; N3" and "MPR-R; GradWarp; N3", we don not impute additional preprocessing steps such as "GradWarp" or "B1 Correction"

## Preprocessing of Downloaded MRI
Above preprocessing steps have already be done, we focus on
(a) BET algorithm is used for brain extraction. 
(b) The MRI images are aligned to Montreal Neurological Institute T1 standard template space (MNI152_T1_1mm) with the FLIRT linear registration algorithm.
(c) Remove the voxels of zero values in the periphery of brain.
(d) Downsample the images to the size of 76×94×76.
