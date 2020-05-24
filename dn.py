import os
import sys


def getfiles():
    found = []
    for root, dirnames, filenames in os.walk(os.getcwd()):
        found.extend([item for item in filenames if item.endswith(".pdf")])
    return [file for file in found if len(file)]


if __name__ == "__main__":
    print(getfiles())
