import sys
import shelve

def main():
	db = shelve.open(sys.argv[1])
	for i in xrange(int(sys.argv[2])):
		s = str(i)
		db[s] = s
    
	db.sync()
	db.close()

