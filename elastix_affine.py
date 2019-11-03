import SimpleITK as sitk
import os
import re

shg_file = [f for f in os.listdir('/home/binli/Projects/registration/data/SHG_512')]
he_file = [f for f in os.listdir('/home/binli/Projects/registration/data/HE_gray')]
ecm_file = [f for f in os.listdir('/home/binli/Projects/registration/data/ECM')]

shg_path = '/home/binli/Projects/registration/data/SHG_512'
he_path = '/home/binli/Projects/registration/data/HE_gray'
ecm_path = '/home/binli/Projects/registration/data/ECM'
save_path = 'registered_affine/ecm'

for i in range(1, len(shg_file)):
	shg = os.path.join(shg_path, shg_file[i])
	he = os.path.join(he_path, he_file[i])
	ecm = os.path.join(ecm_path, ecm_file[i])
	save = os.path.join(save_path, shg_file[i])
	elastixImageFilter = sitk.ElastixImageFilter()
	elastixImageFilter.SetFixedImage(sitk.ReadImage(shg))
	elastixImageFilter.SetMovingImage(sitk.ReadImage(ecm))
	elastixImageFilter.SetParameterMap(sitk.GetDefaultParameterMap("affine"))
	try:
		elastixImageFilter.Execute()
	except:	
		sitk.WriteImage(sitk.ReadImage(he), save, True)
		continue
	transformixImageFilter = sitk.TransformixImageFilter()
	transformixImageFilter.SetTransformParameterMap(elastixImageFilter.GetTransformParameterMap())
	transformixImageFilter.SetMovingImage(sitk.ReadImage(he))
	transformixImageFilter.Execute()
	
	sitk.WriteImage(transformixImageFilter.GetResultImage(), save, True)