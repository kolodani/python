set_coutries = {'col', 'mex', 'bol'}

size = len(set_coutries)
print(size)

print('col' in set_coutries)
print('per' in set_coutries)

# add
set_coutries.add('per')
print(set_coutries)

# update
set_coutries.update({'arg', 'ecu', 'per'})
print(set_coutries)

# remove
set_coutries.remove('col')
print(set_coutries)

set_coutries.remove('arg')
print(set_coutries)

set_coutries.discard('usa')
print(set_coutries)

set_coutries.clear()
print(set_coutries)
print(len(set_coutries))