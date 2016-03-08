#!/usr/bin/env python
import sys
import re
import subprocess
import argparse
import os

def __main__():

    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("--trimmed", help="an integer for the accumulator")
    parser.add_argument("--type",  help="sum the integers (default: find the max)")
    parser.add_argument("--mapping",  help="sum the integers (default: find the max)")
    parser.add_argument("--clustering_sim",  help="sum the integers (default: find the max)")
    parser.add_argument("--mapping_match_value",  help="sum the integers (default: find the max)")
    parser.add_argument("--mapping_mismatch_value",  help="sum the integers (default: find the max)")
    parser.add_argument("--mapping_gapopen_penalty",  help="sum the integers (default: find the max)")

    parser.add_argument("--calling_snp",  help="sum the integers (default: find the max)")

    parser.add_argument("--forward",  help="sum the integers (default: find the max)", nargs="*", action="append")
    parser.add_argument("--reverse",  help="sum the integers (default: find the max)", nargs="*", action="append")

    parser.add_argument("--trimmed_forward",  help="sum the integers (default: find the max)", nargs="*", action="append")
    parser.add_argument("--trimmed_paired_end",  help="sum the integers (default: find the max)", nargs="*", action="append")


    args = parser.parse_args()


    ## edit config.file
    config_file = open("config_file", "w")

    config_file.write("Number of Processors\n")
    config_file.write("4\n")
    config_file.write("Trimming\n")
    config_file.write(args.trimmed+"\n")
    config_file.write("Assembly?\n")
    config_file.write("yes\n")
    config_file.write("Type_of_Assembly\n")
    config_file.write(args.type+"\n")
    config_file.write("Clustering_Similarity%\n")
    config_file.write(args.clustering_sim+"\n")
    config_file.write("Mapping_Reads?\n")
    config_file.write(args.mapping+"\n")

    if args.mapping == "yes":
        config_file.write("Mapping_Match_Value\n")
        config_file.write(args.mapping_match_value+"\n")
        config_file.write("Mapping_MisMatch_Value\n")
        config_file.write(args.mapping_mismatch_value+"\n")
        config_file.write("Mapping_GapOpen_Penalty\n")
        config_file.write(args.mapping_gapopen_penalty+"\n")


    config_file.write("Calling_SNPs?\n")
    config_file.write(args.calling_snp+"\n")

    config_file.close()

    # prepare data
    if args.trimmed == "yes":

       # number of sample
       sample_num = 1
       for trimmed_F in args.trimmed_forward:
           # change name in order to respect : Pop1_001.R1.fq.gz
           os.system("gzip -c "+trimmed_F[0]+" > Pop1_00"+str(sample_num)+".R1.fq.gz")
           sample_num =+ 1

       # number of sample
       sample_num = 1
       for trimmed_PE in args.trimmed_paired_end:
           # change name in order to respect : Pop1_001.R1.fq.gz
           os.system("gzip -c "+trimmed_PE[0]+" > Pop1_00"+str(sample_num)+".R2.fq.gz")
           sample_num =+ 1
    else:
       # number of sample
       sample_num = 2
       for trimmed_F in args.forward:
           print trimmed_F
           # change name in order to respect : Pop1_001.R1.fq.gz
           os.system("gzip -c "+trimmed_F[0]+" > Pop1_Sample"+str(sample_num)+".F.fq.gz")
           sample_num =+ 1
       sample_num = 2
       # number of sample
       for trimmed_R in args.reverse:
           # change name in order to respect : Pop1_001.R1.fq.gz
           print trimmed_R
           os.system("gzip -c "+trimmed_R[0]+" > Pop1_Sample"+str(sample_num)+".R.fq.gz")
           sample_num =+ 1

    os.system("dDocent config_file")


if __name__=="__main__": __main__()
