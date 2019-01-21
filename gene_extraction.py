#! /usr/bin/env python
import sys
import os

def extfa(myfile, sp):
 '''
 myfile is the fasta file, sp the gene name
 A script for extracting certain sequences from within a FASTA file.
 
 First, convert FASTA file into file with one line per sequence.
 Make sure the name of your FASTA file doesn't contain any dots
 besides the one before the extension!
 '''
    linenum = 0
    onelinefile = 'allononeline_' + myfile.partition('.')[0] + '.tmp'
    with open(onelinefile, 'w') as outfile:
        for line in open(myfile, 'r'):
            line = line.strip()
            if len(line) > 0:
                if line[0] == '>':
                    if linenum == 0:
                        outfile.write(line + '\t')
                        linenum += 1
                    else:
                        outfile.write('\n' + line + '\t')
                else:
                    outfile.write(line)
 
    # Populate a dictionary using the 'allononeline' file
    all_seqs = {}
    with open(onelinefile, 'r') as allseqsfile:
        for line in allseqsfile:
            line = line.strip().split('\t')
            all_seqs[line[0][1:]] = line[1]
 
    # Generate a set of the sequences you wish to retrieve
    desired_seqs = set()
    #with open(sys.argv[2], 'r') as listfile:
    #    for line in listfile:
    #        desired_seqs.add(line.strip())
    desired_seqs.add(sp)
 
    # Find the overlap between the total sequences and the desired ones
    all_seqs_names = set(all_seqs.keys())
    toextract = all_seqs_names.intersection(desired_seqs)
 
    # Use 'toextract' set to generate desired file
    with open(sp+'.fa', 'w') as extractfile:
        for name in toextract:
            extractfile.write('>' + name + '\n' + all_seqs[name] + '\n')
 
    os.remove(onelinefile)
