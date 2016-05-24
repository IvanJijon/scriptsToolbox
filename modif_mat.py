import time
import sys, getopt

def main(argv):

	start_time = time.time()
	
	# Lecture des arguments
	try:
		# h pour help, n'a pas besoin de valeur donc pas de ":" 
		# i pour input file, le nom du fichier est obligatoire donc "i:"
		# o pour output file, le nom du fichier est obligatoire donc "o:"		
		opts, args = getopt.getopt(argv,"hi:o:",["help=","inputfile=","outputfile="])
	except getopt.GetoptError:
		print 'Mauvaise syntaxe ou argument(s) non reconnu(s).'
		print 'Usage : modif_mat.py -i <inputfile> -o <outputfile>'
		print 'Pour afficler l\'aide : modif_mat.py -h'
		sys.exit(2)
	
	for opt, arg in opts:
		if opt == '-h':
			print 'Usage : modif_mat.py -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			filename_in = arg
		elif opt in ("-o", "--ofile"):
			filename_out = arg
	
	infile = open(filename_in, "r")
	outfile = open(filename_out,"w")

	# On initialise les entetes sur filename_out
	outfile.write(infile.next())
	outfile.write(infile.next())

	infile.close()

	print 'Traitement matricules en cours...'

	# On itere 35 fois
	for it in xrange(0, 36):
		
		# On ouvre infile et on saute son entete
		infile = open(filename_in, "r")
		infile.next()
		infile.next()
		
		# On prefixe les matricules
		for line in infile:
			dataline = str(it) + '_' + line
			#print dataline
			outfile.write(dataline)
		
		# On ferme infile
		infile.close()	

	# On ferme outfile
	outfile.close()
	print '...This is The End...'
	print("--- Temps d'execution : %s secondes ---" % (time.time() - start_time))
	
if __name__ == "__main__":
	main(sys.argv[1:])