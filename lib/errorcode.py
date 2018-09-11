'''
Purpose: mapping between error code name and value
'''

class ErrorCode(object):
	NOERROR = 0
	INPUTERROR = 1
	MISSINPUT = 10
	WRONGINPUTTYPE = 11
	MISSNODE = 12
	
	def __init__(self):
		'''
		'''
	
	def thrownmsg(self,code):
		'''
		Print and return the error message based on
		the error code value
		'''
		msg = self.returnmsg(code)
		print (msg)
		return msg
		
	def thrownanymsg(self,errmessage):
		'''
		Print any error message based on user input
		'''
		print (errmessage)
		return errmessage
		
	def returnmsg(self,code):
		return {
		self.NOERROR: '',
		self.INPUTERROR: 'Error: Invalid input option or values',
		self.MISSINPUT: 'Error: Missing input option or value',
		self.WRONGINPUTTYPE: 'Error: Incorrect input data type',
		self.MISSNODE: 'Error: node or nodelist must be specified'
		}.get(code,"unknown error")
	