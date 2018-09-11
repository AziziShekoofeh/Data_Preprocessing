"""
Read the data from the Main Folder
The data includes different categories and each category is indicated in the .csv file
The data should be reformat to put every image in a folder with the name of category             
Author: Shekoofeh Azizi @UBC
"""
import numpy as np
import os, errno
import csv
from os.path import isfile, join
from shutil import copyfile
import glob

class Data:

    def __init__(self, host_dir='/media/sf_SharedDrive/WasteData/',
                 raw_path='March2018WasteAuditRaWData',
                 final_path='EditedWasteAuditData'):

        self.raw_path = os.path.join(host_dir, raw_path)
        self.final_path = os.path.join(host_dir, final_path)


    @staticmethod
    def make_directory(directory):
        """ Check if the final path exist and if not create the directory, otherwise raise an error
        :return:
        """
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
        return

    def read_raw(self):
        """ Read the host folder, identify the number of sub-folders for sub-datasets
        # create the destination/final folder
        # open the host folder
        # find the sub-folders or sub-datasets
        # for each sub-folder:
        #   read the last or highest number csv
        #   read the label column and create a sub-folder for that label in the destination/final folder if not exist
        #   read the image name
        #   generate the origin and destination path and copy the image
        :return: list the name of sub-folders
        """
        dir_list = os.listdir(self.raw_path)

        for dir_idx in dir_list:
            item_count = 0
            sub_dir = os.path.join(self.raw_path, dir_idx)
            csv_list = glob.glob(sub_dir+'/*.csv')
            csv_file = csv_list[0]
            csv_data = self.read_csv(csv_file)

            for label, im_name in csv_data:
                dst_path = os.path.join(self.final_path, label)
                src_path = os.path.join(self.raw_path, dir_idx, im_name)
                self.make_directory(dst_path)
                dst_path = os.path.join(dst_path, im_name)
                copyfile(src_path, dst_path)
                print('image', im_name, 'copied from dataset', dir_idx)
                item_count += 1
            print('Total number of ', item_count, ' images copied from dataset', dir_idx)

        return

    def read_csv(self, csv_file):
        """ The function should open the given CSV file and
        :return:
        """
        with open(csv_file) as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            csv_data = [r for r in reader]
        return csv_data
