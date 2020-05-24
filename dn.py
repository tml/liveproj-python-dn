import os
import sys

def getfiles():
    found = []
    for root, dirnames, filenames in os.walk(os.getcwd()):
        found.append(''.join([item for sublist in filenames for item in sublist if sublist.endswith('.pdf')]))
    return [file for file in found if len(file)]

print(getfiles())