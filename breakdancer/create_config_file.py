import argparse


description = ("This script will create a configuration file for samples to be run in Breakdancer."
               "If pooled analysis desired, only one config file needed for all samples."
               "Otherwise, individual analysis requires individual config files for each sample.")

parser = argparse.ArgumentParser()
parser.add_argument("--input_file", nargs="*", help="One or more alignment files")
parser.add_argument("--mean", nargs="+", help="Mean insert size")
parser.add_argument("--std_dev", nargs="+", help="The standard deviation of insert size")
parser.add_argument("--read_length", nargs="+", help="Average read length")
parser.add_argument("--sample_name", nargs="+", help="Sample name")
parser.add_argument("--output_config_file", help="Name of the output config file")
args = parser.parse_args()

template = "map:{input_file}\tmean:{mean}\tstd:{std_dev}\treadlen:{read_length}\tsample:{sample_name}\texe:samtools view\n"
with open(args.output_config_file, "w") as output:
    for input_file, mean, std_dev, read_length, sample_name in zip(args.input_file, args.mean, args.std_dev, args.read_length, args.sample_name):
        config_line = template.format(input_file=input_file, mean=mean, std_dev=std_dev, read_length=read_length, sample_name=sample_name)
        output.write(config_line)