import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import os
import shutil

class Fasta2Codon():

	def __init__(self, gene):
		self.n = gene

	def amino(self):
		name = self.n
		infile = name+'.fa'
		outfile = name+'_protein.fa'
		out = open(outfile, 'w')
		with open(infile, 'r') as fh:
			for line in fh:
				if line.startswith('>'):
					out.write(line)
				else:
					string = line.strip()
					cds = Seq(string, IUPAC.ambiguous_dna)
					p = cds.translate()
					out.write(str(p)+'\n')
		fh.close()
		out.close()

	def align(self):
		name = self.n
		protein = name+'_protein.fa'
		aln = name+'.aln'
		os.system("sed -i 's/\.//g' {0}".format(protein))
		os.system('kalign -i {0} -f clu -o {1}'.format(protein, aln))
		os.system('sed -e 1,3d -i {0}'.format(aln))
		
	def codon(self):
		name = self.n
		aln = name+'.aln'
		cdn = name+'.codon'
		protein = name+'_protein.fa'
		nucl = name+'.fa'
		os.system('perl pal2nal.pl {0} {1} -output paml > {2}'.format(aln, nucl, cdn))
		shutil.move(cdn, 'codon_alignment/{0}'.format(cdn))
		os.remove(aln)
		os.remove(nucl)
		os.remove(protein)

	def tree(self):
		# you need to customize this function to meet the number of species you analyze
		name = self.n
		name = name.replace('.','')
		n = name.split('_') # split tandom syntenic genes into individual ones, you need to figure out the order
		sb = n[0]
		zm = n[1]
		si = n[2]
		with open('species.trees','w') as out: 
			out.write('(({0},{1}),{2});'.format(zm,sb,si)+'\n') # modify the tree file according the evolutionary relationship between your species
			out.close()

	def codeml(self):
		name = self.n
		n = name.split('_')
		sb = n[0]
		zm = n[1]
		si = n[2]
		cdn = name+'.codon'
		shutil.copy('codon_alignment/{0}'.format(cdn), './species.codon')				
		os.system('codeml codeml.ctl') # you need to edit the codeml.ctl file to adjust parameters based on your criteria
		os.system('tail '+'-10 '+'species_unroot_model1 | '+'head '+'-7 > '+'temp_codeml_output.txt')
		os.system('python extract_codeml.py {0} {1} {2}'.format(sb,zm,si))
			
if __name__ == "__main__":
	Fasta2Codon()
