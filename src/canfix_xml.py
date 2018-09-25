#!/usr/bin/env python

# This program parses the Spreadsheet that has all of our CANFix definitions and
# creates the official canfix.xml file

#
import pyexcel as pe

inputfile = "CAN-FIX.ods"
outputfile = "canfix.xml"
canfixVersion = "0.7"

tablebuilder = pe.get_book(file_name=inputfile)
out = open(outputfile, 'w')

NameColumn = 0
StartColumn = 3
EndColumn = 6

out.write("<protocol>\n<name>CANFIX</name>\n")
out.write("<version>%s</version>\n" % canfixVersion)


for x, row in enumerate(tablebuilder["Groups"]):
    if x < 1: continue  # Not sure why slicing doesn't work on sheets - quick hack
    if row[NameColumn]:
        out.write("<group>\n")
        out.write("  <name>%s</name>\n" % row[NameColumn])
        out.write("  <startid>%s</startid>\n" % row[StartColumn])
        out.write("  <endid>%s</endid>\n" % row[EndColumn])
        out.write("</group>\n")
        print "Writing Group: %s" % row[NameColumn]

idColumn = 1
nameColumn = 4
countColumn = 3
rangeColumn = 5
unitsColumn = 6
typeColumn = 8
offsetColumn = 7
indexColumn = 9
remarksColumn = 10
auxColumnStart = 11

for x,row in enumerate(tablebuilder["Identifiers"]):
    if x < 2: continue
    if row[idColumn]:
        print "Writing Parameter: %s" % row[nameColumn]
        out.write("<parameter>\n")
        out.write("  <id>%s</id>\n" % row[idColumn])
        out.write("  <count>%s</count>\n" % row[countColumn])
        out.write("  <name>%s</name>\n" % row[nameColumn])

        if not row[typeColumn]:
            print("Warning: Type not set for %s" % row[nameColumn])
            s = ""
        else:
            s = row[typeColumn]
        out.write("  <type>%s</type>\n" % s)

        if row[rangeColumn]:
            s = row[rangeColumn]
            if s.find(" to ") != -1:
                ranges = s.replace(" to ", "$").split("$")
                #out.write("  <range>\n")
                out.write("  <min>%s</min>\n" % ranges[0])
                out.write("  <max>%s</max>\n" % ranges[1])
                #out.write("  </range>\n")
            else:
                out.write("  <format>%s</format>\n" % s)

        #if row[offsetColumn]:
        #    out.write("  <offset>%s</offset>\n" % row[offsetColumn])

        if row[unitsColumn]:
            i = 0
            #s = row[unitsColumn].replace(u'\xba',u'deg')
            s = row[unitsColumn]
            for x in range(len(s)-1):
                if s[x].isdigit(): 
                    i = 0
                    break
            if i == 0:
                mult = None
                units = s
            else:
                i=i+1
                mult = s[:i]
                units = s[i:].strip()

            if mult:
                out.write("  <multiplier>%s</multiplier>\n" % mult)
            s = u"  <units>%s</units>\n" % units
            out.write(s.encode("UTF-8"))

        if row[indexColumn]:
            out.write("  <index>%s</index>\n" % row[indexColumn])
        if row[remarksColumn] != None:
            remarks = row[remarksColumn].replace(r"\l", "\l").split("\l")
            for s in remarks:
                out.write("  <remarks>%s</remarks>\n" % s)
        #out.write("  <>%s</>\n" % row[Column])

        for i in range(15):
            s = row[auxColumnStart + i]
            if s:
                out.write("  <aux id='%d'>%s</aux>\n" % (i+1, s))

        out.write("</parameter>\n")

out.write("</protocol>\n")

out.close
