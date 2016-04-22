
# coding: utf-8
import argparse
import sys


def get_dict(tabular_file_handle):  # In this function, the file te_name_file_handle is used
    """
    This function creates a dictionary out of the file provided containing TE ID names\
    and their common usage names separated by a tab
    """
    dictionary = {}  # A dictionary is named 'dictionary'
    for line in tabular_file_handle:  # For every line in the file
        line = line.strip()  # The leading and trailing white spaces are stripped
        key, value = line.split("\t")  # The line is then split where there is a tab and 
                                       # then the two results are defined as key and value
        dictionary[key] = value  # The key(ID Name) is linked to the value(common use name)
    return dictionary  # Show dictionary on the screen


def replace_id(line, dictionary):  
# In this function, the dictionary and the lines of the te_name_file_handle are fed in.
    """
    This function reads a fasta header (line), recovers the name of the sequence "(>fasta_1)"
    and stores this in key. We look up key in the dictionary, and if the key is present,
    we replace the key in the line with the value that is assigned to the key in the
    dictionary.
    """
    key = line[1:].strip()  #The key is the ID name (not including the >)
    if key in dictionary:  #If key is in the dictionary, it is replaced
        line = line.replace(key,dictionary[key])
        return line
    print("Fasta header  %s is not present in multifastafile" % key)
    return line


description = ( "This script will exchange fasta headers in multifasta file with values linked in tabular file")

parser = argparse.ArgumentParser(description)
parser.add_argument("input1", help="A file containing two linked columns separated by a tab")
parser.add_argument("input2", help="A multifasta file containing fasta headers and their sequences")
parser.add_argument("output", help="Name of the output fasta file.")
# uncomment the next line only when interactively testing!
#args = parser.parse_args(["TE_ID_Names.tsv", "TE_seq_d.fasta", "my_fancy_new_out.fasta"])
args = parser.parse_args()


python_version = sys.version_info
if python_version.major >= 3:
    kwargs = {"encoding": "utf-8"}
else:
    kwargs = {}

with open(args.input1, **kwargs) as tabular_file_handle:
    dictionary = get_dict(tabular_file_handle)

with open(args.input2, **kwargs) as fasta_file_handle:
    with open(args.output, "w") as output:
        for line in fasta_file_handle:
           if line.startswith(">"):
                line = replace_id(line, dictionary)
           output.write(line)

