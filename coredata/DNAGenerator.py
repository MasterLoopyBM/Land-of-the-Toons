#DNA Generator

def newToon(head, torso, legs, gender, headColor, torsoColor, legColor, toptex, toptexcolor, bottex, bottexcolor, sleevetex, sleevetexcolor)
	if not head == HeadTypes:
		return 'Invalid head.'
	if not torso == torsoTypes:
		return 'invalid torso.'
	if not legs == legsTypes:
		return 'Invalid legs.'