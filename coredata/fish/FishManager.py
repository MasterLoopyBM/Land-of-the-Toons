from coredata.fish import FishNames
import random

def chooseRandomFish(ID, name):
	for ID, name in FishNames.FishTypes:
		ID, name = random.choice(FishTypes)
	return (ID, name)

def chooseRandomWeight(minWeight, maxWeight):
	minWeight, maxWeight = FISH_MIN_WEIGHT, FISH_MAX_WEIGHT
	randNumA = random.random()
	randNumB = random.random()
	randNumC = (randNumA + randNumB) / 2.0
	randWeight = minWeight + (maxWeight - minWeight) * randNumC
	return int(round(randWeight * 16)
	
def getValue(value):
	value = (randWeight * RARITY) * 2