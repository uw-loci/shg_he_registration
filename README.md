Evaluation code for automatic registration of H&E brightfield image and SHG image of tissue sections. Paramters are tuned for the datasets.
1. Proposed method can be used by running CurveAlign.m in curvelets folder. 
   Detailed instruction of the graphical user interface is in the paper.
2. SIFT can be used by running main_registration.mlx in SIFT-matlab-V1.0 folder. 
   File path need to point to the corresponding path storing the dataset. (Input/HE_512 and SHG_512_not_adjusted)
   Comment out the segmentation part if testing the raw HE input.
3. PSO-SIFT can be used by running main_registration.mlx in PSO-SIFT-matlab-V1.0 folder. 
   File path need to point to the corresponding path storing the dataset. (Input/HE_512 and Input/SHG_512_not_adjusted)
   Comment out the segmentation part if testing the raw HE input.
4. Elastix can be used by running elastix_affine.py. 
   SimpleElastix and all dependencies need to be installed. https://simpleelastix.github.io/. 
   File path need to point to the corresponding path storing the dataset. (Input/HE_512 and Input/SHG_512_adjusted for raw HE input;    Input/ECM and Input/SHG_512_adjusted for ECM input)
   Need to change to use either ECM as source image or raw HE as source image in the code.
5. Results are shown in Supplementary figure 1107.docx
