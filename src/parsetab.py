
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEleftANDORleftEQEQNEQleftLTLEGTGEleftBITANDBITORBITXORleftLSHIFTRSHIFTrightNOTBITNOTAND ASSIGN BITAND BITNOT BITOR BITXOR COLON COMMA DIVIDE ENDMODULE EQ EQEQ GE GT IDENTIFIER INPUT LE LPAREN LSHIFT LSQUARE LT MINUS MODULE NEQ NOT NUMBER OR OUTPUT PLUS RPAREN RSHIFT RSQUARE SEMI TIMES WIREmodule : MODULE IDENTIFIER LPAREN port_list RPAREN SEMI module_items ENDMODULEport_list : port\n    | port_list COMMA portport : INPUT range_opt IDENTIFIER\n    | OUTPUT range_opt IDENTIFIERrange_opt : LSQUARE NUMBER COLON NUMBER RSQUARE\n    | emptyempty :module_items : module_item\n    | module_items module_itemmodule_item : wire_declaration\n    | assignmentwire_declaration : WIRE range_opt IDENTIFIER SEMIassignment : ASSIGN IDENTIFIER EQ expression SEMIexpression : expression PLUS expression\n    | expression MINUS expression\n    | expression TIMES expression\n    | expression DIVIDE expression\n    | expression AND expression\n    | expression OR expression\n    | expression EQEQ expression\n    | expression NEQ expression\n    | expression LT expression\n    | expression LE expression\n    | expression GT expression\n    | expression GE expression\n    | expression BITAND expression\n    | expression BITOR expression\n    | expression BITXOR expression\n    | expression LSHIFT expression\n    | expression RSHIFT expressionexpression : MINUS expression %prec NOT\n    | NOT expression\n    | BITNOT expressionexpression : LPAREN expression RPARENexpression : NUMBERexpression : IDENTIFIER'
    
