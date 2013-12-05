#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Generating Theoretical Spectrum Problem
Assignment #: 02
Problem ID: C
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/Sequencing-Antibiotics-by-Shattering-Them-into-Pieces-98/#step-3
'''

from scripts import ProteinWeightDict

def cyclospectrum(peptide):
	# Dictionary translating RNA to Protein
	weight = ProteinWeightDict()

	# Initialize as the mass 0 and the mass of the entire peptide.
	cyclospec = [0, sum([int(weight[protein]) for protein in peptide])]

	# Find the masses of the adjacent intermediary subpeptides
	cyclospec += [sum([int(weight[protein]) for protein in (peptide*2)[j:j+i]]) for i in xrange(1,len(peptide)) for j in xrange(len(peptide))]

	# Sort the list in ascending order and convert to strings.
	cyclospec = map(str,sorted(cyclospec))

	return cyclospec

if __name__ == '__main__':
	with open('data/stepic_2c.txt') as input_data:
		peptide = input_data.read().strip()

	cyclospec = cyclospectrum(peptide)

	# Print and save the answer.
	print ' '.join(cyclospec)
	with open('output/Assignment_02C.txt', 'w') as output_data:
		output_data.write(' '.join(cyclospec))
