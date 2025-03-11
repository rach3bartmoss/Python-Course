brands = ['adidas', 'puma', 'asics', 'reebok', 'umbro']
i = 0
brand_present = False

for brand in brands:
	if brand == 'puma':
		print(brand.upper())
	else:
		print("xalalala")
	if 'asics' in brands:

		i += 1
	if 'nike' not in brands:
		brand_present = True

print(brand_present)
