Evaluation code (highlighted in bold) for automatic registration of H&E brightfield image and SHG image of tissue sections. We compared two SIFT-based methods [1-4] and an intensity-based method [5-6] to our proposed method. 
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




