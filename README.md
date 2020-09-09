## Using python-fu to batch process images in GIMP.

Repo to document batch processing in Gimp using python-fu scripting. Runs Gimp non-interactively (no GUI).

### Steps

#### 0. Acquiring images
You can batch download Wikimedia Commons images using the very nice tool [Imker](https://commons.wikimedia.org/wiki/Commons:Imker_(batch_download)). Download the zip file, unzip, and (for MacOS), launch the appropriate jar from the terminal. 

For GUI - `java -jar imker-gui.jar`

Best feature is downloading all images at original resolution from a Wikimedia Category. Example: Set category to Voynich_manuscript to download all images from https://commons.wikimedia.org/wiki/Category:Voynich_manuscript 

#### 1. Setting up the python script

Download the batchwrapper.py to the folder containing the images. The script takes two arguments as input - foldername & file extension.

Modify the section below the comment << now the actual work >>. Fill in with python-fu processing steps. In Gimp, go to Filters -> Python-fu -> console -> Browse to get a reference library of all the python-fu commands available to work with. Save file.

Hat-tip to user MCO at https://stackoverflow.com/questions/42925482/gimp-batch-editing-script-fu-python-fu/42933365 for the script. I just converted it from a Gimp plugin to a standard python script. See note below.

##### Note: Default way of running a python-fu script is to register it as a plugin in Gimp and then run it. This caused a lot of headache for me as the plugin I tried to create kept crashing Gimp.

#### 2. Running the python script.

Open terminal, navigate to the folder containing images & the python script, paste the following command and run it.


`/Applications/GIMP-2.10.app/Contents/MacOS/gimp -idf  --batch-interpreter python-fu-eval -b "import sys;sys.path=['.']+sys.path;import batchwrapper;batchwrapper.gimpbatchproc('/Users/username/Downloads/images/rawpics','*.jpg')" -b "pdb.gimp_quit(1)"`

Very elegant command line solution from user Xenoid at https://stackoverflow.com/questions/44430081/how-to-run-python-scripts-using-gimpfu-from-command-line . Answer also contains another version of the batch script.

If everything works well, a new folder named "output" should be created in the folder containing the images and should be populated with the processed images. File extension might be incorrect but you can change this to the correct extension by bulk rename in MacOS. Files should be in the correct format though.

