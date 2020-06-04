import os, sys

testsdir = os.path.dirname(os.path.realpath(__file__))
projdir = os.path.dirname(testsdir)

if projdir not in sys.path:
	sys.path.append(projdir)

print('======== Test Infomation ========')
print('Project Directory: %s' % projdir)
print('Tests Directory: %s' % testsdir)
print('Test File Path: %s' % __file__)
print('---------------------------------')