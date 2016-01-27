x = 5

def f1():
	return(x)

def f2():
	global x
	x = 3
	return(x)

#will print 5, x not defined in f1 so uses global
print(f1())
#will print 3, x is redefined in f2
print(f2())
#will print 3, global x was redefined when we called f2 in line 15
print(x)
