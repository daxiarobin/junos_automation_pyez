#!/usr/bin/python

'''
Display OSPF interfaces with associated parameters
by using YAML Table and View approach

Author: Yifneg Shen
Version: 1.0
Change history:
	v1.0	2018-08-24	Y.Shen	Created first version
'''

import os,sys,yaml,glob,errno
from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
from jnpr.junos.factory import loadyaml
libpath=os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib/'))
if libpath not in sys.path:
    sys.path.append(libpath)
from getopts import GetOpts
from inputopts import InputOpts

'''
Build new option list
'''
optlist_add = []
optlist_del = ['eu','ep']

_inputopt = InputOpts()
_inputopt.optname = 'f'
_inputopt.longdes = 'YAML Table and View file, default is ./ospfoutput.yml'
_inputopt.shortdes = 'yaml'
optlist_add.append(_inputopt)

'''
Get input values
'''
opts = GetOpts(optlist_add,optlist_del)

'''
Quit the script if node or node list is not specified
'''
if opts.returncode == 12:
	sys.exit(1)
	
'''
user name/password
'''
_usrname = opts.args.u
_password = opts.args.p

'''
locate the YAML file
'''
if opts.args.f is None:
	_yamlfile = './ospfoutput.yml'
else:
	_yamlfile = opts.args.f

globals().update(loadyaml(_yamlfile))

'''
define output format
'''
outfmt = "%16s%20s%10s%16s%16s%16s%10s"

def gen_sepline(count):
	'''
	Generating the sepration line
	eg:  ----------------
	'''
	line = '-'
	for x in range(count):
		line = line + '-'
	return line

def gen_interface_table(_NODE,line):
	try:
		_dev = Device(host=_NODE,user=_usrname,password=_password)
		_dev.open()
	except Exception as err:
		print ("Can not Connect" + _NODE,err)
		return
	ospf_int_T = Ospf_int_Table(_dev)
	ospf_int_T.get()
	for ospf in ospf_int_T:
		print (outfmt % (_NODE,ospf.interface_name,
		ospf.ospf_interface_state,ospf.ospf_area,ospf.dr_id,
		ospf.bdr_id,ospf.neighbor_count))
		print (line)

	
if __name__ == "__main__":
	print ("\n" + outfmt % ("NODE",\
	"Interface","State","OSPF_area","DR","BDR","Nei_Count"))
	_sepline = gen_sepline(103)
	print (_sepline)
	
	if opts.args.n is not None:
		_node = opts.args.n
		gen_interface_table(_node,_sepline)
	else:
		_nodelist = opts.args.l
		with open(_nodelist) as f:
			lines = f.readlines()
			for line in lines:
				line = line.strip()
				gen_interface_table(line,_sepline)
	print ("\nScript Completed!")
	
	

