#!/usr/bin/env python

# This program parses the Spreadsheet that has all of our CANFix definitions and
# creates the official canfix.xml file
 
# import the needed modules
import zipfile
import xml.parsers.expat

inputfile = "CAN-FIX-0.6.ods"
outputfile = "canfix.xml"
canfixVersion = "0.6"

class TableBuilder:
    def __init__(self):
        self.tables = {}
        self.row = 0
        self.cell = None
        self.table = []
        self.row = []
    def start_element(self, name, attrs):
        if name == "table:table":
          print "Parsing Table: " + attrs["table:name"]
          self.tables[attrs["table:name"]] = list()
          self.table = self.tables[attrs["table:name"]]
        if name == "table:table-row":
          self.row = []
        if name == "table:table-cell":
          if "table:number-columns-repeated" in attrs.keys():
            for i in range(int(attrs["table:number-columns-repeated"]) -1):
              self.row.append(None)
          self.cell = None
    def end_element(self, name):
        if name == "table:table-row":
          self.table.append(self.row)
        if name == "table:table-cell":
          self.row.append(self.cell)
    def char_data(self, data):
        self.cell = data
        
# get content xml data from OpenDocument file
ziparchive = zipfile.ZipFile(inputfile, "r")
xmldata = ziparchive.read("content.xml")
ziparchive.close()
print xmldata
out = open(outputfile, 'w')

# create parser and parsehandler
parser = xml.parsers.expat.ParserCreate()
tablebuilder = TableBuilder()
# assign the handler functions
parser.StartElementHandler  = tablebuilder.start_element
parser.EndElementHandler    = tablebuilder.end_element
parser.CharacterDataHandler = tablebuilder.char_data
parser.DefaultHandler       = tablebuilder.char_data
 
# parse the data
parser.Parse(xmldata, True)

# At this point tablebuilder.tables is a dictionary of lists of lists.  The dictionary
# represents the sheet name and the list of lists is the table

NameColumn = 0
StartColumn = 3
EndColumn = 6

out.write("<protocol>\n<name>CANFIX</name>\n")
out.write("<version>%s</version>\n" % canfixVersion)

for row in tablebuilder.tables["Groups"][1:]:
    if row[NameColumn] != None:
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

for row in tablebuilder.tables["Identifiers"][2:]:
    if row[idColumn] != None:
        print "Writing Parameter: %s" % row[nameColumn]
        out.write("<parameter>\n")
        out.write("  <id>%s</id>\n" % row[idColumn])
        out.write("  <count>%s</count>\n" % row[countColumn])
        out.write("  <name>%s</name>\n" % row[nameColumn])
        
        if row[typeColumn] == None:
            print("Warning: Type not set for %s" % row[nameColumn])
            s = ""
        else:
            s = row[typeColumn]
        out.write("  <type>%s</type>\n" % s)
                
        if row[rangeColumn] != None:
            s = row[rangeColumn]
            if s.find(" to ") != -1:
                ranges = s.replace(" to ", "$").split("$")
                #out.write("  <range>\n")
                out.write("  <min>%s</min>\n" % ranges[0])
                out.write("  <max>%s</max>\n" % ranges[1])
                #out.write("  </range>\n")
            else:
                out.write("  <format>%s</format>\n" % s)
        
        if row[offsetColumn] != None:
            out.write("  <offset>%s</offset>\n" % row[offsetColumn])
        
        if row[unitsColumn] != None:
            s = row[unitsColumn].replace(u'\xba',u'deg')
            for i in range(len(s)-1, -1, -1):
                if s[i].isdigit(): break
            if i == 0:
                mult = None
                units = s
            else:
                i=i+1
                mult = s[:i]
                units = s[i:].strip()
                
            if mult:
                out.write("  <multiplier>%s</multiplier>\n" % mult)
            out.write("  <units>%s</units>\n" % units)
        
        if row[indexColumn] != None:
            out.write("  <index>%s</index>\n" % row[indexColumn])
        if row[remarksColumn] != None:
            remarks = row[remarksColumn].replace(r"\l", "\l").split("\l")
            for s in remarks:
                out.write("  <remarks>%s</remarks>\n" % s)
        #out.write("  <>%s</>\n" % row[Column])

        for i in range(15):
            s = row[auxColumnStart + i]
            if s != None:
                out.write("  <aux id='%d'>%s</aux>\n" % (i+1, s))
       
        out.write("</parameter>\n")
    
out.write("</protocol>\n")
       
out.close
