import random
import time

atoms = [] #  atoms are named by the order in which it arrives
molecules = [] #  list of atoms

def choose_atom():
	random_id = random.randint(0 ,len(atoms) - 1)
	return atoms[random_id]

def get_molecule(atom):
	ans = ''
	for molecule in molecules:
		if atom in molecule:
			ans = molecule
			break
	if ans == '':
		raise ValueError('atom {0} is not in any molecule'.format(atom))
	return ans

def print_detail():
	print('Top 20 molecule list:')
	molecules.sort(key=len, reverse=True)
	for mol in molecules[0:20]:
		print(len(mol))
		print(mol)

def print_chart():
	print('The molecule chart (might be empty at first):')
	molecules.sort(key=len, reverse=True)
	for mol in molecules[0:20]:
		atom_in_mol = len(mol)
		total_atoms = len(atoms)
		mol_len_percent = int( atom_in_mol/total_atoms * 100)
		print('{0}/{1} ({2}%)'.format(atom_in_mol, total_atoms, mol_len_percent))
		for _ in range(mol_len_percent):
			print('-', end='')
		print()
	print('\n')

for _ in range(1000000):	
	# add an atom whose name equals to its order 
	new_atom = str(len(atoms))
	atoms.append(new_atom)
	# then add the molecule correspond to it
	molecules.append([new_atom])

while True:
	# ALGORHYTHM
	# Then choose randomly two different atoms (skip if there's only one:
	if len(atoms) == 1:
		continue
	atom1 = choose_atom()
	atom2 = choose_atom()
	# Then take their molecules:
	mol1 = get_molecule(atom1)
	mol2 = get_molecule(atom2)
	# Then join them together (if different):
	if mol1 == mol2:
		i1, i2 = mol1.index(atom1), mol1.index(atom2)
		# SWITCH PLACE IF i1 > i2:
		if i1 > i2: i1, i2 = i2, i1
		m1, m2, m3 = mol1[:i1], mol1[i1:i2+1], mol1[i2+1:]
		if not len(m1) == 0:
			molecules.append(m1)
		if not len(m2) == 0:
			molecules.append(m2)
		if not len(m3) == 0:
			molecules.append(m3)
		molecules.remove(mol1)
	else:
		mol1.extend(mol2)
		molecules.remove(mol2)

	# PRINTING!
	print_chart()