_lr_action_items = {'MODULE':([0,],[2,]),'$end':([1,27,],[0,-1,]),'IDENTIFIER':([2,7,8,11,13,14,24,25,29,33,34,38,39,40,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[3,-8,-8,17,-7,19,-8,30,32,36,-6,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'LPAREN':([3,33,38,39,40,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[4,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'INPUT':([4,10,],[7,7,]),'OUTPUT':([4,10,],[8,8,]),'RPAREN':([5,6,16,17,19,36,42,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[9,-2,-3,-4,-5,-37,-36,-32,-33,-34,82,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-35,]),'COMMA':([5,6,16,17,19,],[10,-2,-3,-4,-5,]),'LSQUARE':([7,8,24,],[12,12,12,]),'SEMI':([9,32,36,37,42,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[15,35,-37,43,-36,-32,-33,-34,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-35,]),'NUMBER':([12,26,33,38,39,40,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[18,31,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'WIRE':([15,20,21,22,23,28,35,43,],[24,24,-9,-11,-12,-10,-13,-14,]),'ASSIGN':([15,20,21,22,23,28,35,43,],[25,25,-9,-11,-12,-10,-13,-14,]),'COLON':([18,],[26,]),'ENDMODULE':([20,21,22,23,28,35,43,],[27,-9,-11,-12,-10,-13,-14,]),'EQ':([30,],[33,]),'RSQUARE':([31,],[34,]),'MINUS':([33,36,37,38,39,40,41,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[38,-37,45,38,38,38,38,-36,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-32,-33,-34,45,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-35,]),'NOT':([33,38,39,40,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'BITNOT':([33,38,39,40,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'PLUS':([36,37,42,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-37,44,-36,-32,-33,-34,44,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-35,]),'TIMES':([36,37,42,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-37,46,-36,-32,-33,-34,46,46,46,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-35,]),'DIVIDE':([36,37,42,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-37,47,-36,-32,-33,-34,47,47,47,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-35,]),'AND':([36,37,42,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-37,48,-36,-32,-33,-34,48,48,48,48,48,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-35,]),'OR':([36,37,42,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-37,49,-36,-32,-33,-34,49,49,49,49,49,-19,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-35,]),'EQEQ':([36,37,42,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-37,50,-36,-32,-33,-34,50,50,50,50,50,50,50,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-35,]),'NEQ':([36,37,42,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-37,51,-36,-32,-33,-34,51,51,51,51,51,51,51,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-35,]),'LT':([36,37,42,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-37,52,-36,-32,-33,-34,52,52,52,52,52,52,52,52,52,-23,-24,-25,-26,-27,-28,-29,-30,-31,-35,]),'LE':([36,37,42,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-37,53,-36,-32,-33,-34,53,53,53,53,53,53,53,53,53,-23,-24,-25,-26,-27,-28,-29,-30,-31,-35,]),'GT':([36,37,42,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-37,54,-36,-32,-33,-34,54,54,54,54,54,54,54,54,54,-23,-24,-25,-26,-27,-28,-29,-30,-31,-35,]),'GE':([36,37,42,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-37,55,-36,-32,-33,-34,55,55,55,55,55,55,55,55,55,-23,-24,-25,-26,-27,-28,-29,-30,-31,-35,]),'BITAND':([36,37,42,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-37,56,-36,-32,-33,-34,56,56,56,56,56,56,56,56,56,56,56,56,56,-27,-28,-29,-30,-31,-35,]),'BITOR':([36,37,42,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-37,57,-36,-32,-33,-34,57,57,57,57,57,57,57,57,57,57,57,57,57,-27,-28,-29,-30,-31,-35,]),'BITXOR':([36,37,42,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-37,58,-36,-32,-33,-34,58,58,58,58,58,58,58,58,58,58,58,58,58,-27,-28,-29,-30,-31,-35,]),'LSHIFT':([36,37,42,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-37,59,-36,-32,-33,-34,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,-30,-31,-35,]),'RSHIFT':([36,37,42,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,],[-37,60,-36,-32,-33,-34,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,-30,-31,-35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'module':([0,],[1,]),'port_list':([4,],[5,]),'port':([4,10,],[6,16,]),'range_opt':([7,8,24,],[11,14,29,]),'empty':([7,8,24,],[13,13,13,]),'module_items':([15,],[20,]),'module_item':([15,20,],[21,28,]),'wire_declaration':([15,20,],[22,22,]),'assignment':([15,20,],[23,23,]),'expression':([33,38,39,40,41,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,],[37,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> module","S'",1,None,None,None),
  ('module -> MODULE IDENTIFIER LPAREN port_list RPAREN SEMI module_items ENDMODULE','module',8,'p_module','parser.py',49),
  ('port_list -> port','port_list',1,'p_port_list','parser.py',59),
  ('port_list -> port_list COMMA port','port_list',3,'p_port_list','parser.py',60),
  ('port -> INPUT range_opt IDENTIFIER','port',3,'p_port','parser.py',68),
  ('port -> OUTPUT range_opt IDENTIFIER','port',3,'p_port','parser.py',69),
  ('range_opt -> LSQUARE NUMBER COLON NUMBER RSQUARE','range_opt',5,'p_range_opt','parser.py',82),
  ('range_opt -> empty','range_opt',1,'p_range_opt','parser.py',83),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',91),
  ('module_items -> module_item','module_items',1,'p_module_items','parser.py',96),
  ('module_items -> module_items module_item','module_items',2,'p_module_items','parser.py',97),
  ('module_item -> wire_declaration','module_item',1,'p_module_item','parser.py',109),
  ('module_item -> assignment','module_item',1,'p_module_item','parser.py',110),
  ('wire_declaration -> WIRE range_opt IDENTIFIER SEMI','wire_declaration',4,'p_wire_declaration','parser.py',115),
  ('assignment -> ASSIGN IDENTIFIER EQ expression SEMI','assignment',5,'p_assignment','parser.py',127),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','parser.py',139),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','parser.py',140),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','parser.py',141),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','parser.py',142),
  ('expression -> expression AND expression','expression',3,'p_expression_binop','parser.py',143),
  ('expression -> expression OR expression','expression',3,'p_expression_binop','parser.py',144),
  ('expression -> expression EQEQ expression','expression',3,'p_expression_binop','parser.py',145),
  ('expression -> expression NEQ expression','expression',3,'p_expression_binop','parser.py',146),
  ('expression -> expression LT expression','expression',3,'p_expression_binop','parser.py',147),
  ('expression -> expression LE expression','expression',3,'p_expression_binop','parser.py',148),
  ('expression -> expression GT expression','expression',3,'p_expression_binop','parser.py',149),
  ('expression -> expression GE expression','expression',3,'p_expression_binop','parser.py',150),
  ('expression -> expression BITAND expression','expression',3,'p_expression_binop','parser.py',151),
  ('expression -> expression BITOR expression','expression',3,'p_expression_binop','parser.py',152),
  ('expression -> expression BITXOR expression','expression',3,'p_expression_binop','parser.py',153),
  ('expression -> expression LSHIFT expression','expression',3,'p_expression_binop','parser.py',154),
  ('expression -> expression RSHIFT expression','expression',3,'p_expression_binop','parser.py',155),
  ('expression -> MINUS expression','expression',2,'p_expression_unop','parser.py',173),
  ('expression -> NOT expression','expression',2,'p_expression_unop','parser.py',174),
  ('expression -> BITNOT expression','expression',2,'p_expression_unop','parser.py',175),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',191),
  ('expression -> NUMBER','expression',1,'p_expression_number','parser.py',196),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','parser.py',201),
]
