my_dic = {}

#dictionary with integer keys

my_dic = {1:'apple',2:'ball'}

print(my_dic)

#dictionary with mixed keys
my_dict_mixed = {'name':'john',1:[1,2,3]}

print(my_dict_mixed)

#using dict()

my_dict_function = dict({1:'Fahim',2:2.1})

#from sequence having each item as a pair

my_dict_pair = dict([(1,'apple'), (2,'ball')])

#access dictionary

my_dict_access = {'name':'Fahim','subject':'CSE'}

print(my_dict_access)

print(my_dict_access['name'])

#with get
print(my_dict_access.get('name'))

#delete or remove
squares = {1:1, 2:4, 3:9, 4:16, 5:25}

print(squares.pop(4))
