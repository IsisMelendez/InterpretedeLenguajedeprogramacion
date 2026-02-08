import ply.yacc as yacc
from lexer import tokens, lexer

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('nonassoc', 'LESS', 'GREATER', 'EQUAL', 'NOTEQUAL'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_program(p):
    'program : statements'
    p[0] = p[1]

def p_statements(p):
    '''statements : statement
                  | statements statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : assignment
                 | print_stmt
                 | if_stmt
                 | while_stmt'''
    p[0] = p[1]

def p_assignment(p):
    'assignment : ID ASSIGN expression SEMICOLON'
    p[0] = ('assign', p[1], p[3])

def p_print_stmt(p):
    'print_stmt : DECIR LPAREN expression RPAREN SEMICOLON'
    p[0] = ('print', p[3])

def p_if_stmt(p):
    '''if_stmt : CUANDO LPAREN expression RPAREN LBRACE statements RBRACE
               | CUANDO LPAREN expression RPAREN LBRACE statements RBRACE DEOTRO LBRACE statements RBRACE'''
    if len(p) == 8:
        p[0] = ('if', p[3], p[6], [])
    else:
        p[0] = ('if', p[3], p[6], p[10])

def p_while_stmt(p):
    'while_stmt : DURANTE LPAREN expression RPAREN LBRACE statements RBRACE'
    p[0] = ('while', p[3], p[6])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression LESS expression
                  | expression GREATER expression
                  | expression EQUAL expression
                  | expression NOTEQUAL expression
                  | expression AND expression
                  | expression OR expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_not(p):
    'expression : NOT expression'
    p[0] = ('not', p[2])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER
                  | FLOAT'''
    p[0] = ('number', p[1])

def p_expression_string(p):
    'expression : STRING'
    p[0] = ('string', p[1])

def p_expression_bool(p):
    '''expression : TRUE
                  | FALSE'''
    p[0] = ('bool', True if p[1] == 'verdadero' else False)

def p_expression_id(p):
    'expression : ID'
    p[0] = ('id', p[1])

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}' (línea {p.lineno})")
    else:
        print("Error de sintaxis: fin de archivo inesperado")

parser = yacc.yacc()

def parse(data):
    return parser.parse(data, lexer=lexer)