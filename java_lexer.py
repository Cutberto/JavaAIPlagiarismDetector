import re

# Definir las expresiones regulares pra cada tipo de token 
TOKEN_TYPES = [
    ('COMMENT_SINGLE', r'//.*'),
    ('COMMENT_MULTI', r'\/\*(.|[\r\n])*?\*\/'),
    ('KEYWORD', r'class|if|else|while|for'),
    ('IMPORT', r'import\s+[a-zA-Z_][a-zA-Z0-9_\.]*;'),
    ('SYSTEM_CALL', r'System[a-zA-Z_\.][a-zA-Z0-9_\.]*'),
    ('METHOD_CALL', r'(\.[\s\n\r]*[\w]+)[\s\n\r]*(?=\(.*\))'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('NUMBER', r'\d+(\.\d+)?'),
    ('STRING', r'"([^"\\]|\\.)*"'),
    ('OPERATOR', r'\+|\-|\*|/|%|=|==|!=|>|<|>=|<='),
    ('PUNCTUATION', r'\{|\}|\(|\)|\[|\]|\;|\,|\.'),
   # ('COMMENT_SINGLE', r'(?<=\n)//.*'),
    ('BOOLEAN', r'true|false'),
    ('NULL', r'null'),
    

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
                    self.tokens.append(token)
                    #el lexer avanza a la posición del source code donde termina el match
                    self.position = match.end(0)
                    break
            if not match:
                #si no hay match, se revisa si fue por un error o por un caracter que se puede ignorar
                if self.source_code[self.position] in [' ']:
                    # ignorar whitespace 
                    self.position += 1
                    self.lineposition += 1
                elif self.source_code[self.position] in ['\n', '\r']:
                    # ignorar salto de linea y cambiar de linea
                    self.position += 1
                    self.line += 1
                    self.lineposition = 0
                else:
                    # error por caracter erroneo 
                    raise Exception('Unexpected character trying '+ token_type+ ' at line '+ str(self.line) + " position: " + str(self.lineposition) + " char: " + self.source_code[self.position])

        return self.tokens

# Código de java para pruebas 
source_code = """
import java.util.ArrayList;
import java.util.List;

// This is a single-line comment
class HelloWorld {
    public static void main(String[] args) {
        /* This is a
           multi-line comment */
        boolean flag = true;
        String message = "Hello, World!";
        int number = 123;
        double pi = 3.14;
        int[] array = {1, 2, 3};
        if (flag == true) {
            System.out.println(message);
        }
        else {
            System.out.println("Flag is false.");
        }
    }
}

"""

# Validar si vale la pena quitar los comentarios o dejarlos, en base a los papers
#source_code = re.sub(r'/\*.*?\*/', '', source_code, flags=re.DOTALL)
print(source_code)

# Mandar a llamar el lexer
lexer = Lexer(source_code)
tokens = lexer.tokenize()

# Imprimir el resultado
for token in tokens:
    print(token.type + ':', token.value)
