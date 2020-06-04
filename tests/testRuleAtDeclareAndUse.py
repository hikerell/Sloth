import logging
from core.Ruler import Ruler

logger = logging.getLogger(__name__)
logger.info('test running...')

if __name__=='__main__':
	stmt_count = 1000
	r = Ruler()
	#e.loadfile('testBuiltin.txt')
	r.loadfile('res/edge_builtins_v2.txt')
	#e.showDefination()

	#print(r.definationContext.scopeStack)
	#print(r.cxt.scopeStack)
	#r.newRuntime()

	#t = e.expandRuleName('@ProxyExpr')
	#print('stmt: %s' % (t))
	#print(e.cxt.getCurrentScope())

	#for x in range(0, 10):
	#	t = r.safeExpandRuleName('@InitIdExpression')
	#	print('InitIdExpression: %s' % t)
	#for x in range(0, 100):
	#	t = r.safeExpandRuleName('@InitIdExpression2')
	#	print('InitIdExpression2: %s' % t)
	#for x in range(0, 5):
	#	t = r.safeExpandRuleName('@NewIdExpression')
	#	print('NewIdExpression: %s' % t)

	#print('test parser...')
	#for x in range(0, 1000):
	#	t = r.expandRuleName('@ProxyExpr')
	#	print('%04d: %s' % (x, t))

	#for x in range(0, 100):
	#	ps, t = r.safeExpandRuleName('@define_dict')
	#	#ps, t = r.safeExpandRuleName('@raw_key')
	#	#ps, t = r.safeExpandRuleName('@key')
	#	print('Statements:')
	#	for p in ps:
	#		print(p)
	#	print(t)

	stmts = []

	old_ids = set(r.cxt.getAllIDs())
	for x in range(0, 2):
		ps, t = r.safeExpandRuleName('@InitIdExpression')
		stmts.extend(ps)
		stmts.append(t)

		current_ids = set(r.cxt.getAllIDs())
		new_ids = current_ids - old_ids
		for nid in new_ids:
			print('//add operation at id %s' % nid)

			stmt = 'if(typeof(%s)=="undefined"){ %s=[]; }' % (nid, nid)
			stmts.append(stmt)

			for c_opts_on_id in range(0, 100):
				ps, t = r.safeExpandRuleName('@NoID_member_setup')
				for p in ps:
					p = p.replace('NoID', nid)
					stmts.append(p)	
				t = t.replace('NoID', nid)
				stmts.append(t)

			for c_opts_on_id in range(0, 100):
				ps, t = r.safeExpandRuleName('@NoID_member_call')
				for p in ps:
					p = p.replace('NoID', nid)
					stmts.append(p)	
				t = t.replace('NoID', nid)
				stmts.append(t)
		old_ids = current_ids

	old_ids = set(r.cxt.getAllIDs())
	for x in range(0, 10):
		ps, t = r.safeExpandRuleName('@InitIdExpression2')
		stmts.extend(ps)
		stmts.append(t)

		current_ids = set(r.cxt.getAllIDs())
		new_ids = current_ids - old_ids
		for nid in new_ids:
			print('//add operation at id %s' % nid)

			stmt = 'if(typeof(%s)=="undefined"){ %s=[]; }' % (nid, nid)
			stmts.append(stmt)

			for c_opts_on_id in range(0, 100):
				ps, t = r.safeExpandRuleName('@NoID_member_setup')
				for p in ps:
					p = p.replace('NoID', nid)
					stmts.append(p)	
				t = t.replace('NoID', nid)
				stmts.append(t)

			for c_opts_on_id in range(0, 100):
				ps, t = r.safeExpandRuleName('@NoID_member_call')
				for p in ps:
					p = p.replace('NoID', nid)
					stmts.append(p)	
				t = t.replace('NoID', nid)
				stmts.append(t)
		old_ids = current_ids

	old_ids = set(r.cxt.getAllIDs())
	for x in range(0, 10000):
		ps, t = r.safeExpandRuleName('@AssignmentExpression')
		stmts.extend(ps)
		stmts.append(t)

		current_ids = set(r.cxt.getAllIDs())
		new_ids = current_ids - old_ids
		for nid in new_ids:
			print('//add operation at id %s because of' % nid)
			print('\t%s' % '\n\t'.join(ps))
			print('\t%s' % t)

			stmt = 'if(typeof(%s)=="undefined"){ %s=[]; }' % (nid, nid)
			stmts.append(stmt)

			for c_opts_on_id in range(0, 100):
				ps, t = r.safeExpandRuleName('@NoID_member_setup')
				for p in ps:
					p = p.replace('NoID', nid)
					stmts.append(p)
				t = t.replace('NoID', nid)
				stmts.append(t)

			#for c_opts_on_id in range(0, 100):
			#	ps, t = r.safeExpandRuleName('@NoID_member_call')
			#	for p in ps:
			#		p = p.replace('NoID', nid)
			#		stmts.append(p)	
			#	t = t.replace('NoID', nid)
			#	stmts.append(t)
		old_ids = current_ids

	wapper = lambda s: 'try{ %s; }catch(e){ console.log(e); }' % s
	stmts = [wapper(stmt) for stmt in stmts]
	for stmt in stmts:
		pass
		#print(stmt)

	print('total statements: %s' % len(stmts))