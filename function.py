def get_vat(payment, percent=18):
	try:
		payment = float(payment)
		percent = int(percent) 
		vat = payment / 100 * percent
		vat =  round(vat, 2)
		return "NDS: {}".format(vat)
	except (TypeError, ValueError):
		return "Хули ты весь пол засрал, ты чо мудак?!"

result = get_vat('666')
print(result)