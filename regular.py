from mendeleev import element


def regular_config():
	key = ["1s2", "2s2", "2p6", "3s2", 
			"3p6", "4s2", "3d10", "4p6", 
			"5s2", "4d10", "5p6", "6s2"]

	atom = element(input("element: "))

	atom_num = atom.atomic_number

	counter = 0
	config = []

	for item in key:
		spaces = int(item[2:])

		for i in range(1, spaces + 1):
			counter += 1

			if counter == atom_num:
				config.append(str(item[:2]) + str(i))

				for term in config:
					print(term, end=" ")

		config.append(item)
