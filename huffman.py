'''
Name: Keval Varia
Program: Huffman Coding
Class: Data Strucutes

Program Details:
- We will implement an algorithm that would compress any given text.
- We will then print the frequency of each alphabet in the text along
  with its location in the tree. (Encode the text)
- We will then compare the decoded text with its binary file which
    would give us the compression ratio of the text.

- Text used: Gettysburg Address
'''

from heapq import heappush, heappop, heapify
from collections import defaultdict

def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


gettysbergAddress = "Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this. But, in a larger sense, we cannot dedicate -- we cannot consecrate -- we cannot hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth."

symb2freq = defaultdict(int)
encoded = []
for ch in gettysbergAddress:
    symb2freq[ch] += 1

# symb2freq = collections.Counter(gettysbergAddress)
huff = encode(symb2freq)

print "\n\nGettysburg Address:\n"
print gettysbergAddress

print "\n\nTotal Number of Characters used: " + str(len(gettysbergAddress))
print "Number of unique characters used: " + str(len(huff))

print "\n\nSymbol\tWeight\tHuffman Code"
for p in huff:
    print "%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1])

print "\n\nCompression Ratio (Exected from calculations): "
print "My binary file is 13.2kb"
print "My decoded file is 6.2kb"
print "The conversion ratio is 2:1"

print ("\n\nGettysburg Address Decoded:")
i = 0;
for x in range(len(gettysbergAddress)):
	for p in huff:
		if gettysbergAddress[x] == p[0]:
			encoded.append(p[1])
			i += 1
			print p[1],


print "\n\nDecoded back from Binary:"
for val in range(len(encoded)):
	for p in huff:
		if encoded[val] == p[1]:
			print p[0],
