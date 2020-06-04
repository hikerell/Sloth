
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON ID TEXT\n\tRULE : RULENAME COLON RULENODES\n\t\n\tRULENAME : ID\n\t\n\tRULENODES : RULENODE\n\t\t\t  | RULENODES RULENODE\n\t\n\tRULENODE : TEXTNODE\n\t\t\t | NAMENODE\n\t\n\tTEXTNODE : TEXT\n\t\n\tNAMENODE : RULENAME\n\t'
    
_lr_action_items = {'ID':([0,3,4,5,6,7,8,9,10,11,],[3,-2,3,-8,3,-3,-5,-6,-7,-4,]),'$end':([1,3,5,6,7,8,9,10,11,],[0,-2,-8,-1,-3,-5,-6,-7,-4,]),'COLON':([2,3,],[4,-2,]),'TEXT':([3,4,5,6,7,8,9,10,11,],[-2,10,-8,10,-3,-5,-6,-7,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'RULE':([0,],[1,]),'RULENAME':([0,4,6,],[2,5,5,]),'RULENODES':([4,],[6,]),'RULENODE':([4,6,],[7,11,]),'TEXTNODE':([4,6,],[8,8,]),'NAMENODE':([4,6,],[9,9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> RULE","S'",1,None,None,None),
  ('RULE -> RULENAME COLON RULENODES','RULE',3,'p_rule','Parser.py',34),
  ('RULENAME -> ID','RULENAME',1,'p_rulename','Parser.py',44),
  ('RULENODES -> RULENODE','RULENODES',1,'p_rulenodes','Parser.py',50),
  ('RULENODES -> RULENODES RULENODE','RULENODES',2,'p_rulenodes','Parser.py',51),
  ('RULENODE -> TEXTNODE','RULENODE',1,'p_rulenode','Parser.py',63),
  ('RULENODE -> NAMENODE','RULENODE',1,'p_rulenode','Parser.py',64),
  ('TEXTNODE -> TEXT','TEXTNODE',1,'p_textnode','Parser.py',70),
  ('NAMENODE -> RULENAME','NAMENODE',1,'p_namenode','Parser.py',79),
]