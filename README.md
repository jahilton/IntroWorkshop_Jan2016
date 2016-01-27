# IntroWorkshop_Jan2016
These are my exercises from an Intro to Python Workshop

Jan 26/27
Eve Porcello - eve@sbtrain.com

\n is new line

%s - string
%d - decimal
%r - raw input
——example——
year = 2016
age = 31
first_name = 'Jason'

print('my name is %s' % first_name)
print('It is %d. I am %d' % (year,age))
————————
If you want to type a quote. Use a \ before it to have it escape.
favorite_restaurant = “Chili\’s”
————————
in print statements, commas add spaces, plus signs do not (can’t mix string & integer)
print(‘I am’,first_name) —> I am Jason
print(‘I am’+first_name) —> I amJason
————————
for a list, len() tells how many items are in list
animals = [‘dog’,’cat’,’bear’,’kangaroo’]
print(len(animals)) —> 4
————————
#create a dictionary
d = {}
#create an ordered dictionary (keeps order of input)
import collections
d = collections.OrderedDict()
#add key-value pairs to diction
d['a']='A'
d['b']='B'
d['c']='C'
d['d']='D'
#print the pairs
for k, v in d.items():
	print(v, k)
