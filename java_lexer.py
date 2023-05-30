import re

# Definir las expresiones regulares pra cada tipo de token 
TOKEN_TYPES = [
    ('COMMENT_SINGLE', r'//.*'),
    ('COMMENT_MULTI', r'\/\*(.|[\r\n])*?\*\/'),
    ('IMPORT', r'import\s+[a-zA-Z_][a-zA-Z0-9_\.]*;'),
    ('KEYWORD', r'\b(?:abstract|assert|break|case|catch|class|const|continue|default|do|else|enum|exports|extends|final|finally|for|if|implements|instanceof|interface|module|native|new|open|opens|package|private|protected|provides|public|requires|return|static|strictfp|super|switch|synchronized|this|throw|throws|transient|try|exports|volatile|while|with)\b'),
    ('DATA_TYPE', r'\b(?:boolean|byte|char|double|float|int|long|short|void)\b'),
    ('SYSTEM_CALL', r'System[a-zA-Z_\.][a-zA-Z0-9_\.]*'),
    ('METHOD_CALL', r'(\.[\s\n\r]*[\w]+)[\s\n\r]*(?=\(.*\))'),
    ('NULL', r'null'),
    ('BOOLEAN', r'true|false'),
    ('NUMBER', r'\d+(\.\d+)?'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('STRING', r'"([^"\\]|\\.)*"'),
    ('STRING2', r'\'([^"\\]|\\.)*\''),
    ('OPERATOR', r'\!=|[++]|[--]|\-|[+=]|-=|[*=]|/=|%=|&=|[|=]|>>=|<<=|\*|/|%|=|==|>=|<=|>|<|!|&&|[||]|^=|[+]|\?|\:|\&|\@|\^|\~'),
    ('PUNCTUATION', r'\{|\}|\(|\)|\[|\]|\;|\,|\.|:|\\'),
    ('WHITESPACE', r'\s'),
   # ('COMMENT_SINGLE', r'(?<=\n)//.*'),
    

]

# Clase token, cuenta con tipo y valor
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

#clase lexer, cuenta con codigo fuente, posición y tokens analizados 
class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.lineposition = 0
        self.line = 0
        self.tokens = []

    # Metodo tokenize, hace el analisis posicion por posicion y va bucando matches con las regex
    # esta configurado para ignorar ciertos caracteres que no haran match 
    def tokenize(self):
        while self.position < len(self.source_code):
            match = None
            for token_type, pattern in TOKEN_TYPES:
                regex = re.compile(pattern)
                match = regex.match(self.source_code, self.position)
                if match:
                    #recupera el valor del token de la instancia re.match
                    value = match.group(0)
                    #crea un objeto token 
                    token = Token(token_type, value)
                    #lo almacena en la clase lexer
                    if token.type != "WHITESPACE" : self.tokens.append(token)
                    #el lexer avanza a la posición del source code donde termina el match
                    self.position = match.end(0)
                    break
            if not match:
                #si no hay match, se revisa si fue por un error o por un caracter que se puede ignorar
                if self.source_code[self.position] in [' ']:
                    # ignorar whitespace 
                    self.position += 1
                    self.lineposition += 1
                elif self.source_code[self.position] in ['\n', '\r', "\r\n" ]:
                    # ignorar salto de linea y cambiar de linea
                    self.position += 1
                    self.line += 1
                    self.lineposition = 0
                else:
                    # error por caracter erroneo 
                    print ('Unexpected character trying '+ token_type+ ' at line '+ str(self.line) + " position: " + str(self.lineposition) + " char: " + self.source_code[self.position])
                    #self.position +=1
                    raise Exception('Unexpected character trying '+ token_type+ ' at line '+ str(self.line) + " position: " + str(self.lineposition) + " char: " + self.source_code[self.position])

        return self.tokens


# Documentacion: https://interactivechaos.com/en/python/function/redotall
# Probar regex: https://regexr.com/