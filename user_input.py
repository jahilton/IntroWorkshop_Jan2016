from sys import argv

script, user_name = argv
print('hi %s, I am the %s script' % (user_name,script))
print('can I ask you some questions?')
print('what is your favorite color?')
color = input()

print('how old are you?')
age = input()

print('where do you live?')
location = input()

print('your favorite color is %r. you are %r years old. you live in %r.' % (color,age,location))
