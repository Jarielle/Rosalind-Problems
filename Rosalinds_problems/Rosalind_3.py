"""Problem
mv 
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s."""

from Bio.Seq import Seq

s = Seq('AAAACCCGGT')
sc = s.reverse_complement()
 
print sc
