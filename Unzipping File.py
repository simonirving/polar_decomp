#######################################################
#Date:      Feb 2 2021#
#Name:      Robert Simon Irving#
#Purpose:   SentinelSat API#
#           COGS Project 2021#
#######################################################
#======================================================#
#1. Import Modules
#======================================================#
import zipfile
import os
import time

dashes = '=' * 120
start = time.process_time()
#======================================================#
#2. Unzip Files
#======================================================#
files = os.listdir('rawdata')

#print(files)
print(dashes)
print('Starting to Decompress Files')
print(dashes)
for file in files:
    if file.endswith('.zip'):
        filepath = 'rawdata' + '/' + file
        print('Decompressing files from ---> ' + str(filepath))
        print(dashes)
        print('Processing ........')
        zip_file = zipfile.ZipFile(filepath)
        for names in zip_file.namelist():
            print(names)
            zip_file.extract(names)
        zip_file.close()
#print(dashes)
#======================================================#
#3. Renaming File Folder
#======================================================#
for f in os.listdir():
    if f.endswith('.SAFE'):
        os.rename(f,'data')
        #print(f)

print(dashes)
print('It took ' + str(time.process_time() - start) + ' seconds to complete')
print(dashes)
print('Files have been decompressed')
print(dashes)