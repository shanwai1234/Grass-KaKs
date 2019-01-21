# Grass-KaKs ![](https://img.shields.io/badge/Release-v1.0.1-blue.svg)  [![](https://img.shields.io/pypi/l/Django.svg)](https://github.com/shanwai1234/Grass-KaKs/commits/master)
Grass-KaKs is used to calculate the ratio of the number of nonsynonymous substitutions per non-synonymous site (Ka) to the number of synonymous substitutions per synonymous site (Ks) per gene in multiple grass species.

## Dependencies

- The code only works under Linux system.
- Install [Phylogenetic Analysis by Maximum Likelihood (PAML)](http://abacus.gene.ucl.ac.uk/software/paml.html) in your environmental path.
- Syntenic gene list with multiple species (example could be found in [here](https://figshare.com/articles/Pan_Grass_Syntenic_Gene_Set_sorghum_referenced_/3113488/1)).
- Relevant CDS sequence with primary transcript of your analyzed species. Name of fasta file should be idential with name in the header file of syntenic gene list (e.g. sorghum3.fa, setaria2.fa and maize4.fa).

## Run the analysis

### This is an example to run analysis for three species including maize, sorghum and setaria.
```
 python grass-kaks-generator.py -s sorghum3 maize4_1 setaria2 -i syntenic_list_example.csv -m
```
- `-s`, species name you want to analyze, it should be idential as the header in syntenic gene list file.
- `-i`, syntenic gene list.
- `-m`, since maize contains a whole genome duplication, set this flag when you include maize in the analysis. maize1 and maize2 should be run separately.

The header for these three species is `Maize,dn,ds,dn/ds,Sorghum,dn,ds,dn/ds,Seteria,dn,ds,dn/ds`

### Several things you need to notice
- each subgenome of WGD (Whole Genome Duplication) Species is analyzed separately
- unflag `-m` if you do not contain species of maize
- clean up `codon_alignment` folder after you run
- modify `tree` function in `codon_align.py` based on relations among your species
- customize parameters in `codeml.ctl` as your requirements. Detailed setting could be found in [here](http://nebc.nerc.ac.uk/bioinformatics/documentation/paml/doc/pamlDOC.pdf)  
- modify `extract_codeml.py` to extract dn(Ka), ds(Ks) and dn/ds(Ka/Ks) ratio for corresponding species
- change the header for your input species.
