def load():
	f = open("lyrics.csv", 'r')
	lyrics = {}
	for ln in f:
		splitln = ln.split(',')
		#Remove trailing newline
		if splitln[1][-1:] == '\n':
			lyrics[int(splitln[0])] = splitln[1].decode("string-escape")[:-1]
		else:
			lyrics[int(splitln[0])] = splitln[1].decode("string-escape")
	return lyrics

def getdur(line):
	n = 0
	for c in line:
		if c == '\n':
			n += 1
	return len(line) / 4 + n * 2