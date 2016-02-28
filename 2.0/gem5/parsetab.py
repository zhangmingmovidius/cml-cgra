
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '-\xf8\x04\xb3\xc1\x84/ vH\xdd\x92\xb7tl\xac'
    
_lr_action_items = {'FORMAT':([4,82,101,106,124,137,138,149,151,],[23,103,103,-50,-45,103,-53,-54,-51,]),'OPERAND_TYPES':([4,],[26,]),'LBRACKET':([79,94,99,130,131,132,134,],[94,94,94,94,94,94,94,]),'CODELIT':([15,22,26,30,31,32,38,76,79,94,99,130,131,132,134,],[29,36,39,41,42,43,50,88,95,95,95,95,95,95,95,]),'INTLIT':([56,79,82,84,94,99,101,106,122,124,130,131,132,134,137,138,149,151,],[72,96,107,109,96,96,107,-50,136,-45,96,96,96,96,107,-53,-54,-51,]),'DEF':([0,1,3,5,7,8,10,11,12,13,14,17,18,20,28,40,44,48,51,52,53,54,68,73,108,110,140,],[4,-15,-5,-7,-11,-8,-16,4,-13,-12,-9,-14,-10,4,-6,-20,-2,-22,-21,-19,-17,-18,-30,-25,-24,-31,-23,]),'STRLIT':([79,94,99,130,131,132,134,],[92,92,92,92,92,92,92,]),'RPAREN':([49,59,60,62,63,64,65,66,67,77,86,87,89,90,92,93,95,96,97,99,115,116,117,118,119,120,121,129,131,142,143,144,145,147,],[-78,-33,76,-40,-35,-34,-41,-39,-36,-44,-32,-37,-38,-42,-72,-43,-73,-71,-70,-78,-65,-67,-62,-63,-70,-64,135,-74,-78,150,-66,-61,-68,-69,]),'SEMI':([29,33,36,39,41,42,43,50,57,58,83,85,88,128,135,139,150,],[40,44,48,51,52,53,54,68,73,-26,108,-27,110,140,-59,149,-60,]),'LESS':([47,],[56,]),'DECODE':([1,3,5,7,8,9,10,11,12,13,14,17,18,20,28,34,40,44,48,51,52,53,54,68,73,108,110,127,140,],[-15,-5,-7,-11,-8,-3,-16,-4,-13,-12,-9,-14,-10,-78,-6,46,-20,-2,-22,-21,-19,-17,-18,-30,-25,-24,-31,46,-23,]),'DEFAULT':([55,82,101,106,124,137,138,149,151,],[69,104,104,-50,-45,104,-53,-54,-51,]),'COMMA':([49,59,63,65,66,67,87,90,92,93,94,95,96,97,99,100,107,111,112,113,115,116,117,118,119,120,129,131,136,141,143,144,145,147,],[-78,75,-35,-41,78,-36,-37,-42,-72,-43,-78,-73,-71,-70,-78,122,-57,130,-75,-77,-65,-67,132,133,-70,-64,-74,-78,-58,-76,-66,133,-68,-69,]),'DOT':([58,],[74,]),'COLON':([72,100,104,105,107,136,],[84,-55,-56,127,-57,-58,]),'$end':([6,45,124,],[0,-1,-45,]),'RBRACE':([101,102,106,123,124,138,148,149,151,],[-48,124,-50,-49,-45,-53,151,-54,-51,]),'EXEC':([16,],[30,]),'ASTERISK':([49,75,78,],[61,61,61,]),'NAMESPACE':([0,1,2,3,5,7,8,9,10,11,12,13,14,17,18,28,40,48,51,52,53,54,68,73,108,110,140,],[-78,-15,19,-5,-7,-11,-8,-3,-16,-4,-13,-12,-9,-14,-10,-6,-20,-22,-21,-19,-17,-18,-30,-25,-24,-31,-23,]),'EQUALS':([67,87,91,119,146,],[79,79,79,134,134,]),'CPPDIRECTIVE':([82,101,106,124,137,138,149,151,],[106,106,-50,-45,106,-53,-54,-51,]),'BITFIELD':([4,21,25,27,],[-78,35,-28,-29,]),'HEADER':([16,],[31,]),'DBLCOLON':([81,],[98,]),'LPAREN':([37,81,114,],[49,99,131,]),'ID':([19,23,24,35,46,47,49,61,69,74,75,78,79,94,98,99,103,127,130,131,132,133,134,],[33,37,38,47,55,58,67,77,81,58,87,91,97,97,114,119,126,81,97,119,119,146,97,]),'GREATER':([72,109,],[83,128,]),'LBRACE':([55,70,71,80,125,126,135,150,],[-78,-46,82,-47,137,-52,-59,-60,]),'OPERANDS':([4,],[22,]),'SIGNED':([4,],[25,]),'LET':([0,1,3,5,7,8,10,11,12,13,14,17,18,20,28,40,44,48,51,52,53,54,68,73,108,110,140,],[15,-15,-5,-7,-11,-8,-16,15,-13,-12,-9,-14,-10,15,-6,-20,-2,-22,-21,-19,-17,-18,-30,-25,-24,-31,-23,]),'TEMPLATE':([4,],[24,]),'DECODER':([16,],[32,]),'OUTPUT':([0,1,3,5,7,8,10,11,12,13,14,17,18,20,28,40,44,48,51,52,53,54,68,73,108,110,140,],[16,-15,-5,-7,-11,-8,-16,16,-13,-12,-9,-14,-10,16,-6,-20,-2,-22,-21,-19,-17,-18,-30,-25,-24,-31,-23,]),'RBRACKET':([92,94,95,96,97,111,112,113,129,141,],[-72,-78,-73,-71,-70,129,-75,-77,-74,-76,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'list_expr':([94,],[111,]),'decode_block':([34,127,],[45,138,]),'param_list':([49,],[60,]),'output_exec':([0,11,20,],[1,1,1,]),'opt_defs_and_outputs':([0,20,],[2,34,]),'def_or_output':([0,11,20,],[3,28,3,]),'push_format_id':([103,],[125,]),'keyword_param':([49,75,78,],[65,65,90,]),'case_label':([82,101,137,],[105,105,105,]),'def_format':([0,11,20,],[5,5,5,]),'positional_arg_list':([99,131,],[117,117,]),'def_template':([0,11,20,],[18,18,18,]),'def_operand_types':([0,11,20,],[7,7,7,]),'excess_args_param':([49,75,78,],[62,62,89,]),'name_decl':([2,],[20,]),'def_bitfield':([0,11,20,],[8,8,8,]),'keyword_param_list':([49,75,],[66,66,]),'empty':([0,4,20,49,55,94,99,131,],[9,27,9,63,70,113,120,120,]),'arg_list':([99,131,],[121,142,]),'opt_signed':([4,],[21,]),'decode_stmt_list':([82,101,137,],[102,123,148,]),'global_let':([0,11,20,],[10,10,10,]),'positional_param_list':([49,],[59,]),'defs_and_outputs':([0,20,],[11,11,]),'keyword_arg':([99,131,132,133,],[116,116,116,145,]),'output_header':([0,11,20,],[12,12,12,]),'inst':([69,127,],[80,139,]),'nonpositional_param_list':([49,75,],[64,86,]),'def_operands':([0,11,20,],[13,13,13,]),'intlit_list':([82,101,137,],[100,100,100,]),'expr':([79,94,99,130,131,132,134,],[93,112,115,141,115,143,147,]),'id_with_dot':([47,74,],[57,85,]),'decode_stmt':([82,101,137,],[101,101,101,]),'def_bitfield_struct':([0,11,20,],[14,14,14,]),'keyword_arg_list':([99,131,132,],[118,118,144,]),'opt_default':([55,],[71,]),'output_decoder':([0,11,20,],[17,17,17,]),'specification':([0,],[6,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> specification","S'",1,None,None,None),
  ('specification -> opt_defs_and_outputs name_decl opt_defs_and_outputs decode_block','specification',4,'p_specification','/home/shail/gem5/src/arch/isa_parser.py',1420),
  ('name_decl -> NAMESPACE ID SEMI','name_decl',3,'p_name_decl','/home/shail/gem5/src/arch/isa_parser.py',1439),
  ('opt_defs_and_outputs -> empty','opt_defs_and_outputs',1,'p_opt_defs_and_outputs_0','/home/shail/gem5/src/arch/isa_parser.py',1445),
  ('opt_defs_and_outputs -> defs_and_outputs','opt_defs_and_outputs',1,'p_opt_defs_and_outputs_1','/home/shail/gem5/src/arch/isa_parser.py',1449),
  ('defs_and_outputs -> def_or_output','defs_and_outputs',1,'p_defs_and_outputs_0','/home/shail/gem5/src/arch/isa_parser.py',1453),
  ('defs_and_outputs -> defs_and_outputs def_or_output','defs_and_outputs',2,'p_defs_and_outputs_1','/home/shail/gem5/src/arch/isa_parser.py',1457),
  ('def_or_output -> def_format','def_or_output',1,'p_def_or_output','/home/shail/gem5/src/arch/isa_parser.py',1462),
  ('def_or_output -> def_bitfield','def_or_output',1,'p_def_or_output','/home/shail/gem5/src/arch/isa_parser.py',1463),
  ('def_or_output -> def_bitfield_struct','def_or_output',1,'p_def_or_output','/home/shail/gem5/src/arch/isa_parser.py',1464),
  ('def_or_output -> def_template','def_or_output',1,'p_def_or_output','/home/shail/gem5/src/arch/isa_parser.py',1465),
  ('def_or_output -> def_operand_types','def_or_output',1,'p_def_or_output','/home/shail/gem5/src/arch/isa_parser.py',1466),
  ('def_or_output -> def_operands','def_or_output',1,'p_def_or_output','/home/shail/gem5/src/arch/isa_parser.py',1467),
  ('def_or_output -> output_header','def_or_output',1,'p_def_or_output','/home/shail/gem5/src/arch/isa_parser.py',1468),
  ('def_or_output -> output_decoder','def_or_output',1,'p_def_or_output','/home/shail/gem5/src/arch/isa_parser.py',1469),
  ('def_or_output -> output_exec','def_or_output',1,'p_def_or_output','/home/shail/gem5/src/arch/isa_parser.py',1470),
  ('def_or_output -> global_let','def_or_output',1,'p_def_or_output','/home/shail/gem5/src/arch/isa_parser.py',1471),
  ('output_header -> OUTPUT HEADER CODELIT SEMI','output_header',4,'p_output_header','/home/shail/gem5/src/arch/isa_parser.py',1489),
  ('output_decoder -> OUTPUT DECODER CODELIT SEMI','output_decoder',4,'p_output_decoder','/home/shail/gem5/src/arch/isa_parser.py',1493),
  ('output_exec -> OUTPUT EXEC CODELIT SEMI','output_exec',4,'p_output_exec','/home/shail/gem5/src/arch/isa_parser.py',1497),
  ('global_let -> LET CODELIT SEMI','global_let',3,'p_global_let','/home/shail/gem5/src/arch/isa_parser.py',1505),
  ('def_operand_types -> DEF OPERAND_TYPES CODELIT SEMI','def_operand_types',4,'p_def_operand_types','/home/shail/gem5/src/arch/isa_parser.py',1526),
  ('def_operands -> DEF OPERANDS CODELIT SEMI','def_operands',4,'p_def_operands','/home/shail/gem5/src/arch/isa_parser.py',1539),
  ('def_bitfield -> DEF opt_signed BITFIELD ID LESS INTLIT COLON INTLIT GREATER SEMI','def_bitfield',10,'p_def_bitfield_0','/home/shail/gem5/src/arch/isa_parser.py',1555),
  ('def_bitfield -> DEF opt_signed BITFIELD ID LESS INTLIT GREATER SEMI','def_bitfield',8,'p_def_bitfield_1','/home/shail/gem5/src/arch/isa_parser.py',1564),
  ('def_bitfield_struct -> DEF opt_signed BITFIELD ID id_with_dot SEMI','def_bitfield_struct',6,'p_def_bitfield_struct','/home/shail/gem5/src/arch/isa_parser.py',1573),
  ('id_with_dot -> ID','id_with_dot',1,'p_id_with_dot_0','/home/shail/gem5/src/arch/isa_parser.py',1581),
  ('id_with_dot -> ID DOT id_with_dot','id_with_dot',3,'p_id_with_dot_1','/home/shail/gem5/src/arch/isa_parser.py',1585),
  ('opt_signed -> SIGNED','opt_signed',1,'p_opt_signed_0','/home/shail/gem5/src/arch/isa_parser.py',1589),
  ('opt_signed -> empty','opt_signed',1,'p_opt_signed_1','/home/shail/gem5/src/arch/isa_parser.py',1593),
  ('def_template -> DEF TEMPLATE ID CODELIT SEMI','def_template',5,'p_def_template','/home/shail/gem5/src/arch/isa_parser.py',1597),
  ('def_format -> DEF FORMAT ID LPAREN param_list RPAREN CODELIT SEMI','def_format',8,'p_def_format','/home/shail/gem5/src/arch/isa_parser.py',1604),
  ('param_list -> positional_param_list COMMA nonpositional_param_list','param_list',3,'p_param_list_0','/home/shail/gem5/src/arch/isa_parser.py',1624),
  ('param_list -> positional_param_list','param_list',1,'p_param_list_1','/home/shail/gem5/src/arch/isa_parser.py',1628),
  ('param_list -> nonpositional_param_list','param_list',1,'p_param_list_1','/home/shail/gem5/src/arch/isa_parser.py',1629),
  ('positional_param_list -> empty','positional_param_list',1,'p_positional_param_list_0','/home/shail/gem5/src/arch/isa_parser.py',1633),
  ('positional_param_list -> ID','positional_param_list',1,'p_positional_param_list_1','/home/shail/gem5/src/arch/isa_parser.py',1637),
  ('positional_param_list -> positional_param_list COMMA ID','positional_param_list',3,'p_positional_param_list_2','/home/shail/gem5/src/arch/isa_parser.py',1641),
  ('nonpositional_param_list -> keyword_param_list COMMA excess_args_param','nonpositional_param_list',3,'p_nonpositional_param_list_0','/home/shail/gem5/src/arch/isa_parser.py',1645),
  ('nonpositional_param_list -> keyword_param_list','nonpositional_param_list',1,'p_nonpositional_param_list_1','/home/shail/gem5/src/arch/isa_parser.py',1649),
  ('nonpositional_param_list -> excess_args_param','nonpositional_param_list',1,'p_nonpositional_param_list_1','/home/shail/gem5/src/arch/isa_parser.py',1650),
  ('keyword_param_list -> keyword_param','keyword_param_list',1,'p_keyword_param_list_0','/home/shail/gem5/src/arch/isa_parser.py',1654),
  ('keyword_param_list -> keyword_param_list COMMA keyword_param','keyword_param_list',3,'p_keyword_param_list_1','/home/shail/gem5/src/arch/isa_parser.py',1658),
  ('keyword_param -> ID EQUALS expr','keyword_param',3,'p_keyword_param','/home/shail/gem5/src/arch/isa_parser.py',1662),
  ('excess_args_param -> ASTERISK ID','excess_args_param',2,'p_excess_args_param','/home/shail/gem5/src/arch/isa_parser.py',1666),
  ('decode_block -> DECODE ID opt_default LBRACE decode_stmt_list RBRACE','decode_block',6,'p_decode_block','/home/shail/gem5/src/arch/isa_parser.py',1679),
  ('opt_default -> empty','opt_default',1,'p_opt_default_0','/home/shail/gem5/src/arch/isa_parser.py',1694),
  ('opt_default -> DEFAULT inst','opt_default',2,'p_opt_default_1','/home/shail/gem5/src/arch/isa_parser.py',1702),
  ('decode_stmt_list -> decode_stmt','decode_stmt_list',1,'p_decode_stmt_list_0','/home/shail/gem5/src/arch/isa_parser.py',1711),
  ('decode_stmt_list -> decode_stmt decode_stmt_list','decode_stmt_list',2,'p_decode_stmt_list_1','/home/shail/gem5/src/arch/isa_parser.py',1715),
  ('decode_stmt -> CPPDIRECTIVE','decode_stmt',1,'p_decode_stmt_cpp','/home/shail/gem5/src/arch/isa_parser.py',1738),
  ('decode_stmt -> FORMAT push_format_id LBRACE decode_stmt_list RBRACE','decode_stmt',5,'p_decode_stmt_format','/home/shail/gem5/src/arch/isa_parser.py',1747),
  ('push_format_id -> ID','push_format_id',1,'p_push_format_id','/home/shail/gem5/src/arch/isa_parser.py',1759),
  ('decode_stmt -> case_label COLON decode_block','decode_stmt',3,'p_decode_stmt_decode','/home/shail/gem5/src/arch/isa_parser.py',1769),
  ('decode_stmt -> case_label COLON inst SEMI','decode_stmt',4,'p_decode_stmt_inst','/home/shail/gem5/src/arch/isa_parser.py',1780),
  ('case_label -> intlit_list','case_label',1,'p_case_label_0','/home/shail/gem5/src/arch/isa_parser.py',1790),
  ('case_label -> DEFAULT','case_label',1,'p_case_label_1','/home/shail/gem5/src/arch/isa_parser.py',1799),
  ('intlit_list -> INTLIT','intlit_list',1,'p_intlit_list_0','/home/shail/gem5/src/arch/isa_parser.py',1807),
  ('intlit_list -> intlit_list COMMA INTLIT','intlit_list',3,'p_intlit_list_1','/home/shail/gem5/src/arch/isa_parser.py',1811),
  ('inst -> ID LPAREN arg_list RPAREN','inst',4,'p_inst_0','/home/shail/gem5/src/arch/isa_parser.py',1819),
  ('inst -> ID DBLCOLON ID LPAREN arg_list RPAREN','inst',6,'p_inst_1','/home/shail/gem5/src/arch/isa_parser.py',1833),
  ('arg_list -> positional_arg_list COMMA keyword_arg_list','arg_list',3,'p_arg_list_0','/home/shail/gem5/src/arch/isa_parser.py',1848),
  ('arg_list -> positional_arg_list','arg_list',1,'p_arg_list_1','/home/shail/gem5/src/arch/isa_parser.py',1852),
  ('arg_list -> keyword_arg_list','arg_list',1,'p_arg_list_2','/home/shail/gem5/src/arch/isa_parser.py',1856),
  ('positional_arg_list -> empty','positional_arg_list',1,'p_positional_arg_list_0','/home/shail/gem5/src/arch/isa_parser.py',1860),
  ('positional_arg_list -> expr','positional_arg_list',1,'p_positional_arg_list_1','/home/shail/gem5/src/arch/isa_parser.py',1864),
  ('positional_arg_list -> positional_arg_list COMMA expr','positional_arg_list',3,'p_positional_arg_list_2','/home/shail/gem5/src/arch/isa_parser.py',1868),
  ('keyword_arg_list -> keyword_arg','keyword_arg_list',1,'p_keyword_arg_list_0','/home/shail/gem5/src/arch/isa_parser.py',1872),
  ('keyword_arg_list -> keyword_arg_list COMMA keyword_arg','keyword_arg_list',3,'p_keyword_arg_list_1','/home/shail/gem5/src/arch/isa_parser.py',1876),
  ('keyword_arg -> ID EQUALS expr','keyword_arg',3,'p_keyword_arg','/home/shail/gem5/src/arch/isa_parser.py',1881),
  ('expr -> ID','expr',1,'p_expr_0','/home/shail/gem5/src/arch/isa_parser.py',1896),
  ('expr -> INTLIT','expr',1,'p_expr_0','/home/shail/gem5/src/arch/isa_parser.py',1897),
  ('expr -> STRLIT','expr',1,'p_expr_0','/home/shail/gem5/src/arch/isa_parser.py',1898),
  ('expr -> CODELIT','expr',1,'p_expr_0','/home/shail/gem5/src/arch/isa_parser.py',1899),
  ('expr -> LBRACKET list_expr RBRACKET','expr',3,'p_expr_1','/home/shail/gem5/src/arch/isa_parser.py',1903),
  ('list_expr -> expr','list_expr',1,'p_list_expr_0','/home/shail/gem5/src/arch/isa_parser.py',1907),
  ('list_expr -> list_expr COMMA expr','list_expr',3,'p_list_expr_1','/home/shail/gem5/src/arch/isa_parser.py',1911),
  ('list_expr -> empty','list_expr',1,'p_list_expr_2','/home/shail/gem5/src/arch/isa_parser.py',1915),
  ('empty -> <empty>','empty',0,'p_empty','/home/shail/gem5/src/arch/isa_parser.py',1922),
]