def hello_decorator(func):
	def inner1(*args,**kwargs):
		print 'inside the fucn {}'.format(func.__name__)
		ret_sum = func(*args,**kwargs)
		print 'after executing {}'.format(func.__name__)
		#return ret_sum
	return inner1



@hello_decorator
def sum_two_nos(a,b):
	print 'inside the function '
	return a+b

a,b = 1,3
print 'Sum of {} and {} is {}'.format(a,b,sum_two_nos(a,b))
