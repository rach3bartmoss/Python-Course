def	city_and_country(city: str, country: str, population = ""):
	if population == "":
		result = city.title() + ', ' + country.title()
		return result
	else:
		result = city.title() + ', ' + country.title() + f' - Population of: {population}'
		return result

print(city_and_country('roma', 'italia', '100'))
