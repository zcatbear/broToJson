#!/usr/local/bin/python
import json
from collections import OrderedDict
import argparse

parser = argparse.ArgumentParser(description="Tranlate a bro log to its json counterpart")
parser.add_argument('-i', '--inputFile', help='This is the file to be read in', required=True)
parser.add_argument('-o', '--outputFile', help="This is the file to be spit out, Default is broToJsonOut.json", default='broToJsonOut.json')
parser.add_argument('-p', '--printout', action='store_true')
args = parser.parse_args()




inputFile = open(args.inputFile) #TODO Change this over to an argument based approach
outputFile = open(args.outputFile, 'w')
fields = list()
for line in inputFile:
    if line[:7] == "#fields":
        fields.extend(line.strip().split('\t')[1:])
    elif line[0] == "#":
        continue
    else:
        myDict = OrderedDict()
        lineList = line.strip().split('\t')
        if (len(lineList)!= len(fields)):
            continue
        for index, element in enumerate(lineList):

            if element == '(empty)':
                element = '-'
            myDict[fields[index]] = element
        jsonOut = json.dumps(myDict)
        if (args.printout):
            print jsonOut
        else:
            outputFile.write(jsonOut + "\n")
outputFile.close()


