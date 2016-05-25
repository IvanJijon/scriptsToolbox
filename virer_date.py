import time
import sys, getopt

def main(argv):

	start_time = time.time()
	
	# Lecture des arguments
	try:
		# h pour help, n'a pas besoin de valeur donc pas de ":" 
		# i pour input file, le nom du fichier est obligatoire donc "i:"
		# o pour output file, le nom du fichier est obligatoire donc "o:"		
		opts, args = getopt.getopt(argv,"hi:o:p:m:",["help=","inputfile=","outputfile=","position=","matricule="])
	except getopt.GetoptError:
		print 'Mauvaise syntaxe ou argument(s) non reconnu(s).'
		print 'Usage : virer_date.py -i <inputfile> -o <outputfile> -p <position_champs> -m <position_matricule>'
		print 'Pour afficler l\'aide : virer_date.py -h'
		sys.exit(2)
	
	for opt, arg in opts:
		if opt == '-h':
			print 'Usage : virer_date.py -i <inputfile> -o <outputfile> -p <position_champs -m <position_matricule>>'
			sys.exit()
		elif opt in ("-i", "--inputfile"):
			filename_in = arg
		elif opt in ("-o", "--outputfile"):
			filename_out = arg
		elif opt in ("-p", "--position"):
			position = arg
		elif opt in ("-m", "--matricule"):
			matricule = arg
	
	infile = open(filename_in, "r")
	outfile = open(filename_out,"w")

	# On initialise les entetes sur filename_out
	outfile.write(infile.next())
	outfile.write(infile.next())

	infile.close()

	print 'Traitement en cours...'

	# On itere 35 fois
	for it in xrange(0, 36):
		
		# On ouvre infile et on saute son entete
		infile = open(filename_in, "r")
		infile.next()
		infile.next()
		
		# Traitement des champs
		for line in infile:
			tmp = line.split('|')
			
			# On prefixe les matricules
			tmp[int(matricule)-1] = str(it) + '_' + tmp[int(matricule)-1]
			
			# On ne conserve pas les registres de Novembre 2015
			if tmp[int(position)-1] != '201511':
				dataline = "|".join(tmp)
				outfile.write(dataline)
		
		# On ferme infile
		infile.close()	

	# On ferme outfile
	outfile.close()
	print '...This is The End...'
	print("--- Temps d'execution : %s secondes ---" % (time.time() - start_time))
	
if __name__ == "__main__":
	main(sys.argv[1:])