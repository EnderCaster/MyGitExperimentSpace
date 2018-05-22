#!/usr/bin/env python3
#-*- utf-8 -*-
import sys
import os
def parse_file(path):
    """analyse the text file (path) ,return the count of space, tabs and lines
    :arg path: the path of the file to analyse
    :return; the summary tuple
    """
    the_file = open(path)
    i =0
    spaces=0
    tabs=0
    for i,line in enumerate(the_file):
        # the i ..... used directly, its the i on top
        spaces+=line.count(' ')
        tabs+=line.count("\t")
    the_file.close()
    return spaces,tabs,i+1

def main(path):
    """just do print
    :arg path: the path of the file to analyse
    :return: if the path exists
    """
    if os.path.exists(path):
        spaces,tabs,lines=parse_file(path)
        print("spaces{:4d},tabs{:4d},lines{:4d}".format(spaces,tabs,lines))
        return True
    else:
        return False

if __name__=="__main__":

    if len(sys.argv)>1:
        main(sys.argv[1])
    else:
        sys.exit(-1)
    sys.exit(0)