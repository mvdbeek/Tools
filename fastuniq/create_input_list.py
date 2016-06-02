import argparse


description = ("This script will create a input list file for input into FastUniq")

parser = argparse.ArgumentParser()
parser.add_argument("--fastq_R1", nargs="*", help="Path to Fastq file containing R1 reads")
parser.add_argument("--fastq_R2", nargs="*", help="Path to Fastq file containing R2 reads")
parser.add_argument("--output_list", help="List containing file paths")
args = parser.parse_args()

template = "{fastq_R1}\n{fastq_R2}\n"
with open(args.output_list, "w") as output:
    for fastq_R1, fastq_R2 in zip(args.fastq_R1, args.fastq_R2):
        list_line = template.format(fastq_R1=fastq_R1, fastq_R2=fastq_R2)
        output.write(list_line)