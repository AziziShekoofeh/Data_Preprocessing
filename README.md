# Data_Preprocessing

## Goal: Generate a new dataset based on the labels

**-** Description: Codes for processing of data folders and sort them based on the labels. 

**-** Assumption and data structure: The assumption is that we have a parent/root folder and a few subfolder and each subfolder includes a .csv file which contains the name of the files and labesl, respectively. Like:

- Main/Root Folder: [host_dir + raw_path]

     **-** Subfolder 1: [includes .csv and images]
  
     **-** Subfolder 2: [includes .csv and images]

**-** Output: The generated label-based new dataset directory

- Proccesed Dataset: [host_dir + final_path]

     **-** Subfolder 1: [has the name of label 1 and includes images with label 1]
  
     **-** Subfolder 2: [has the name of label 2 and includes images with label 2]




credits: Shekoofeh Azizi
