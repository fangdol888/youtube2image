#!/usr/bin/env python
# coding: utf-8

import utils.install_lib as ins
import utils.downloading as dwn
import utils.frame_extraction as fe
import utils.filtering as ft
import utils.cropping as crp
import utils.sampling as smpl
import os
import glob
import argparse

# 'usage: python run.py [-i] [-d] [-e] [-f height weight] [-c class_name]'

def main():
    cwd = os.getcwd()
    txt_list = glob.glob(os.path.join(cwd, 'list.txt'))
    
    parser = argparse.ArgumentParser(description='Youtube video download & frames extraction, cropping, filtering, sampling tools')
    parser.add_argument('-i',action='store_true',help="install requirement library")
    parser.add_argument('-d', action='store_true',help='download video from youtube link in "list.txt", saving in \'src\'') 
    parser.add_argument('-e',action='store_true', help='extract frames from \'src\' directory')
    parser.add_argument('-f',metavar=("height", "weight"),nargs=2, help="filter images by given minimum size(height, weight)")    
    parser.add_argument('-c',metavar=("class_name"), nargs=1, help="crop images by class name")
    parser.add_argument('-s',metavar=("sample_number"),nargs=1, help="sampling by given number of samples")
    parser.add_argument('--force',action='store_true', help="If you have any data, they would be deleted")
    args = parser.parse_args()
    
    if args.i:
       ins.requirement()
    if args.d:
        dwn.downloading(txt_list)
    if args.e:
        fe.execute_extraction(cwd)
    if args.f != None:
        ft.filtering_image(list(map(int,args.f)),force=args.force)
    if args.c != None:
        crp.cropping_images(image_class=args.c[0],force=args.force)
    if args.s != None:
        smpl.sampling(n=int(args.s[0]),force=args.force)
        
if __name__ == "__main__":
    main()


    
