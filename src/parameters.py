#!/usr/bin/env python
# encoding=utf8

# This program parses the spreadsheet file and creates the parameter_list.rst file
# that is compiled into the specification document.

import pyexcel as pe

columns = {"idstart":1,
           "count":3,
           "description":4,
           "range":5,
           "units":6,
           "datatype":8,
           "index":9,
           "remarks":10,
           "meta":11,
           "fixid":26}


sheet = pe.get_book(file_name="CAN-FIX.ods")["Identifiers"]
f = open("parameter_list.rst","wb")

first = True

for x,row in enumerate(sheet):
    if x < 2: continue

    if row[0]:
        if not first: f.write("\n")
        f.write(row[0] + "\n")
        f.write("-" * len(row[0]) + "\n\n")
        first = False
    elif row[1]:
            idstart = int(row[columns["idstart"]])
            count = int(row[columns["count"]])
            idend = idstart + count -1
            description = row[columns["description"]]
            datatype = row[columns["datatype"]]
            index = row[columns["index"]]
            range_ = row[columns["range"]]
            units = row[columns["units"]]
            remarks = row[columns["remarks"]]
            fixid = row[columns["fixid"]]
            meta = [None]*16
            mstart = columns["meta"]
            for i, each in enumerate(row[mstart:mstart+15]):
                if each: meta[i] = each
            s="{d}\n".format(d=description)
            f.write(s)
            f.write("~" * (len(s)-1) + "\n\n")
            if count == 1:
                s=":Identifier\:: {s} (0x{s:X})\n".format(s=idstart,e=idend)
            else:
                s=":Identifiers\:: {s} - {e} (0x{s:X} - 0x{e:X})\n".format(s=idstart,e=idend)
            f.write(s)
            s=u":{}\:: {}\n"
            f.write(s.format("Data Type", datatype))
            if range_: f.write(s.format("Range", range_))
            if units: # We have to do all this sillyness because of the degree symbol
                ss = s.format(u"Units", units)
                f.write(ss.encode("UTF-8"))
            if index: f.write(s.format("Index", index))
            if fixid: f.write(s.format("FIX Id", fixid))
            mstring = ""
            for i, each in enumerate(meta):
                if each:
                    mstring += "  | {:04b} = {}\n".format(i+1, each)
            if mstring != "":
                f.write(":Meta\::\n")
                f.write(mstring)
                f.write("\n")
            if remarks:
                f.write(":Remarks\::\n")
                f.write("  | " + remarks.replace("\l","\n  | ") + "\n")
            #f.write("\n\n------------------\n\n")
            f.write("\n")
