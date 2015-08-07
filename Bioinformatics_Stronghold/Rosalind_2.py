"""Problem

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t."""

T = str('GATGGAACTTGACTACGTAAATT')
t_list = []

for x in T:
    if x == "T":
       t_list.append("U")
    elif x != "T":
         t_list.append(x)
t = ''.join(t_list)
print t

