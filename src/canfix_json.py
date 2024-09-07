#!/usr/bin/env python3

# This program parses the Spreadsheet that has all of our CANFix definitions and
# creates the official canfix.xml file

#
import pyexcel as pe
import re
import json

inputfile = "CAN-FIX.ods"
outputfile = "canfix.json"
canfixVersion = "0.7"

tablebuilder = pe.get_book(file_name=inputfile)

NameColumn = 0
StartColumn = 3
EndColumn = 6

output = {}

output["name"] = "CANFIX"
output["version"] = canfixVersion

groups = []
for x, row in enumerate(tablebuilder["Groups"]):
    if x < 1: continue  # Not sure why slicing doesn't work on sheets - quick hack
    if row[NameColumn]:
        group = {}
        group["name"] = row[NameColumn]
        group["startid"] = row[StartColumn]
        group["endid"] = row[EndColumn]
        print("Writing Group: %s" % row[NameColumn])
        groups.append(group)
output["groups"] = groups

idColumn = 1
nameColumn = 4
countColumn = 3
rangeColumn = 5
unitsColumn = 6
typeColumn = 8
offsetColumn = 7
indexColumn = 9
remarksColumn = 10
metaColumnStart = 11

parameters = []
for x,row in enumerate(tablebuilder["Identifiers"]):
    if x < 2: continue
    if row[idColumn]:
        print("Writing Parameter: %s" % row[nameColumn])
        p = {}
        p["id"] = row[idColumn]
        p["count"] = row[countColumn]
        p["name"] = row[nameColumn]

        if not row[typeColumn]:
            print("Warning: Type not set for %s" % row[nameColumn])
            s = ""
        else:
            s = row[typeColumn]
        p["type"] = s.replace(" ","")

        if row[rangeColumn]:
            s = row[rangeColumn]
            if s.find(" to ") != -1:
                ranges = s.replace(" to ", "$").split("$")
                p["min"] = ranges[0]
                p["max"] = ranges[1]
            else:
                p["format"] = s

        if row[unitsColumn]:
            i = 0
            #s = row[unitsColumn].replace(u'\xba',u'deg')
            s = row[unitsColumn].replace(" ","")
            match = re.match(r"([0-9\.]+)(.+)", s)
            if match:
                items = match.groups()
                p["multiplier"] = items[0]
                p["units"] = items[1]
            else:
                #p["units"] = units.encode("UTF-8")
                p["units"] = s

            # for x in range(len(s)-1):
            #     if s[x].isdigit():
            #         i = 0
            #         break
            # if i == 0:
            #     mult = None
            #     units = s
            # else:
            #     i=i+1
            #     mult = s[:i]
            #     units = s[i:].strip()
            #
            # if mult:
            #     p["multiplier"] = mult
            #s = u"  <units>%s</units>\n" % units
            #out.write(s.encode("UTF-8"))


        p["index"] = row[indexColumn] if row[indexColumn] else None

        if row[remarksColumn]:
            p["remarks"] = row[remarksColumn].replace(r"\l", "\l").split("\l")
        else:
            p["remarks"] = None

        metadata = {}
        for i in range(15):
            s = row[metaColumnStart + i]
            if s:
                metadata[i+1] = s
        p["metadata"] = metadata
        parameters.append(p)

output["parameters"] = parameters


idColumn = 0
descColumn = 1
unitsColumn = 2
typeColumn = 3

status = []
for x,row in enumerate(tablebuilder["Status"]):
    if x < 1: continue
    if row[idColumn] != "":
        print("Writing Status: %s" % row[descColumn])
        p = {}
        p["type"] = row[idColumn]
        p["description"] = row[descColumn]

        if not row[typeColumn]:
            print("Warning: Type not set for %s" % row[descColumn])
            s = ""
        else:
            s = row[typeColumn]
        p["datatype"] = s.replace(" ","")

        if row[unitsColumn]:
            i = 0
            #s = row[unitsColumn].replace(u'\xba',u'deg')
            s = row[unitsColumn].replace(" ","")
            match = re.match(r"([0-9\.]+)(.+)", s)
            if match:
                items = match.groups()
                p["multiplier"] = items[0]
                p["units"] = items[1]
            else:
                #p["units"] = units.encode("UTF-8")
                p["units"] = s
        status.append(p)

output["status"] = status

with open(outputfile, 'w') as outfile:
    json.dump(output, outfile, indent=4, sort_keys=True)
