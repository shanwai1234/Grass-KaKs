# Grass-KaKs![](https://img.shields.io/badge/Release-v1.0.1-blue.svg)  [![](https://img.shields.io/pypi/l/Django.svg)](https://github.com/shanwai1234/Grass-KaKs/commits/master)
Grass-KaKs is used to calculate the ratio of the number of nonsynonymous substitutions per non-synonymous site (Ka) to the number of synonymous substitutions per synonymous site (Ks) per gene in multiple grass species.

## Dependencies

- The code only works under Linux system.
- Install [Phylogenetic Analysis by Maximum Likelihood (PAML)](http://abacus.gene.ucl.ac.uk/software/paml.html) in your environmental path.
- Syntenic gene list with multiple species (example could be found in [here](10.6084/m9.figshare.3113488.v1)).
- Relevant CDS sequence with primary transcript of your analyzed species.

## Run the analysis

### This is an example to run analysis for three species including maize, sorghum and setaria.
```
 python grass-kaks-generator.py -s sorghum3 maize4_1 setaria2 -i syntenic_list_example.csv -m
```
- -s, species name you want to analyze, it should be idential as the header in syntenic gene list file.
- -i, syntenic gene list.
- -m, since maize contains a whole genome duplication, set this flag when you include maize in the analysis. maize1 and maize2 should be run separately.

The header for these three species is `Maize,dn,ds,dn/ds,Sorghum,dn,ds,dn/ds,Seteria,dn,ds,dn/ds`

### Several things you need to notice
- unflag m if you do not contain species of maize
- clean up `codon_alignment` folder after you run
- modify `tree` function in `codon_align.py` based on relations among your species
- modify `extract_codeml.py` to extract dn(Ka), ds(Ks) and dn/ds ratio for corresponding species
