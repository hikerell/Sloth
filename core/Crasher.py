#!/usr/bin/env python3

import os
import signal
import logging
from subprocess import Popen, PIPE, TimeoutExpired
from time import monotonic as timer

logger = logging.getLogger(__name__)

def shell(command, timeout=None):
	#start = timer()
	status = 0
	stdout = b''
	stderr = b''
	with Popen(command, shell=True, stdout=PIPE, stderr=PIPE, preexec_fn=os.setsid) as process:
		try:
			stdout, stderr = process.communicate(timeout=timeout)
		except TimeoutExpired:
			os.killpg(process.pid, signal.SIGINT) # send signal to the process group
			stdout, stderr = process.communicate()
		status = process.returncode
	#print('status: %d' % status)
	#print('Elapsed seconds: {:.2f}'.format(timer() - start))

	if timeout and status==-2:
		status = 0
	return status, stdout, stderr

class Crasher(object):
	"""docstring for Crasher"""
	def __init__(self):
		super(Crasher, self).__init__()

	def execute(self, command, timeout=None):
		logger.info('execute %s' % command)
		start = timer()
		status = 0
		stdout = b''
		stderr = b''
		with Popen(command, shell=True, stdout=PIPE, stderr=PIPE, preexec_fn=os.setsid) as process:
			try:
				stdout, stderr = process.communicate(timeout=timeout)
			except TimeoutExpired:
				os.killpg(process.pid, signal.SIGINT) # send signal to the process group
				stdout, stderr = process.communicate()
			status = process.returncode
		logger.info('execute status: %d' % status)
		logger.info('execute elapsed seconds: {:.2f}'.format(timer() - start))	

		#if timeout and status==-2:
		#	status = 0
		return status, stdout, stderr

if __name__=='__main__':
	print(execute('./d8debug.sh logs/log_1538660389.68.txt', timeout=5))
	#print(shell('cat crashes/cast.txt'))
	#print(shell('cat crashes/cast.txt|./d8debug.sh'))