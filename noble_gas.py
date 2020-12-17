from mendeleev import element


def noble_gas_config():
	key = ["He1s2", "jj2s2", "Ne2p6", "jj3s2", 
			"Ar3p6", "jj4s2", "jj3d10", "Kr4p6", 
			"jj5s2", "jj4d10", "Xe5p6", "jj6s2"]

	nobles = [grp for grp in key if grp[0] != "j"]

	atom = element(input("element: "))

	atom_num = atom.atomic_number

	counter = 0
	config = []

	for item in key:
		spaces = int(item[4:])

		for i in range(1, spaces + 1):
			counter += 1

			if counter == atom_num:
				config.append(str(item[:4]) + str(i))

				for i in range(len(config) - 1, -1, -1):
					if config[i] in nobles:
						flag = i
						break

				ans = "[" + str(config[flag][:2]) + "]"

				for j in config[flag + 1:]:
					ans += f" {j[2:]}"

				print(ans)

		config.append(item)
