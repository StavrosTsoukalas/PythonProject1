#Defining the number functions:
def zero(x = 100):
	if(x == 100):
		return 0
	if(type(x)==tuple):
		num=x[0]
		oper=x[1]
		if(oper=='+'):
			print 0 + x[0]
		elif(oper=='*'):
			print 0 * x[0]
		elif(oper=='-'):
			print 0 - x[0]

def one(x = 100):
	if(x == 100):
		return 1
	if(type(x)==tuple):
		num=x[0]
		oper=x[1]
		if(oper=='+'):
			print 1 + x[0]
		elif(oper=='*'):
			print 1 * x[0]
		elif(oper=='-'):
			print 1 - x[0]

def two(x = 100):
	if(x == 100):
		return 2
	if(type(x)==tuple):
		num=x[0]
		oper=x[1]
		if(oper=='+'):
			print 2 + x[0]
		elif(oper=='*'):
			print 2 * x[0]
		elif(oper=='-'):
			print 2 - x[0]

def three(x = 100):
	if(x == 100):
		return 3
	if(type(x)==tuple):
		num=x[0]
		oper=x[1]
		if(oper=='+'):
			print 3 + x[0]
		elif(oper=='*'):
			print 3 * x[0]
		elif(oper=='-'):
			print 3 - x[0]

def four(x = 100):
	if(x == 100):
		return 4
	if(type(x)==tuple):
		num=x[0]
		oper=x[1]
		if(oper=='+'):
			print 4 + x[0]
		elif(oper=='*'):
			print 4 * x[0]
		elif(oper=='-'):
			print 4 - x[0]

def five(x = 100):
	if(x == 100):
		return 5
	if(type(x)==tuple):
		num=x[0]
		oper=x[1]
		if(oper=='+'):
			print 5 + x[0]
		elif(oper=='*'):
			print 5 * x[0]
		elif(oper=='-'):
			print 5 - x[0]

def six(x = 100):
	if(x == 100):
		return 6
	if(type(x)==tuple):
		num=x[0]
		oper=x[1]
		if(oper=='+'):
			print 6 + x[0]
		elif(oper=='*'):
			print 6 * x[0]
		elif(oper=='-'):
			print 6 - x[0]

def seven(x = 100):
	if(x == 100):
		return 7
	if(type(x)==tuple):
		num=x[0]
		oper=x[1]
		if(oper=='+'):
			print 7 + x[0]
		elif(oper=='*'):
			print 7 * x[0]
		elif(oper=='-'):
			print 7 - x[0]

def eight(x = 100):
	if(x == 100):
		return 8
	if(type(x)==tuple):
		num=x[0]
		oper=x[1]
		if(oper=='+'):
			print 8 + x[0]
		elif(oper=='*'):
			print 8 * x[0]
		elif(oper=='-'):
			print 8 - x[0]

def nine(x = 100):
	if(x == 100):
		return 9
	if(type(x)==tuple):
		num=x[0]
		oper=x[1]
		if(oper=='+'):
			print 9 + x[0]
		elif(oper=='*'):
			print 9 * x[0]
		elif(oper=='-'):
			print 9 - x[0]

#Defining the operator functions:
def plus(x):
	return (x,'+')

def minus(x):
	return (x,'-')

def times(x):
	return (x,'*')

#Default example:
zero(plus(zero()))



#python 2.x and 3.x compatible