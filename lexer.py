import ply.lex as lex

reserved = {
    'cuando': 'CUANDO',
    'deotro': 'DEOTRO',
    'durante': 'DURANTE',
    'decir': 'DECIR',
    'verdadero': 'TRUE',
    'falso': 'FALSE',
    'y': 'AND',
    'o': 'OR',
    'no': 'NOT'
}

tokens = [
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LESS', 'GREATER', 'EQUAL', 'NOTEQUAL',
    'ASSIGN', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',
    'SEMICOLON', 'COMMA', 'ID', 'NUMBER', 'FLOAT', 'STRING',
    'CUANDO', 'DEOTRO', 'DURANTE', 'DECIR',
    'TRUE', 'FALSE', 'AND', 'OR', 'NOT'
]

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LESS = r'<'
t_GREATER = r'>'
t_EQUAL = r'=='
t_NOTEQUAL = r'!='
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_COMMA = r','

t_ignore = ' \t'

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1]
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Error léxico: '{t.value[0]}' en línea {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()