import sys

fh = open('temp_codeml_output.txt','r')
mdict = {}
n = 1
out = open('maize_version4_kaks.txt','a')
sb = sys.argv[1]
zm = sys.argv[2]
si = sys.argv[3]
#out.write('Maize,dn,ds,dn/ds,Sorghum,dn,ds,dn/ds,Seteria,dn,ds,dn/ds'+'\n')
for line in fh:
	if n == 2:
		new = line.strip().split(',')
		zm_ds = new[0].split(':')[1].replace(' ','')
		sb_ds = new[1].split(':')[1].replace(')','').replace(' ','')
		si_ds = new[2].split(':')[1].replace(');','').replace(' ','')		
	if n == 4:
		new = line.strip().split(',')
		zm_dn = new[0].split(':')[1].replace(' ','')
		sb_dn = new[1].split(':')[1].replace(')','').replace(' ','')
		si_dn = new[2].split(':')[1].replace(');','').replace(' ','')	
	if n == 7:
		new = line.strip().split(',')
		zm_as = new[0].split('#')[1].replace(' ','')
		sb_as = new[1].split('#')[1].replace(')','').replace(' ','')
		si_as = new[2].split('#')[1].replace(');','').replace(' ','')
	n += 1
	out.write(zm+','+zm_dn+','+zm_ds+','+zm_as+','+sb+','+sb_dn+','+sb_ds+','+sb_as+','+si+','+si_dn+','+si_ds+','+si_as+'\n')
fh.close()
out.close()
