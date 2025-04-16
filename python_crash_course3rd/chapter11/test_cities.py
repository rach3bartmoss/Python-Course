from city_functions import city_and_country

def	test_cityandcountry():
	t_nome = city_and_country('natal', 'brasil', '1.000.000')
	t_nome2 = city_and_country('porto', 'portugal', '1.000.000')
	t_nome3 = city_and_country('roma', 'itália')

	assert t_nome == 'Natal, Brasil - Population of: 1.000.000'
	assert t_nome2 == 'Porto, Portugal - Population of: 1.000.000'
	assert t_nome3 == 'Roma, Itália'
