#!/usr/bin/env python

import os

myfilename = "housing.data.txt"

# if os.path.isfile(myfilename):
#   print("yay, I have a file")
#   if sky == blue:
#     print('yay the sky is blue')
# else:
#   print ('boo, no files for me')

with open(myfilename, 'r') as file_handle:
    mylist = []
    for line in file_handle.readlines():
        line_clean = line.replace('   ', ' ').replace('  ', ' ')
        line_clean = line_clean.strip()
        values = line_clean.split(' ')
        linelist = []
        for value in values:
            try:
                linelist += [int(value)]
            except ValueError as e:
                linelist += [float(value)]
        mylist += [linelist]

print("just printing a bit to save our eyes....")
print(mylist[0:2])
rotated_list = [[mylist[jdx][idx]
                 for jdx, row in enumerate(mylist)]
                for idx, column in enumerate(mylist[0])]

print(rotated_list[0])
print('finished!')
