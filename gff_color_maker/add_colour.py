#!/usr/bin/env python
# coding: utf-8

import argparse
import doctest  # This will test if the functions are working


parser = argparse.ArgumentParser()
parser.add_argument("--input", help="GFF file")
parser.add_argument("--features", nargs='+', help='Features')
parser.add_argument("--colours",nargs='+', help='Colours for each feature')
parser.add_argument("--output", help="GFF file with colours")
args = parser.parse_args()


with open(args.output, "w") as output:
    with open(args.input) as input_file_handle:
        dictionary = dict(zip(args.features, args.colours))
        for line in input_file_handle:
            columns = line.strip().split("\t")
            if columns[2] in dictionary:
                columns[8] = columns[8] + "Colour={colour}\n".format(colour = dictionary[columns[2]])
            output.write("\t".join(columns))