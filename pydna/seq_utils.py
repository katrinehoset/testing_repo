def complement_codon(input_codon):
	if is_codon_correct(input_codon) is True:
		print('Everything under normal parameters')
	else:
		print('my bad')
		return None
	base_complements = {
			'A': 'T','T': 'A','C': 'G','G': 'C',
			'?': '?',
			'N': 'N',
			'-': '-'
	}

	first_base = input_codon[0]
	second_base = input_codon[1]
	third_base = input_codon[2]

	first_complemented_base = base_complements[first_base]
	second_complemented_base = base_complements[second_base]
	third_complemented_base = base_complements[third_base]

	complemented_codon = first_complemented_base + second_complemented_base + third_complemented_base

	return complemented_codon

def is_codon_correct(input_codon):
	if type(input_codon) == float:
		return False
	
	allowed_chars=['A', 'T', 'G', 'C', 'N', '?', '-']
	
	for base in input_codon:
		if base.upper() in allowed_chars:
			continue
		else:
			print('Your codon is bad. Get your act together')
			return False
	return True

codon = 'A€G'
complement_codon(codon)
