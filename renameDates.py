#! /usr/bin/env python3
# renameDates.py -  Renames filenames with American MM-DD-YYYY date format
# to computer friendly date format YYYY-MM-DD.

import shutil, os, re

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((09|10|11|12|13|14|15|16))     # four digits for the year
    (.*?)$                          # all text after the date
    """, re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)

    if int(dayPart) < 10:
        dayPart = '0' + dayPart

    if int(monthPart) < 10:
        monthPart = '0' + monthPart

    # Form the computer friendly date format filename.
    friendlyFilename = beforePart + '20' + yearPart + '-' + monthPart + '-' + dayPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    friendlyFilename = os.path.join(absWorkingDir, friendlyFilename)

    # Rename the files.
    #print('Renaming "%s" to "%s"...' % (amerFilename, friendlyFilename))
    shutil.move(amerFilename, friendlyFilename)   # uncomment after testing
