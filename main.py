import regular
import noble_gas


while True:
	try:
		preference = input("(r)egular or (n)oble gas style?: ")
		print()
	except TypeError:
		print("Invalid entry.")
		continue

	if not(preference == "r" or preference == "R" or preference == "n" or preference == "N"):
		print("Invalid entry.")
		continue
	else:
		break

if preference == "r" or preference == "R":
	regular.regular_config()
else:
	noble_gas.noble_gas_config()
