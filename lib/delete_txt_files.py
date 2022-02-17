import os
import glob

def run():
    for f in glob.glob('*.txt'):
        os.remove(f)