
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftEQUALSleftPLUSMINUSleftTIMESDIVIDErightUMINUSAND BOOL_FALSE BOOL_TRUE DIVIDE EQUALS LPAREN MINUS NAME NUMBER OR PLUS RPAREN STRING TIMESstatement : NAME EQUALS expressionstatement : expressionexpression : expression PLUS expression\n                      | expression MINUS expression\n                      | expression TIMES expression\n                      | expression DIVIDE expressionexpression : expression OR expression\n                      | expression AND expression\n        expression : MINUS expression %prec UMINUSexpression : LPAREN expression RPARENexpression : NUMBERexpression : STRINGexpression : BOOL_TRUEexpression : BOOL_FALSEexpression : NAME'
    
_lr_action_items = {'NAME':([0,4,5,10,11,12,13,14,15,16,],[2,18,18,18,18,18,18,18,18,18,]),'MINUS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,],[4,-15,12,4,4,-11,-12,-13,-14,4,4,4,4,4,4,4,-9,-15,12,12,-3,-4,-5,-6,12,12,-10,]),'LPAREN':([0,4,5,10,11,12,13,14,15,16,],[5,5,5,5,5,5,5,5,5,5,]),'NUMBER':([0,4,5,10,11,12,13,14,15,16,],[6,6,6,6,6,6,6,6,6,6,]),'STRING':([0,4,5,10,11,12,13,14,15,16,],[7,7,7,7,7,7,7,7,7,7,]),'BOOL_TRUE':([0,4,5,10,11,12,13,14,15,16,],[8,8,8,8,8,8,8,8,8,8,]),'BOOL_FALSE':([0,4,5,10,11,12,13,14,15,16,],[9,9,9,9,9,9,9,9,9,9,]),'$end':([1,2,3,6,7,8,9,17,18,20,21,22,23,24,25,26,27,],[0,-15,-2,-11,-12,-13,-14,-9,-15,-1,-3,-4,-5,-6,-7,-8,-10,]),'EQUALS':([2,],[10,]),'PLUS':([2,3,6,7,8,9,17,18,19,20,21,22,23,24,25,26,27,],[-15,11,-11,-12,-13,-14,-9,-15,11,11,-3,-4,-5,-6,11,11,-10,]),'TIMES':([2,3,6,7,8,9,17,18,19,20,21,22,23,24,25,26,27,],[-15,13,-11,-12,-13,-14,-9,-15,13,13,13,13,-5,-6,13,13,-10,]),'DIVIDE':([2,3,6,7,8,9,17,18,19,20,21,22,23,24,25,26,27,],[-15,14,-11,-12,-13,-14,-9,-15,14,14,14,14,-5,-6,14,14,-10,]),'OR':([2,3,6,7,8,9,17,18,19,20,21,22,23,24,25,26,27,],[-15,15,-11,-12,-13,-14,-9,-15,15,15,-3,-4,-5,-6,15,15,-10,]),'AND':([2,3,6,7,8,9,17,18,19,20,21,22,23,24,25,26,27,],[-15,16,-11,-12,-13,-14,-9,-15,16,16,-3,-4,-5,-6,16,16,-10,]),'RPAREN':([6,7,8,9,17,18,19,21,22,23,24,25,26,27,],[-11,-12,-13,-14,-9,-15,27,-3,-4,-5,-6,-7,-8,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,4,5,10,11,12,13,14,15,16,],[3,17,19,20,21,22,23,24,25,26,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> NAME EQUALS expression','statement',3,'p_statement_assign','dsl.py',124),
  ('statement -> expression','statement',1,'p_statement_expr','dsl.py',128),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','dsl.py',132),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','dsl.py',133),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','dsl.py',134),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','dsl.py',135),
  ('expression -> expression OR expression','expression',3,'p_expression_condition','dsl.py',146),
  ('expression -> expression AND expression','expression',3,'p_expression_condition','dsl.py',147),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','dsl.py',155),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','dsl.py',159),
  ('expression -> NUMBER','expression',1,'p_expression_number','dsl.py',163),
  ('expression -> STRING','expression',1,'p_expression_string','dsl.py',167),
  ('expression -> BOOL_TRUE','expression',1,'p_expression_bool_true','dsl.py',171),
  ('expression -> BOOL_FALSE','expression',1,'p_expression_bool_false','dsl.py',175),
  ('expression -> NAME','expression',1,'p_expression_name','dsl.py',179),
]
