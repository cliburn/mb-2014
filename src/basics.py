__author__ = 'cliburn'

def complement(seq, rule = dict(zip('ATCG', 'TAGC')) ):
    """Returns the complement of a DNA seqeunce."""

    return ''.join([rule[nuc] for nuc in seq])

def reverse_complement(seq):
    """Returns reversed complement of a DNA sequence."""

    return complement(seq)[::-1]

def test_comp():
    seq = 'ATCG'
    ans = 'TAGC'
    assert(complement(seq) == ans)

def test_rev_comp():
    seq = 'ATCG'
    ans = 'CGAT'
    assert(reverse_complement(seq) == ans)

test_comp()
test_rev_comp()

import numpy as np
dna = ''.join(np.random.choice(['A', 'T', 'C', 'G'], 100))
print dna
print complement(dna)
print reverse_complement(dna)