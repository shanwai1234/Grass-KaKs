import argparse
import fasta_align
import codon_align

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('-s', '--species', action='append', nargs='+', help='add name of species you want to analyze')
	parser.add_argument('-i', '--inputfile', help='add the syntenic gene list file')
	parser.add_argument('-m', '--maize', action='store_true', help='open this option if you have maize in your syntenic gene list')
	args = parser.parse_args()
	single = parser.parse_args(['-m'])
	gset = set(args.species[0])
	glen = len(args.species[0])

	if single.maize:
		iind = set([])
		mind = set([])
		tlist = []
		fh = open(args.inputfile,'r')
		head = fh.readline().strip().split(',')
		for i,j in enumerate(head):
			if j not in gset:continue
			sp = j.split('_')[0]
			if 'maize' in sp:
				zm = sp
				iind.add(i)
			else:
				iind.add(i)
		for line in fh:
			new = line.strip().split(',')
			gene1 = []
			splist1 = []
			gene2 = []
			splist2 = []
			for i,j in enumerate(new):
				if i in iind:
					if 'No Gene' == j:continue
					gene1.append(j)
					if 'maize' in head[i]:
						splist1.append('{0}.fa'.format(zm))
					else:
						splist1.append('{0}.fa'.format(head[i]))
			if len(gene1) == glen:
				outfile = fasta_align.fa(gene1, splist1)
				gname = outfile.replace('.fa','')
				print "Fasta alignment file of %s is generating..." % gname
				print "Codon alignment file of %s is generating..." % gname
				k = codon_align.Fasta2Codon(gname)
				k.amino()
				k.align()
				k.codon()
				k.tree()
				k.codeml(num)
		fh.close()
	else:
		iind = set([])
		mind = set([])
		tlist = []
		fh = open(args.inputfile,'r')
		head = fh.readline().strip().split(',')
		for i,j in enumerate(head):
			if j not in gset:continue
			iind.add(i)
		for line in fh:
			new = line.strip().split(',')
			gene = []
			splist = []
			for i,j in enumerate(new):
				if i in iind:
					if j == 'No Gene':continue
					gene.append(j)
				 	splist.append(head[i])
			if len(gene) == glen:
				outfile = fasta_align.fa(gene, splist)
				gname = outfile.replace('.fa','')
				print "Fasta alignment file of %s is generating..." % gname
				print "Codon alignment file of %s is generating..." % gname
				k = codon_align.Fasta2Codon(gname)
				k.amino()
				k.align()
				k.codon()
				k.tree()
				k.codeml()
		fh.close()

if __name__ == "__main__":
	main()
