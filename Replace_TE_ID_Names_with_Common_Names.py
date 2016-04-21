
# coding: utf-8

# In[56]:

get_ipython().system('wget --output-document TE_Names.tsv https://mississippi.snv.jussieu.fr/datasets/abd2998095546994/display?to_ext=gg')
get_ipython().system('wget --output-document TE_seq_d.fasta https://mississippi.snv.jussieu.fr/datasets/ee837b421679e431/display?to_ext=fasta')


# In[3]:

get_ipython().system('ls')


# In[37]:

import argparse


# In[38]:

import doctest  # This will test if the functions are working


# In[57]:

def get_dict(te_name_file_handle):
    """
    This function creates a dictionary out of the file provided containing TE ID names\
    and their common usage names
    """
    dictionary = {}
    for line in te_name_file_handle:
        line = line.strip()
        key, value = line.split("\t")
        dictionary[key] = value
    return dictionary


# In[58]:

def replace_id(line, dictionary):
    """
    This function reads a fasta_header and replaces the ID name with Transposon name used in/
    Flybase Transposon Sequence Set
    """
    key = line[1:].strip()
    if key in dictionary:
        line = line.replace(key,dictionary[key])
        return line
    print("Transposon %s is not present in reference genom annotation" % key)
    return line
    


# In[61]:

description = ( "This script will exchange TE ID names with their common usage names")

parser = argparse.ArgumentParser(description)
parser.add_argument("input1", help="A file containing TE ID Names and their common usage names")
parser.add_argument("input2", help="A multifasta file containing TE ID Names and their sequences")
parser.add_argument("output", help="Name of the output fasta file.")
# uncomment the next line only when interactively testing!
#args = parser.parse_args(["TE_Names.tsv", "TE_seq_d.fasta", "my_fancy_new_out.fasta"])
args.parse_args()


# In[62]:

args.input1


# In[63]:

with open(args.input1, encoding = "utf-8") as te_name_file_handle:
         dictionary = get_dict(te_name_file_handle)


# In[64]:

with open(args.input2, encoding = "utf-8") as te_seq_file_handle:
    with open(args.output, "w") as output:
        for line in te_seq_file_handle:
            if line.startswith(">"):
                line = replace_id(line, dictionary)
            output.write(line)


# In[54]:

get_ipython().system('ls')


# In[ ]:



