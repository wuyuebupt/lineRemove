keys = []

#this file should be the smaller one with just the keys, not names
keys_file = "names.list"

with open(keys_file) as f:
	keys = f.read().splitlines()

#print keys

print "The keys have been read"

names = []

#this file should be the bigger file with all the keys and names
names_file = "name.en"

with open(names_file) as f:
	names = f.read().splitlines()

#print names

print "The names have been read"

#block of code that compares the keys
for keyFromKey in keys:
	keyFromName = []
	indexOfKey = 0
	length = len(keyFromKey)
	while indexOfKey < len(names):
		keyFromName.append(names[indexOfKey][0:length:])
		indexOfKey += 1
	if keyFromKey in keyFromName:
		del names[keyFromName.index(keyFromKey)]
		#print "Key deleted"
		#print names

print "The keys have been compared and deleted if found in both files "

#overwrites the file to replace the names with the modified list
output_file = open(names_file,'w')

for name in names:
	output_file.write(name)
	output_file.write("\n")

output_file.close()

print "Names have been output to the file"