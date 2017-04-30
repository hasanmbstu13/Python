def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1) > len(dna2)    

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    num_nucleotide = 0

    for char in dna:
        if char == nucleotide:
            num_nucleotide = num_nucleotide + 1
            
    return num_nucleotide

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1

def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if dna contains only following letters A, T, C, G
    otherwise return False.

    >>> is_valid_sequence('ATTTGGCC')
    True
    >>> is_valid_sequence('ATTGHHK')
    False
    '''

    found = True

    for char in dna:
        if char not in 'ATCG':
            found = False

    return found

def insert_sequence(dna1, dna2, index):
    ''' (str, str, int) -> str

    Return the string that will produce by inserting dna2 in dna1
    by given index.

    >>> insert_sequence('CCGG', 'AT', 2)
    CCATGG
    >>> insert_sequence('CCGGTA', 'AT', 1)
    CATCGGTA
    '''

    return dna1[:index] + dna2 + dna1[index:]

def get_complement(nucleotide):
    ''' (str) -> str

    Return the complement of given nuclotide.

    >>> get_complement('A')
    T
    >>> get_complement('T')
    A
    >>> get_complement('C')
    G
    '''

    if nucleotide == 'A':
        nucleotide = 'T'
    elif nucleotide == 'T':
        nucleotide = 'A'
    elif nucleotide == 'C':
        nucleotide = 'G'
    elif nucleotide == 'G':
        nucleotide = 'C'

    return nucleotide

def get_complementary_sequence(dna_sequence):
    ''' (str) -> str

    Return the complementary sequence of given dna_sequence.

    >>> get_complementary_sequence('AT')
    TA
    >>> get_complementary_sequence('TA')
    AT
    >>> get_complementary_sequence('CG')
    GC
    '''

    complement_sequence = ''
    
    if dna_sequence == 'AT':
        complement_sequence = 'TA'
    elif dna_sequence == 'TA':
        complement_sequence = 'AT'
    elif dna_sequence == 'CG':
        complement_sequence = 'GC'
    elif dna_sequence == 'GC':
        complement_sequence = 'CG'

    return complement_sequence
        
        
    
