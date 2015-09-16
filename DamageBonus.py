#Damage bonuses and also some new text that pops up when you deal some insane damage.

def bonusText():
	if damage <= 50:
		return 'Cool!'
	if damage > 50 and <= 150:
		return 'Great!'
	if damage > 150 and <= 299:
		return 'Fantastic!'
	if damage > 300:
		return 'Astonishing!'