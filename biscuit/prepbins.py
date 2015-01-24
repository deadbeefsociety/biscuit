#!/usr/bin/env python

import os
import re
import sys

def dn(f):
	f = os.path.basename(f)
	return '_bin_' + re.sub('\W', '_', f)

def sn(f):
	f = os.path.basename(f)
	return '_bin_' + re.sub('\W', '_', f) + '_len'

if len(sys.argv) <= 1:
	print 'usage: %s <bin1> <bin2>...' % (os.path.basename(sys.argv[0]))
	sys.exit(1)

print '// automatically generated by %s, do not edit' % (os.path.basename(sys.argv[0]))
print
print 'package main'
print
print '//type bin_t struct {'
print '//    data   *[]uint8'
print '//    len    int'
print '//}'
print
print 'var allbins = map[string]*elf_t{'

for prog in sys.argv[1:]:
	print '"%s" : &elf_t{ &%s, %s},' % (prog, dn(prog), sn(prog))

print '}'
print

for prog in sys.argv[1:]:
	with open(prog+'.bgo') as f:
		print ''.join(f.readlines())
