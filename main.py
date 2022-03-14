from get_mediainfo import get_mediainfo
from fieldname_list import fieldname_list

from datetime import datetime
from pathlib import Path
from operator import itemgetter
from pymediainfo import MediaInfo
from time import localtime, strftime

import csv
import os


def get_mp4_list(source_path):
    '''
    Create a list of all the MP4 files in the given Source Dir.
    File names must follow the specific pattern defined in the
    regex statement.
    '''
    os.chdir(source_path)

    mp4_source_list = []

    mp4_file_list = sorted(os.listdir(source_path), key=os.path.getctime)

    for root,d_name,f_name in os.walk(source_path):
        for f in f_name:
            if (f.endswith('.mp4') or f.endswith(".mov")): 
                mp4_source_list.append(os.path.join(root,f))
                # print(os.path.join(root,f))
            else: 
                pass
    
    mp4_file_list = sorted(mp4_source_list, key=os.path.getctime)
    # print(mp4_file_list)


    # for mp4_file in mp4_file_list:
    #     if mp4_file.endswith('.mp4'):
    #         print(mp4_file)
    #         mp4_source_list.append(mp4_file)
    #     else:
    #         continue

    for mp4 in mp4_file_list:
        mp4_dict = get_mediainfo(source_path,mp4)
        mp4_dict["file_name"] = os.path.basename(mp4)
        mp4_dict["file_path"] = os.path.dirname(mp4)
        csv_writer(mp4_dict, source_path)
        print(mp4_dict)
        print("="*20)


def csv_writer(mp4_dict, source_path):

    os.chdir("/Users/admin/Scripts/MediaInfo_to_CSV")
    file_exists = os.path.isfile("mp4_mediainfo.csv")

    fieldnames = fieldname_list
    
    with open("mp4_mediainfo.csv", mode='a') as csv_file:
        fieldnames = fieldname_list
        writer = csv.DictWriter(csv_file, delimiter=',',
                                fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(mp4_dict)
        csv_file.close
    return


if __name__ == '__main__':
    get_mp4_list("/Volumes/Quantum2/DaletStorage/Gorilla_MOV_Proxy")

