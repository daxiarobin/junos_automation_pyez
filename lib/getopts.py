'''
Functions to handle user input options
Author: Yifeng Shen
Version: 1.0
Change history:
	v1.0	2018-08-24	Y.Shen	Created first version
'''
import argparse,os,sys,getpass
libpath=os.path.abspath(os.path.join(os.path.dirname(__file__), './'))
if libpath not in sys.path:
    sys.path.append(libpath)
from inputopts import InputOpts
from errorcode import ErrorCode

class GetOpts(object):
	'''
	Build default option object list
	'''
	optionlist = []	
	optionnamelist = []
	
	_inputopt = InputOpts()
	_inputopt.optname = 'n'
	_inputopt.longdes = 'node name or ip'
	_inputopt.shortdes = 'node'
	optionlist.append(_inputopt)
	optionnamelist.append(_inputopt.optname)
	
	_inputopt = InputOpts()
	_inputopt.optname = 'l'
	_inputopt.longdes = 'full path of node list file'
	_inputopt.shortdes = 'nodelist'
	optionlist.append(_inputopt)
	optionnamelist.append(_inputopt.optname)
	
	_inputopt = InputOpts()
	_inputopt.optname = 'u'
	_inputopt.longdes = 'CLI user name to access the node'
	_inputopt.shortdes = 'username'
	optionlist.append(_inputopt)
	optionnamelist.append(_inputopt.optname)
	
	_inputopt = InputOpts()
	_inputopt.optname = 'p'
	_inputopt.longdes = 'CLI password to access the node'
	_inputopt.shortdes = 'password'
	optionlist.append(_inputopt)
	optionnamelist.append(_inputopt.optname)
	
	_inputopt = InputOpts()
	_inputopt.optname = 'eu'
	_inputopt.longdes = 'user name for debug/enable mode'
	_inputopt.shortdes = 'e_user'
	optionlist.append(_inputopt)
	optionnamelist.append(_inputopt.optname)
	
	_inputopt = InputOpts()
	_inputopt.optname = 'ep'
	_inputopt.longdes = 'password for debug/enable modoe'
	_inputopt.shortdes = 'e_password'
	optionlist.append(_inputopt)
	optionnamelist.append(_inputopt.optname)
	
	_inputopt = InputOpts()
	_inputopt.optname = 'o'
	_inputopt.longdes = 'output directory for all the log files, default is /tmp'
	_inputopt.shortdes = 'out'
	optionlist.append(_inputopt)
	optionnamelist.append(_inputopt.optname)
	
	err = ErrorCode()
	def __init__(self,optlist_add=[],optlist_del=[]):
		'''
		Step 1: Construct option descrption list 
		The elements in this list are all InputOpts objects.
		
		Step 2: Read and store the input values
		
		:param
			optlist_add	-	list of InputOpts objects to be added 
			optlist_del	-	list of option names (string only) to be removed
		'''
		
		'''
		add new options
		'''
		for _opt in optlist_add:
			self.optionlist.append(_opt)
			
		'''
		remove the options which are not required
		'''
		for _optname in optlist_del:
			for _opt in self.optionlist:
				if _opt.optname == _optname:
					self.optionlist.remove(_opt)
		
		'''
		define the return code, this variable is ued to determine 
		whether there is error when initiating the object
		'''
		self.returncode = 0
		
		'''
		read the input 
		'''
		self.parser = argparse.ArgumentParser()
	
		for _opt in self.optionlist:
			self.parser.add_argument(('-' + _opt.optname),required=_opt.mandatory,
			help=_opt.longdes)
	
		self.args = self.parser.parse_args()
		
		'''
		Node or nodelist must be specified
		'''
		if 'n' in self.optionnamelist and \
			'l' in self.optionnamelist:
			try:
				if self.args.n is None and self.args.l is None:
					self.returncode = 12
					self.err.thrownmsg(self.returncode)
					self.parser.print_help()
					return
			except:
				'''
				do nothing
				'''
		
		'''
		Read user name and password
		'''
		if 'u' in self.optionnamelist:
			try:
				if self.args.u is None:
					self.args.u = input("Please input cli user name:")
			except:
				'''
				do nothing
				'''
		if 'p' in self.optionnamelist:
			try:
				if self.args.p is None:
					self.args.p = getpass.getpass('Please input cli password:')
			except:
				'''
				do nothing
				'''
		if 'eu' in self.optionnamelist:
			try:
				if self.args.eu is None:
					self.args.eu = input("Please input debug/enable user name:")
			except:
				'''
				do nothing
				'''
		if 'ep' in self.optionnamelist:
			try:
				if self.args.ep is None:
					self.args.ep = getpass.getpass('Please input debug/enable password:')
			except:
				'''
				do nothing
				'''
		'''
		Determine output directory
		'''
		if self.args.o is None:
			self.args.o = '/tmp'
