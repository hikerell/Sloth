import fixTestImport

import re

from plugins import JS

f = open('tmp.js', 'w')

m = JS.JSRegexMaker()
for x in range(0, 100):
	print('[%d]' % x)
	p = m.makePattern()
	strp = p.replace('"', '\\"')

	tpl = 'try{ /*%d*/RegExp("%s"); }catch(e){ console.log("[E:%d] "+e); }' % (x, strp, x)
	print(tpl)
	print('')
	f.write(tpl+'\n')
f.write('console.log("finished!")\n')
f.close()


