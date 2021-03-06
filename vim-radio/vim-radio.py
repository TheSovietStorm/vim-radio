import os                 
import csv
import platform
import argparse
import sys
from subprocess import call

with open(os.path.dirname(os.path.realpath(sys.argv[0]))+'/streams.csv', 'r') as f:
  reader = csv.reader(f)
  streamlist = list(reader)
parser = argparse.ArgumentParser()
parser.add_argument("n")
args=parser.parse_args()
number=int(args.n)
stream = streamlist[number][0]
if platform.system() == 'Darwin':
  call(["/Applications/VLC.app/Contents/MacOS/VLC", "-I", "rc",stream])
elif platform.system() == 'Linux':
  call(["vlc", "-I", "rc",stream])
