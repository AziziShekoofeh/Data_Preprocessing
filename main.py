"""

The data includes different categories and each category is indicated in the .csv file
The data should be reformat to put every image in a folder with the name of category
Author: Shekoofeh Azizi @ UBC
"""
import data_util


if __name__ == "__main__":

    host_dir = '/media/sf_SharedDrive/WasteData/'
    raw_path = 'March2018WasteAuditRaWData'
    final_path = 'EditedWasteAuditData'

    data_handler = data_util.Data(host_dir=host_dir, raw_path=raw_path, final_path=final_path)
    data_handler.read_raw()
