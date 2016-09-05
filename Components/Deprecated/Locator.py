import os
import sys
import fnmatch

def locate(pattern, root=os.curdir):
    '''Locate all files matching supplied filename pattern in and below
    supplied root directory.'''
    for path, dirs, files in os.walk(os.path.abspath(root)):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(path, filename)

if __name__ == "__main__":
    for x in locate(raw_input("path to search: "),
                    raw_input("dir where search: ")):
        print x

#doesn't locate dirs
#with another func it can discover a file only by a branch of name(?)
#^ *.py <- it's works just with this simple code jet
