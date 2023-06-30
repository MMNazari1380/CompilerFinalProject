from antlr4 import *

from rulesLexer import * 
from rulesParser import *
from rulesListener import *
from rulesParser import rulesParser

class rulesListenrFirst(rulesListener):
    def __init__(self):
        self.code = ""
        self.temp_count = 0

        self.ar = {}
    
    def enterProgram(self, ctx: ProgramContext):
        self.code += \
        """#include <stdio.h>
        #define printInt(k) printf(\"%d\\n\", k)
        #define printDouble(x) printf(\"%f\\n\", x)
        #define printString(t) printf(\"%s\\n\", t)
        int readInt() {
            int x;
            scanf(\"%d\", &x);
            return x;
        }
        double readDouble() {
            double x;
            scanf(\"%lf\", &x);
            return x;
        }
        union cell {
            int i;
            double d;
            void* l;
        };
        union cell m[1000000];
        int top = 0;"""
        self.enterFunctions(ctx)
    
    def exitProgram(self, ctx: ProgramContext):
        with open('run.out', 'w') as f:
            f.write(self.code)
    
    def enterFunctions(self, ctx: FunctionsContext):
        # functions -> function functions | function
        self.enterFunction(ctx.getChild(0))
        if ctx.getChildCount() > 1:
            self.enterFunctions(ctx.getChild(1))
    
    def exitFunctions(self, ctx: FunctionsContext):
        return super().exitFunctions(ctx)

    def enterFunction(self, ctx: FunctionContext):
        self.enterType(ctx.getChild(0))
        


