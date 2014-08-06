## Script Name: interproAppender.py
## Purpose: Append info from interpro output into annotation file
## Created by James Pickett
## University of Connecticut
##
## Version: 1.0.0
## Last Edit 8/6/2014
## Usage: Run from terminal, filename can be included in line or a query will appear on run (Wildcard and Relative OK)

import glob

target = glob.glob(raw_input("Enter the name of the annotation file (Relative and wildcards OK) \n"))[0]
jobInput = glob.glob(raw_input("Enter the name of the interpro output file (Relative and wildcards OK) \n"))[0]

with open(target,'r') as inputFile:
	annoArray = inputFile.read().split('\n')
with open(jobInput,'r') as inputFile:
	interArray = inputFile.read().split('\n')


modAnnoArray = []
modInterArray = []
sequencePFams = []
targets = []

for fields in annoArray:
	fields = fields.split('\t')
	modAnnoArray.append(fields)
	targets.append(fields[0][:fields[0].find('|')])

for fields in interArray:
	modInterArray.append(fields.split('\t'))

for fields in modInterArray:
	fields[0] = fields[0][7:]


for i in range(len(modInterArray) - 1):
	try:
		pos = targets.index(modInterArray[i][0])
	except ValueError:
		continue
	modAnnoArray[pos].append(modInterArray[i][11])
	modAnnoArray[pos].append(modInterArray[i][5])
	modAnnoArray[pos].append(modInterArray[i][12])
	modAnnoArray[pos].append(modInterArray[i][13])

output = raw_input("Enter filename you would like output stored in (Relative and wildcards OK, include filetype) \n")
with open(output,'w') as outputFile:
	for fields in modAnnoArray:
		outputFile.write('%s\n'%'\t'.join(fields))