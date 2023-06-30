from antlr4 import *

from rulesLexer import * 
from rulesParser import *
from rulesListener import *

input_stream = FileStream('input.txt')
lexer = rulesLexer(input_stream)
tokens_stream = CommonTokenStream(lexer)
parser = rulesParser(tokens_stream)
tree = parser.function()
listener = rulesListener()
walker = ParseTreeWalker()
walker.walk(listener, tree)
print(tree)