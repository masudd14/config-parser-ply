import ply.lex as lex
import ply.yacc as yacc


tokens = (
    'LBRACKET',   
    'RBRACKET',  
    'EQUAL',      
    'ID',         
    'VALUE',      
    'NEWLINE'     
)


t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_EQUAL    = r'='


t_ignore_COMMENT = r'\#.*'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_\-]*'
  
    return t


def t_VALUE(t):
    
    r'[^=\[\]\n\r\#]+' 
    t.value = t.value.strip() 
    return t


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

t_ignore = ' \t' 

def t_error(t):
    print(f"error Lexer: unsuported charcter '{t.value[0]}' in {t.lexer.lineno} line")
    t.lexer.skip(1)

lexer = lex.lex()