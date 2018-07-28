import os
import sys
import gene_extraction

def fa(*args):

	mlist = []
	nlist = []

	for arg, fa in zip(args[0], args[1]):
		mlist.append(arg)
		nlist.append(arg+'.fa')
		gene_extraction.extfa(fa, arg) #gene_extraction(fasta file, gene name)	

	outfile = '_'.join(mlist)+'.fa'

	with open(outfile,'w') as three:
		for fname in nlist:
			with open(fname) as infile:
				for line in infile:
					three.write(line)
			infile.close()
	three.close()

	for arg in args[0]:
		os.remove('{0}.fa'.format(arg))

	return outfile

if __name__ == "__main__":
	codon(*args)
