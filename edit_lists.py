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
print len(keys)
print len(names)

#print names

print "The names have been read"

#block of code that compares the keys
if 0:
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

# block of code from Yue
if 1:
	output_file = open("output-yue",'w')
	for index, nameFromNames in enumerate(names):
		# print nameFromNames
		arr = nameFromNames.strip().split()
		keyofname = arr[0]
		if keyofname not in keys:
			output_file.write(nameFromNames)
			output_file.write("\n")
			
	output_file.close()
			

print "The keys have been compared and deleted if found in both files "
print "Names have been output to the file"
