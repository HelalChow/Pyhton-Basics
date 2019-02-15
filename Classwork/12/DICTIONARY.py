#TYPE DICTIONARY

d = {'had':7, 'farm': 3, 'he': 6}
#print(d['had']) returns 7

d['moo'] = 10 #adds 'moo' to dictionary
#print(d)

print('had' in d) # returns true

#FUNCTIONS
del d['had']  #deletes an item from dictionary
min(d)
max(d)

for x in d:     #iterates over the keys (words)
    print(x)

for x in d:             #iterates over as tuples
    item = (x, d[x])
    print(item)