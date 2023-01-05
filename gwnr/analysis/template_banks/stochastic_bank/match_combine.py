#!/usr/bin/env python
# Alex Nitz

from os.path import isfile

from optparse import OptionParser

from numpy import *
### option parsing ###

parser = OptionParser()

parser.add_option('--inj-num',
                  help="index of the injection set for the match files",
                  type=int)
parser.add_option('-o',
                  '--out-file',
                  help="output file with the maximized values")
options, argv_frame_files = parser.parse_args()

index = 0
matches = []
while isfile("match" + str(options.inj_num) + "part" + str(index) + ".dat"):
    matches.append(
        loadtxt("match" + str(options.inj_num) + "part" + str(index) + ".dat"))
    index = index + 1

maxmatch = atleast_1d(array(matches).max(0))

found_index = atleast_1d(array(matches).argmax(axis=0))
found = []

fout = open(options.out_file + ".found", "w")
for index in range(0, len(found_index)):
    num = found_index[index]
    fp = open("match" + str(options.inj_num) + "part" + str(num) +
              ".dat.found")
    for i, line in enumerate(fp):
        if i == index:
            found.append(line)
            fout.write(line)
    index += 1

print(found)
print(maxmatch)
savetxt(options.out_file, maxmatch, fmt='%5.5f')

print("Max over " + str(index) + " files")
options, argv_frame_files = parser.parse_args()
