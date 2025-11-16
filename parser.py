import ply.lex as lex
import ply.yacc as yacc

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
    print(f"-> new section: [{current_section}]")


def p_statement_key_value(p):
    '''
    statement : ID EQUAL VALUE NEWLINE
    '''
    key = p[1]
    value = p[3]
    

    if current_section not in config:
        config[current_section] = {}
        
    config[current_section][key] = value
    print(f"   + add: {key} = {value} به [{current_section}]")


def p_statement_newline_only(p):
    '''
    statement : NEWLINE
    '''
    pass


def p_error(p):
    if p:
        print(f"error '{p.value}' in {p.lineno} line")
    else:
        print("error in the end of the input")

parser = yacc.yacc()