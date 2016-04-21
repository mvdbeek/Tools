#!/usr/bin/env python
# coding: utf-8

import argparse
import doctest  # This will test if the functions are working


def get_id(line):
    """
    This function reads a line and returns the ID name
    
    >>> line = 'ID   TE    standard; DNA; INV; 7411 BP.'
    >>> 'TE'== get_id(line)
    True
    
    """
    if line.startswith("ID"):
        id = line.split("   ")[1] #split line into 'ID' and rest of line, take rest of line and define as id
        id = id.split(" ")[0] #split id into 'ID name' and rest of line, take ID name and define as id
        return id


def get_seq(line):
    """
    This function reads a sequence line from a genbank file
    and returns a sequence with no spaces or digits
    
    >>> line = "AGTGACATAT TCACATACAA AACCACATAA CATAGAGTAA ACATATTGAA AAGCCGCATA        60"
    >>> 'AGTGACATATTCACATACAAAACCACATAACATAGAGTAAACATATTGAAAAGCCGCATA' == get_seq(line)
    True
    
    """
    seq = []
    for char in line:
        if not char.isdigit() and not char == " ":  # If a character is not a digit or space, 
                                                    # it will be added to sequence.
            seq.append(char)
    seq = "".join(seq)
    return seq


def make_seq_dictionary(input_file_handle):
    """
    This function loops over a multi genbank file and returns
    a collection of ID and corresponding sequence in a dictionary.
    """
    seq_d = {}  # dictionary with id as key and sequence as value
    next_line_is_seq = False
    for line in input_file_handle:
        line = line.strip()  # strips any leading or trailing whitespace
        if line.startswith("ID"):
            id = get_id(line)
            seq_d[id]=""  # We just create a new key
        if line.startswith("SQ"):
            next_line_is_seq = True  # If line starts with 'SQ' then state is true
            continue
        if line.startswith("//"):  # If line starts with '//' then state is false
            next_line_is_seq = False
        if next_line_is_seq:  # Whatever has been read as true, this is copied to file
            seq = get_seq(line)
            seq_d[id] += seq
    return seq_d


def write_seq_d_to_file(seq_d, output):
    """
    This function will write the sequence dictionary to an output file
    """
    for transposon, seq in seq_d.items():
        output.write(">%s\n" % transposon)
        output.write("%s\n" % seq)

description = ( "This script will extract ID names and sequences from a multigenbank"
               "file and format them into a multifasta file." )


parser = argparse.ArgumentParser(description)
parser.add_argument("input", help="A multi-genbank file.")
parser.add_argument("output", help="Name of the output fasta file.")
args = parser.parse_args()

try:
    with open(args.input, encoding = "utf-8") as input_file_handle:
        # This will perform the tasks
        seq_d = make_seq_dictionary(input_file_handle)
except TypeError:
    with open(args.input) as input_file_handle:
        seq_d = make_seq_dictionary(input_file_handle)

with open(args.output, "w") as output:
    write_seq_d_to_file(seq_d, output)

