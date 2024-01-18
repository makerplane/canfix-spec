#!/usr/bin/env python

# This program parses the Spreadsheet that has all of our CANFix definitions and
# creates the official canfix.xml file

#
import pyexcel as pe

inputfile = "CAN-FIX.ods"
outputfile = "canfix.xml"
canfixVersion = "0.7"

tablebuilder = pe.get_book(file_name=inputfile)
out = open(outputfile, 'wb')

NameColumn = 0
StartColumn = 3
EndColumn = 6

out.write("<protocol>\n<name>CANFIX</name>\n".encode("UTF-8"))
out.write(f"<version>{canfixVersion}</version>\n".encode("UTF-8"))


for x, row in enumerate(tablebuilder["Groups"]):
    if x < 1: continue  # Not sure why slicing doesn't work on sheets - quick hack
    if row[NameColumn]:
        out.write("<group>\n".encode("UTF-8"))
        out.write(f"  <name>{row[NameColumn]}</name>\n".encode("UTF-8"))
        out.write(f"  <startid>{row[StartColumn]}</startid>\n".encode("UTF-8"))
        out.write(f"  <endid>{row[EndColumn]}</endid>\n".encode("UTF-8"))
        out.write("</group>\n".encode("UTF-8"))
        print("Writing Group: %s" % row[NameColumn])

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
        print("Writing Parameter: %s" % row[nameColumn])
        out.write("<parameter>\n".encode("UTF-8"))
        out.write(f"  <id>{row[idColumn]}</id>\n".encode("UTF-8"))
        out.write(f"  <count>{row[countColumn]}</count>\n".encode("UTF-8"))
        out.write(f"  <name>{row[nameColumn]}</name>\n".encode("UTF-8"))

        if not row[typeColumn]:
            print("Warning: Type not set for %s" % row[nameColumn])
            s = ""
        else:
            s = row[typeColumn]
        out.write(f"  <type>{s}</type>\n".encode("UTF-8"))

        if row[rangeColumn]:
            s = row[rangeColumn]
            if s.find(" to ") != -1:
                ranges = s.replace(" to ", "$").split("$")
                #out.write("  <range>\n")
                out.write(f"  <min>{ranges[0]}</min>\n".encode("UTF-8"))
                out.write(f"  <max>{ranges[1]}</max>\n".encode("UTF-8"))
                #out.write("  </range>\n")
            else:
                out.write(f"  <format>{s}</format>\n".encode("UTF-8"))

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
                out.write(f"  <multiplier>{mult}</multiplier>\n".encode("UTF-8"))
            s = f"  <units>{units}</units>\n"
            out.write(s.encode("UTF-8"))

        if row[indexColumn]:
            out.write(f"  <index>{row[indexColumn]}</index>\n".encode("UTF-8"))
        if row[remarksColumn] != None:
            remarks = row[remarksColumn].replace(r"\l", "\l").split("\l")
            for s in remarks:
                out.write(f"  <remarks>{s}</remarks>\n".encode("UTF-8"))
        #out.write("  <>%s</>\n" % row[Column])

        for i in range(15):
            s = row[auxColumnStart + i]
            if s:
                out.write(f"  <meta id='{i+1}'>{s}</meta>\n".encode("UTF-8"))

        out.write("</parameter>\n".encode("UTF-8"))

out.write("</protocol>\n".encode("UTF-8"))

out.close
