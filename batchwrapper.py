#!/usr/bin/env python

from gimpfu import *
import glob
import os
import argparse

pdb = gimp.pdb

def gimpbatchproc(loadfolder, fileextension):

# correct loadfolder: add (back-)slash if needed
	if not loadfolder.endswith(("/", "\\")):
		if os.name == "nt": # we need backslashes on windows, but slashes on linux/mac
			loadfolder = loadfolder + "\\"
		else:
			loadfolder = loadfolder + "/"

# prepare the file pattern
	filepattern = loadfolder + fileextension
	filelist = glob.glob(filepattern)
	filelist.sort()
    # gimp.message(" ".join(filelist) # for debugging

# loop once for every file
	for filepath in filelist:
    # load image
		if filepath.endswith((".jpeg,", ".jpg")):
			image = pdb.file_jpeg_load(filepath, filepath)
		elif filepath.endswith(".png"):
			image = pdb.file_png_load(filepath, filepath)
		layer = image.active_layer
    # prepare filename
		if os.name == "nt": # we need backslashes on windows, but slashes on linux/mac
			outputfolder = "%soutput\\" % loadfolder # add the name of a new folder
		else:
			outputfolder = "%soutput//" % loadfolder # add the name of a new folder
            
		gimp.message(outputfolder)
        
		if not os.path.exists(outputfolder):
			os.makedirs(outputfolder) # create the new folder if it doesn't exist yet
            
		filename = os.path.basename(filepath) # remove the path and only keep the actual filename with extension
		outputpath = outputfolder + filename
        # now the actual work
        
        # fuzzy select on the 1st pixel, invert select, copy selection, create new image from selection
        # save as png
		pdb.gimp_image_select_contiguous_color(image, 0, layer, 0, 0)
		pdb.gimp_selection_invert(image)
		pdb.gimp_selection_feather(image, 5)
		pdb.gimp_edit_copy(image.layers[0])
		new_img = pdb.gimp_edit_paste_as_new_image()
		layern = pdb.gimp_image_merge_visible_layers(new_img, CLIP_TO_IMAGE)
		pdb.file_png_save2(image, layern, outputpath, outputpath,1,9,0,0,0,0,0,0,0)
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--path', metavar='path', required=True,
                        help='the path to workspace')
	parser.add_argument('--files', required=True,
                        help='filetype')
 	args = parser.parse_args()
	gimpbatchproc(loadfolder=args.path, fileextension=args.files)
