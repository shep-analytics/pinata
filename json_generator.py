import random
import json

#seeds the generator
random.seed(10)

# Attribute Export from Blender
accesories = {'eyes': ['Superman', 'Black', 'Brown', 'Light Blue', 'Blue', 'Hazel', 'Green', 'Yellow', 'Orange', 'Purple', 'Red', 'Pink', 'Glow eyes', 'Zooted', 'Vampire', 'Warewolf'], 'furs': ['Classic', 'Brown', 'Black', 'Charcoal', 'Coral', 'Lemon Lime', 'Party Pink', 'Sky Blue', 'Grizzly', 'Bumblebee', 'Honey', 'Neon Red', 'Neon Green', 'Neon Pink', 'Neon Blue', 'Neon Orange', 'Neon Yellow', 'Light Tree', 'Quartz', 'Cheese', 'Treebear', 'NeoChrome', 'Ceramic', 'Copper', 'MysticChrome', 'Alien Goo', 'Gold', 'Dented Metal', 'Silver', 'Snow', 'Rusty', 'Gummy', 'Strawberry Milk', 'Moo', 'Dark Aether', 'Rainbow', 'Sea Glass', 'Light Polka-Dot', 'Dark Polka-Dot', 'Chocolate'], 'backgrounds': ['grass', 'island', 'beach', 'snow forest', 'yacht', 'kitchen', 'moon', 'igloo', 'future mall', 'aspen street', 'tokyo', 'city', 'mars', 'mars', 'jamaica'], 'Neck': ['Burgandy Baller Bowtie', 'Spiked Collar', 'Timekepper', 'Christmas', 'Heart Locket', 'Large Christmas Lights', 'Gold Chain', 'Party Beeds', 'Bear Bandanna', 'Lanyard', 'Lavender Baller Bowtie', 'Lei', 'Glowstick Necklace', 'Tie (Black)', 'Tie (Blue)', 'Tie (Red)'], 'Head': ['Beer Bucket Hat', 'BirthdayHat', 'Propeller Hat', 'Drivers Hat Blue', 'Devil Horns', 'Pirate Hat', 'Chocolate Factory', 'Royal Crown', 'Elf Hat', 'Steampunk Hat', 'Top Hat', 'Cowboy Hat', 'Burgandy Beanie', 'Halo', 'Ice Crown', 'Santa Hat', 'Christmas Glasses', 'Antlers', 'Penguin'], 'Eyewear': ['Visionary', '3D Glasses', 'Swimmers', 'Bookkeeper', 'Space Invadors', 'Hollywood', 'Aviators', 'Bifocals', 'Blu Blockers', 'Party Glasses (Blue)', 'Steampunk Goggles', 'Sixties', 'New Years Glasses', 'Party Glasses (Red)', 'Party Glasses (Green)', 'The Defenders', 'The Stockbrokers', 'Ski Goggles', 'Eyepatch'], 'Hand': ['Beer Bottle', 'Cola', 'Honey Pot', 'Apple Pie', 'Balloons', 'Birthday Horn', 'Candy Cane', 'Cream Cola', 'Hotdog', 'Ice Cream', 'Icicle', 'Red Rose', 'Cave Dweller', 'Cola Pop', 'Oktoberfest', 'Mojito'], 'Earrings': ['Tripple Hoops', 'Black Rings', 'Gold Hoops', 'Studs', 'Round Studs', 'Spiked Studs', 'Beartrap', 'Donut', 'Gold Bow', 'Heart', 'Bottle Caps'], 'Badges': ['Maple Mountains', 'Candy Corridor', 'Rasta Rainforest', 'Viking Valley', 'Glacier Falls']}

#will create a json dictionary for a bear
def create_json():
	metadata = {}
	for (index, item) in accesories.items():
		metadata[index] = item[random.randrange(len(item))]
#	background = backgrounds[random.randrange(len(backgrounds))]
#	fur = furs[random.randrange(len(furs))]
#   eyes = eyes[random.randrange(len(eyes))]
	# head
	# eyewear
	# earrings
	# neck
	# hand
	return(metadata)

num_to_create = 100

full_bear_dict = []

for i in range(0,num_to_create):
	bear = create_json()
	full_bear_dict.append(bear)
	
with open('metadata.json', 'w', encoding='utf-8') as f:
    json.dump(full_bear_dict, f, ensure_ascii=False, indent=4)