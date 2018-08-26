'''
Class to represent user input options/arguments
Author: Yifeng Shen
Version: 1.0
Change history:
	v1.0	2018-08-24	Y.Shen	Created first version
'''

class InputOpts(object):
	'''
	create a option class which includes all the attributes
	which can describe the option
	'''
	def __init__(self):
		'''
		:param
			optname	-	option name, normally a sigle letter, eg "n"
			longdes	-	full description of the option,
						eg: node name or ip address
			type	-	data type of the option, default is string
			shortdes	-	short description of the given option
			mandatory	-	Whther this option is mandatory. True or False
							Default value is False
		
		:Usage Example
			from inputopts import InputOpts
			_inputopt = InputOpts()
			_inputopt.optname = 'n'
			_inputopt.longdes = 'nodename or ip'
			_inputopt.shortdes = 'node'
			_inputopt.mandatory = 'True'
			_inputopt.type = 'string'
			
		'''
		self.optname = ''
		self.longdes = ''
		self.shortdes = ''
		self.mandatory = False
		self.type = 'string'

'''
Test function
'''
'''
if __name__ == "__main__":
	list = []
	_inputopt = InputOpts();
	_inputopt.optname = 'n'
	list.append(_inputopt)
	_inputopt = InputOpts();
	_inputopt.optname = 'l'
	list.append(_inputopt)
	for opt in list:
		print (opt.optname)
'''
	
		
		
	
