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
    print(f"خطای Lexer: کاراکتر غیرمجاز '{t.value[0]}' در خط {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()
#--------------------------------------------------------------------------------------------------------------

config = {}
current_section = "GLOBAL" 

def p_program(p):
    '''
    program : statements
    '''
    p[0] = config


def p_statements_list(p):
    '''
    statements : statement
               | statements statement
    '''
    pass


def p_statement_section(p):
    '''
    statement : LBRACKET ID RBRACKET NEWLINE
    '''
    global current_section
    current_section = p[2]
    config[current_section] = {}
    print(f"-> بخش جدید: [{current_section}]")


def p_statement_key_value(p):
    '''
    statement : ID EQUAL VALUE NEWLINE
    '''
    key = p[1]
    value = p[3]
    

    if current_section not in config:
        config[current_section] = {}
        
    config[current_section][key] = value
    print(f"   + افزودن: {key} = {value} به [{current_section}]")


def p_statement_newline_only(p):
    '''
    statement : NEWLINE
    '''
    pass


def p_error(p):
    if p:
        print(f"خطای نحوی: توکن غیرمنتظره '{p.value}' در خط {p.lineno}")
    else:
        print("خطای نحوی در انتهای ورودی")

parser = yacc.yacc()
#-------------------------------------------------------------------------------------------------------------------------
# --- ۳. Main Execution ---

if __name__ == '__main__':
    config_code = """
app_name = MyService # این یک تنظیمات سراسری (Global) است

[Database]
host = 127.0.0.1
port = 5432
user = admin

[Logging]
level = DEBUG
file_path = /var/log/app.log
# این یک کامنت است

"""
    print("--- شروع تحلیل فایل پیکربندی ---")
    

    config.clear()
    current_section = "GLOBAL"
    config[current_section] = {}
    
    result = parser.parse(config_code)
    
    print("\n--- نتیجه نهایی دیکشنری پیکربندی ---")
    import json
    print(json.dumps(result, indent=4))