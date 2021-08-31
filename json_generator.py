import random
import json

#seeds the generator
random.seed(10)


#will create a json dictionary for a bear
def create_json():
	furs = ['white', 'brown', 'black', 'grey', 'light red', 'light green','light pink', 'light blue', 'light orange', 'light yellow', 'light brown', 'neon red', 'neon green', 'neon pink', 'neon blue', 'neon orange', 'neon yellow',     'Light tree', 'Quartz', 'Cheese', 'Dark tree', 'NeoChrome', 'Ceramic', 'Copper', 'MysticChrome', 'Alien goo', 'Gold', 'Dented metal', 'Silver', 'Snow', 'Diamond plate', 'Rusty', 'Gummy',     'Barney', 'Dark moo', 'Light moo', 'Crazy stripes', 'Dark aether', 'Rainbow', 'Glowy glass', 'Spots', 'Light polka-dots', 'Dark polka-dots', 'Chocolate']
	eyes = ['Superman', 'Black', 'Brown', 'Light blue', 'Blue', 'Hazel', 'Green', 'Yellow', 'Orange', 'Purple', 'Red', 'Pink', 'Glow eyes']
	backgrounds = ['grass', 'island', 'beach', 'snow forest', 'yacht', 'kitchen','moon', 'igloo', 'future mall', 'aspen street', 'tokyo', 'city','mars','mars', 'jamaica']
	background = backgrounds[random.randrange(len(backgrounds))]
	fur = furs[random.randrange(len(furs))]
	eyes = eyes[random.randrange(len(eyes))]
	# head
	# eyewear
	# earrings
	# neck
	# hand

	metadata = {'background':background,'fur':fur,'eyes':eyes}

	return(metadata)


num_to_create = 20

full_bear_dict = {'metadata':[]}

for i in range(0,num_to_create):
	bear = create_json()
	full_bear_dict['metadata'].append(bear)
	
with open('metadata.json', 'w', encoding='utf-8') as f:
    json.dump(full_bear_dict, f, ensure_ascii=False, indent=4)