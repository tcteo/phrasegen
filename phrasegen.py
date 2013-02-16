#!/usr/bin/env python
# Phrase generator
# by TEO Tse Chin <tsechin at tsechin dot com>
# 
# Generates xkcd-style phrases - http://xkcd.com/936/

import random

punctuation = ''.join( [chr(c) for c in range(33,47+1)+range(58,64+1)+range(91,96+1)+range(123,126+1) ] )
uppercase = ''.join( [chr(c) for c in range(ord('A'),ord('Z')+1)] )

def phrasegen(
	wordFile = '/usr/share/dict/words',
	minWordLength = 1,
	maxWordLength = 10,
	wordsPerSet = 4,
	numSets = 10,
	excludeWordsContainingChars = uppercase + punctuation
	):

	excludeChars = [x for x in excludeWordsContainingChars]

	f = open(wordFile)
	filteredWords = []
	allWords = f.readlines()
	for w in allWords:
		w = w.strip()
		wl = len(w)
		select = True
		if (wl<minWordLength): select = False
		if (wl>maxWordLength): select = False
		for c in excludeChars:
			if not -1 == w.find(c):
				select = False
				break;
		if select:
			filteredWords.append(w)
	print "Selecting from a filtered list of %d words" % ( len(filteredWords) )
	phrases = []
	for n in range(0,numSets):
		phrase=[]
		for m in range(0,wordsPerSet):
			phrase.append( filteredWords[random.randrange(0,len(filteredWords))] )
		phrases += [ phrase ]
	return phrases

if '__main__'==__name__:
	phrases = phrasegen()

	print '\n'.join( [ ' '.join(p) for p in phrases] )
	
