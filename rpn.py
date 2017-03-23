#!/usr/bin/env python3

import operator
import readline
import random
from termcolor import colored, cprint


OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow
}




def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			
			stack.append(result)
	return stack.pop()

def main():
	while True:
		result = calculate(input('rpn calc> '))
		str_result = str(result)
		arr = []
		arr.append('grey')
		arr.append('red')
		arr.append('green')
		arr.append('yellow')
		arr.append('blue')
		arr.append('magenta')
		arr.append('cyan')
		arr.append('white')
		val = random.randint(0, 7)

		str_result = colored(str_result, arr[val])
		print("Result:", str_result)

if __name__ == '__main__':
	main()
