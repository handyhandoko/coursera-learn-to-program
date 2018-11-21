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
    return get_length(dna1) > get_length(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


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
    """ (str) -> bool
    
    return True if and only dna contain 'A', 'T', 'C', 'G'. Otherwise return False 

    >>> is_valid_sequence('ATACAG')
    True
    >>> is_valid_sequence('ATaCAG')
    False
    >>> is_valid_sequence('AFAGAC')
    False
    """
    for character in dna:
        if character not in ['A', 'T', 'C', 'G']:
            return False
    return True

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str
    
    return new dna where dna2 inserted into dna1 on index position.

    >>> insert_sequence('CCGG', 'AT', 2)
    CCATGG
    """
    new_dna = ''
    if index == len(dna1):
        return dna1+dna2
    for character_index, character in enumerate(dna1):
        if character_index == index:
            new_dna = new_dna + dna2
        new_dna = new_dna + character
    return new_dna

def get_complement(nucleotide):
    """ (str) -> str
    
    return complement of nucleotide

    >>> get_complement('A')
    T
    >>> get_complement('T')
    A
    >>> get_complement('G')
    C
    >>> get_complement('C')
    G
    """
    if(nucleotide == 'A'):
        return 'T'
    if(nucleotide == 'T'):
        return 'A'
    if(nucleotide == 'G'):
        return 'C'
    if(nucleotide == 'C'):
        return 'G'
    else:
        return False

def get_complementary_sequence(dna):
    """ (str) -> str
    
    return compelentary sequence of dna

    >>> get_complementary_sequence('ATCCG')
    TAGGC
    """
    complementary_sequence = ''
    for nucleotide in dna:
        complementary_sequence = complementary_sequence + get_complement(nucleotide)
    return complementary_sequence
