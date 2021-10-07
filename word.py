#!/usr/bin/python3
#
#  czz78 made this script for OSCP preparation
#

from concurrent.futures import ThreadPoolExecutor
import argparse


duplicates = []


def read_words(inputfile):
    with open(inputfile, 'r') as f:
        while True:
            buf = f.read(10240)
            if not buf:
                break

            # make sure we end on a space (word boundary)
            while not str.isspace(buf[-1]):
                ch = f.read(1)
                if not ch:
                    break
                buf += ch

            words = buf.split()
            for word in words:
                yield word
        yield '' #handle the scene that the file is empty


def process_file(inputfile):
    for word in read_words(inputfile):
        if word not in duplicates:
            duplicates.append(word)
            print("{}".format(word))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Make unique words list from file text')
    parser.add_argument('filename',  help='file name or multiple files separated by coma ex: /tmp/file1.txt,/tmp/file2.txt')
    args = parser.parse_args()

    myfiles = args.filename.split(',')

    # multithreading
    with ThreadPoolExecutor() as executor:
        result = executor.map(process_file, myfiles)

