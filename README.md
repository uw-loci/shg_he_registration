# Intensity-based registration of bright-field and second-harmonic generation images of histopathology tissue sections
Evaluation code and demo code for automatic registration of H&E brightfield image and SHG image of tissue sections.  
## Demo
1. [Proposed method](https://www.osapublishing.org/boe/abstract.cfm?uri=boe-11-1-160) is integrated in CurveAlign program, execute **CurveAlign.m in _curvealign_** folder.
2. Running the program without a complete installation of MATLAB is possible, a detailed description of the installation can be found at
   * https://eliceirilab.org/software/curvealign/
   * https://eliceirilab.org/sites/default/files/2017-08/Manual%20%20for%20%20CurveAlign%20V4.0%20Beta%20August%202017.pdf
3. Quick start guide for running in MATLAB
   * Open MATLAB
   * Navigate to **_curvealign_** folder and run **CurveAlign.m**   
   * Click _BD creation_ in the main panel     
   * Click _Get HE Files_ in the pop-up panel and select the H&E images    
   * Click _Get SHG Folder_ in the pop-up panel and seelect the folder containing all the SHG images, each SHG image should have the same file name as the corresponding H&E image.  
   * Select the registration method.  
      [Auto based on RGB intensity] uses a k-means clustering to segment the H&E images (slower)        
      [Auto based on HSV intensity] uses Otsu's method and simple hue channel thresholding to segment the H&E images (faster)        
   * Check _Reg_ box at the bottom of the pop-out window   
   * Click _OK_ and wait, messages are logged in MATLAB command window
   

## Evaluation
We compared two SIFT-based methods [1-4] and an intensity-based method [5-6] to our proposed method[7]. 
1. Proposed method can be used by running **CurveAlign.m in _curvealign_** folder.  
   Detailed instruction of the graphical user interface is in the paper.
2. SIFT can be used by running **main_registration.mlx in _SIFT-matlab-V1.0_** folder.  
   File path need to point to the corresponding path storing the dataset. (**_Input/HE_512_** and **_Input/SHG_512_not_adjusted_**)
   Comment out the segmentation part if testing the raw HE input.
3. PSO-SIFT can be used by running **main_registration.mlx in _PSO-SIFT-matlab-V1.0_** folder.  
   File path need to point to the corresponding path storing the dataset. (**_Input/HE_512_** and **_Input/SHG_512_not_adjusted_**)
   Comment out the segmentation part if testing the raw HE input.
4. Elastix can be used by running **elastix_affine.py.**  
   SimpleElastix and all dependencies need to be installed. https://simpleelastix.github.io/. 
   File path need to point to the corresponding path storing the dataset. (**_Input/HE_512_** and **_Input/SHG_512_adjusted_** for raw HE input;    **_Input/ECM_** and **_Input/SHG_512_adjusted_** for ECM input)
   Need to change to use either ECM as source image or raw HE as source image in the code.
5. Results are shown in **Supplementary figure 1107.docx** and **_comparison_** folder  

**Please contact us for any questions**

**References:**  
[1] D. G. Lowe, “Distinctive Image Features from Scale-Invariant Keypoints,” Int. J. Comput. Vis. 60, 91–110 (2004).  
[2] M. A. Fischler and R. C. Bolles, “Random Sample Consensus: A Paradigm for Model Fitting with Applications to Image Analysis and Automated Cartography,” Commun. ACM 24, 381–395 (1981).  
[3] G. Shi, X. Xu, and Y. Dai, “SIFT Feature Point Matching Based on Improved RANSAC Algorithm,” in 2013 5th International Conference on Intelligent Human-Machine Systems and Cybernetics, vol. 1 (2013), pp. 474–477.  
[4] W. Ma, Z. Wen, Y. Wu, L. Jiao, M. Gong, Y. Zheng, and L. Liu, “Remote Sensing Image Registration With Modified
SIFT and Enhanced Feature Matching,” IEEE Geosci. Remote. Sens. Lett. 14, 3–7 (2017).  
[5] S. Klein, M. Staring, K. Murphy, M. Viergever, and J. Pluim, “elastix: A Toolbox for Intensity-Based Medical Image Registration,” IEEE Transactions on Med. Imaging 29, 196–205 (2010).  
[6] K. Marstal, F. Berendsen, M. Staring, and S. Klein, “SimpleElastix: A User-Friendly, Multi-lingual Library for
Medical Image Registration,” in 2016 IEEE Conference on Computer Vision and Pattern Recognition Workshops
(CVPRW), (2016), pp. 574–582. ISSN: 2160-7516  
[7] Adib Keikhosravi, Bin Li, Yuming Liu, and Kevin W. Eliceiri. "Intensity-based registration of bright-field and second-harmonic generation images of histopathology tissue sections." Biomedical Optics Express 11, no. 1 (2020): 160-173.

## Citations
```
@article{keikhosravi_intensity-based_2020,
	title = {Intensity-based registration of bright-field and second-harmonic generation images of histopathology tissue sections},
	volume = {11},
	copyright = {\&\#169; 2019 Optical Society of America},
	issn = {2156-7085},
	url = {https://www.osapublishing.org/boe/abstract.cfm?uri=boe-11-1-160},
	doi = {10.1364/BOE.11.000160},
	number = {1},
	journal = {Biomedical Optics Express},
	author = {Keikhosravi, Adib and Li, Bin and Liu, Yuming and Eliceiri, Kevin W.},
	month = jan,
	year = {2020},
	note = {Publisher: Optical Society of America},
	pages = {160--173}
}
```


