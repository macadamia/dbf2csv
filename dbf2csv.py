#!/usr/bin/python

import csv
from dbfpy import dbf
from os import rename
import sys
from glob import glob

filename = sys.argv[1]

listdb = glob('%s.*' % filename)

for dbFile in listdb:
    rename(dbFile, dbFile.lower())

filename = '%s.dbf' % filename.lower()

if filename.endswith('.dbf'):
    print "Converting %s to csv" % filename
    csv_fn = filename[:-4]+ ".csv"
    with open(csv_fn,'wb') as csvfile:
        in_db = dbf.Dbf(filename)
        out_csv = csv.writer(csvfile)
        names = []
        for field in in_db.header.fields:
            names.append(field.name)
        out_csv.writerow(names)
        for rec in in_db:
            out_csv.writerow(rec.fieldData)
        in_db.close()
        print "Done..."
else:
  print "Filename does not end with .dbf"
