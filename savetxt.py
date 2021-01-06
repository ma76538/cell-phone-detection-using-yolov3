# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:50:34 2020

@author: user
"""
import os
# a=os.listdir('D:/yolov3/data/cell_phone/images/')
a=os.listdir('/Users/KevinKuok/project/cell-phone-detection/data/coco/images/train_cell_phone/')

b=[]
for i in a:
    # b.append(os.path.join('D:/yolov3/data/cell_phone/images/', i))
    b.append(os.path.join('images/train_cell_phone/', i))


with open('data/coco/train_cell_phone.txt', 'w') as filehandle:
# with open('train_cell_phone.txt', 'w') as filehandle:
    
    for listitem in b:
        filehandle.write('%s\n' % listitem)
        

a=os.listdir('/Users/KevinKuok/project/cell-phone-detection/data/coco/images/val_cell_phone/')

b=[]
for i in a:
    b.append(os.path.join('images/val_cell_phone/', i))


with open('data/coco/val_cell_phone.txt', 'w') as filehandle:
# with open('train_cell_phone.txt', 'w') as filehandle:
    
    for listitem in b:
        filehandle.write('%s\n' % listitem)