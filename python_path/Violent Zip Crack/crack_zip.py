#!/usr/bin/env python3
import zipfile
import argparse
def extractOnce(file_name,pwd=None,path='./'):
    try:
        with zipfile.ZipFile(file_name) as zFile:
            zFile.extractall(path=path,pwd=pwd)
            print("Success with password: {}".format(pwd.decode("utf-8")))
            return True
    except Exception as e:
        print("Failed with password: {}".format(pwd.decode("utf-8")))
        return False

if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Regards to your name")
    parser.add_argument('-f',dest='zFile',type=str,help='Zip File Path')
    parser.add_argument('-w',dest='pwdFile',type=str,help='Password Dictionary File Path')
    try:
        options=parser.parse_args()
    except:
        print(parser.parse_args(['-h']))
        exit(0)
    if (not options.zFile) or (not options.pwdFile):
        print(parser.parse_args(['-h']))
        exit(0)

    finish=False
    with open(options.pwdFile) as f:
        while not finish:
            this_pwd=f.readline().strip()
            finish=extractOnce(options.zFile,this_pwd.encode('utf-8'))
            finish|=(len(this_pwd) ==0 )
    