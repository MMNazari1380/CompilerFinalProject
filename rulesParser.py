# Generated from rules.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,44,183,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,1,1,1,1,1,1,1,3,1,39,8,1,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,54,8,2,1,3,1,3,1,3,
        1,3,1,3,3,3,61,8,3,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,
        7,1,7,3,7,76,8,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,
        121,8,9,1,10,1,10,1,10,1,10,1,10,5,10,128,8,10,10,10,12,10,131,9,
        10,1,11,1,11,1,11,1,11,3,11,137,8,11,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,3,12,161,8,12,1,12,1,12,1,12,1,12,5,12,167,8,12,
        10,12,12,12,170,9,12,1,13,1,13,1,13,1,13,1,13,3,13,177,8,13,1,14,
        1,14,1,15,1,15,1,15,0,2,20,24,16,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,0,3,1,0,5,8,1,0,15,16,2,0,15,15,17,28,194,0,32,1,0,0,
        0,2,38,1,0,0,0,4,53,1,0,0,0,6,60,1,0,0,0,8,62,1,0,0,0,10,65,1,0,
        0,0,12,67,1,0,0,0,14,75,1,0,0,0,16,77,1,0,0,0,18,120,1,0,0,0,20,
        122,1,0,0,0,22,136,1,0,0,0,24,160,1,0,0,0,26,176,1,0,0,0,28,178,
        1,0,0,0,30,180,1,0,0,0,32,33,3,2,1,0,33,1,1,0,0,0,34,35,3,4,2,0,
        35,36,3,2,1,0,36,39,1,0,0,0,37,39,3,4,2,0,38,34,1,0,0,0,38,37,1,
        0,0,0,39,3,1,0,0,0,40,41,3,10,5,0,41,42,5,38,0,0,42,43,5,32,0,0,
        43,44,3,6,3,0,44,45,5,33,0,0,45,46,3,12,6,0,46,54,1,0,0,0,47,48,
        3,10,5,0,48,49,5,38,0,0,49,50,5,32,0,0,50,51,5,33,0,0,51,52,3,12,
        6,0,52,54,1,0,0,0,53,40,1,0,0,0,53,47,1,0,0,0,54,5,1,0,0,0,55,56,
        3,8,4,0,56,57,5,37,0,0,57,58,3,6,3,0,58,61,1,0,0,0,59,61,3,8,4,0,
        60,55,1,0,0,0,60,59,1,0,0,0,61,7,1,0,0,0,62,63,3,10,5,0,63,64,5,
        38,0,0,64,9,1,0,0,0,65,66,7,0,0,0,66,11,1,0,0,0,67,68,5,30,0,0,68,
        69,3,14,7,0,69,70,5,31,0,0,70,13,1,0,0,0,71,72,3,18,9,0,72,73,3,
        14,7,0,73,76,1,0,0,0,74,76,3,16,8,0,75,71,1,0,0,0,75,74,1,0,0,0,
        76,15,1,0,0,0,77,78,1,0,0,0,78,17,1,0,0,0,79,121,5,34,0,0,80,121,
        3,12,6,0,81,82,3,10,5,0,82,83,3,20,10,0,83,121,1,0,0,0,84,85,5,38,
        0,0,85,86,5,36,0,0,86,121,3,24,12,0,87,88,5,38,0,0,88,121,5,13,0,
        0,89,90,5,38,0,0,90,121,5,14,0,0,91,92,5,9,0,0,92,121,5,34,0,0,93,
        94,5,9,0,0,94,95,3,24,12,0,95,96,5,34,0,0,96,121,1,0,0,0,97,98,5,
        10,0,0,98,99,5,32,0,0,99,100,3,24,12,0,100,101,5,33,0,0,101,102,
        3,18,9,0,102,121,1,0,0,0,103,104,5,10,0,0,104,105,5,32,0,0,105,106,
        3,24,12,0,106,107,5,33,0,0,107,108,3,18,9,0,108,109,5,11,0,0,109,
        110,3,18,9,0,110,121,1,0,0,0,111,112,5,12,0,0,112,113,5,32,0,0,113,
        114,3,24,12,0,114,115,5,33,0,0,115,116,3,18,9,0,116,121,1,0,0,0,
        117,118,3,24,12,0,118,119,5,34,0,0,119,121,1,0,0,0,120,79,1,0,0,
        0,120,80,1,0,0,0,120,81,1,0,0,0,120,84,1,0,0,0,120,87,1,0,0,0,120,
        89,1,0,0,0,120,91,1,0,0,0,120,93,1,0,0,0,120,97,1,0,0,0,120,103,
        1,0,0,0,120,111,1,0,0,0,120,117,1,0,0,0,121,19,1,0,0,0,122,123,6,
        10,-1,0,123,124,3,22,11,0,124,129,1,0,0,0,125,126,10,2,0,0,126,128,
        3,22,11,0,127,125,1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,
        1,0,0,0,130,21,1,0,0,0,131,129,1,0,0,0,132,137,5,38,0,0,133,134,
        5,38,0,0,134,135,5,36,0,0,135,137,3,24,12,0,136,132,1,0,0,0,136,
        133,1,0,0,0,137,23,1,0,0,0,138,139,6,12,-1,0,139,161,5,1,0,0,140,
        161,5,2,0,0,141,161,5,38,0,0,142,161,5,3,0,0,143,161,5,4,0,0,144,
        161,5,39,0,0,145,146,5,38,0,0,146,147,5,32,0,0,147,161,5,33,0,0,
        148,149,5,38,0,0,149,150,5,32,0,0,150,151,3,26,13,0,151,152,5,33,
        0,0,152,161,1,0,0,0,153,154,5,32,0,0,154,155,3,24,12,0,155,156,5,
        33,0,0,156,161,1,0,0,0,157,158,3,28,14,0,158,159,3,24,12,2,159,161,
        1,0,0,0,160,138,1,0,0,0,160,140,1,0,0,0,160,141,1,0,0,0,160,142,
        1,0,0,0,160,143,1,0,0,0,160,144,1,0,0,0,160,145,1,0,0,0,160,148,
        1,0,0,0,160,153,1,0,0,0,160,157,1,0,0,0,161,168,1,0,0,0,162,163,
        10,1,0,0,163,164,3,30,15,0,164,165,3,24,12,2,165,167,1,0,0,0,166,
        162,1,0,0,0,167,170,1,0,0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,
        25,1,0,0,0,170,168,1,0,0,0,171,172,3,24,12,0,172,173,5,37,0,0,173,
        174,3,26,13,0,174,177,1,0,0,0,175,177,3,24,12,0,176,171,1,0,0,0,
        176,175,1,0,0,0,177,27,1,0,0,0,178,179,7,1,0,0,179,29,1,0,0,0,180,
        181,7,2,0,0,181,31,1,0,0,0,10,38,53,60,75,120,129,136,160,168,176
    ]

class rulesParser ( Parser ):

    grammarFileName = "rules.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'true'", "'false'", 
                     "'int'", "'double'", "'void'", "'boolean'", "'return'", 
                     "'if'", "'else'", "'while'", "'++'", "'--'", "'-'", 
                     "'!'", "'*'", "'/'", "'%'", "'+'", "'<'", "'>'", "'<='", 
                     "'>='", "'=='", "'!='", "'&&'", "'||'", "'.'", "'{'", 
                     "'}'", "'('", "')'", "';'", "'\"'", "'='", "','" ]

    symbolicNames = [ "<INVALID>", "INTEGER", "DOUBLE", "TRUE", "FALSE", 
                      "INT_T", "DOUBLE_T", "VOID_T", "BOOLEAN_T", "RETURN", 
                      "IF", "ELSE", "WHILE", "PLUSPLUS", "MINUSMINUS", "MINUS", 
                      "EXCLEM", "TIMES", "DEVIDE", "MOD", "PLUS", "LT", 
                      "GT", "LE", "GE", "EQ", "NE", "LOG_AND", "LOG_OR", 
                      "DOT", "O_B", "C_B", "O_P", "C_P", "SC", "DQ", "ASSIGN", 
                      "COMMA", "ID", "STRING", "BASIC_SOURCE_CHAR", "ESCAPE_SEQUENCE", 
                      "COMMENT", "LINE_COMMENT", "WS" ]

    RULE_program = 0
    RULE_functions = 1
    RULE_function = 2
    RULE_arguments = 3
    RULE_argument = 4
    RULE_type = 5
    RULE_block = 6
    RULE_statements = 7
    RULE_empty = 8
    RULE_statement = 9
    RULE_items = 10
    RULE_item = 11
    RULE_expression = 12
    RULE_parameters = 13
    RULE_unaryoperator = 14
    RULE_binaryoperator = 15

    ruleNames =  [ "program", "functions", "function", "arguments", "argument", 
                   "type", "block", "statements", "empty", "statement", 
                   "items", "item", "expression", "parameters", "unaryoperator", 
                   "binaryoperator" ]

    EOF = Token.EOF
    INTEGER=1
    DOUBLE=2
    TRUE=3
    FALSE=4
    INT_T=5
    DOUBLE_T=6
    VOID_T=7
    BOOLEAN_T=8
    RETURN=9
    IF=10
    ELSE=11
    WHILE=12
    PLUSPLUS=13
    MINUSMINUS=14
    MINUS=15
    EXCLEM=16
    TIMES=17
    DEVIDE=18
    MOD=19
    PLUS=20
    LT=21
    GT=22
    LE=23
    GE=24
    EQ=25
    NE=26
    LOG_AND=27
    LOG_OR=28
    DOT=29
    O_B=30
    C_B=31
    O_P=32
    C_P=33
    SC=34
    DQ=35
    ASSIGN=36
    COMMA=37
    ID=38
    STRING=39
    BASIC_SOURCE_CHAR=40
    ESCAPE_SEQUENCE=41
    COMMENT=42
    LINE_COMMENT=43
    WS=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functions(self):
            return self.getTypedRuleContext(rulesParser.FunctionsContext,0)


        def getRuleIndex(self):
            return rulesParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = rulesParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.functions()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(rulesParser.FunctionContext,0)


        def functions(self):
            return self.getTypedRuleContext(rulesParser.FunctionsContext,0)


        def getRuleIndex(self):
            return rulesParser.RULE_functions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctions" ):
                listener.enterFunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctions" ):
                listener.exitFunctions(self)




    def functions(self):

        localctx = rulesParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functions)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.function()
                self.state = 35
                self.functions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.function()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(rulesParser.TypeContext,0)


        def ID(self):
            return self.getToken(rulesParser.ID, 0)

        def O_P(self):
            return self.getToken(rulesParser.O_P, 0)

        def arguments(self):
            return self.getTypedRuleContext(rulesParser.ArgumentsContext,0)


        def C_P(self):
            return self.getToken(rulesParser.C_P, 0)

        def block(self):
            return self.getTypedRuleContext(rulesParser.BlockContext,0)


        def getRuleIndex(self):
            return rulesParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = rulesParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        try:
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.type_()
                self.state = 41
                self.match(rulesParser.ID)
                self.state = 42
                self.match(rulesParser.O_P)
                self.state = 43
                self.arguments()
                self.state = 44
                self.match(rulesParser.C_P)
                self.state = 45
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.type_()
                self.state = 48
                self.match(rulesParser.ID)
                self.state = 49
                self.match(rulesParser.O_P)
                self.state = 50
                self.match(rulesParser.C_P)
                self.state = 51
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(rulesParser.ArgumentContext,0)


        def COMMA(self):
            return self.getToken(rulesParser.COMMA, 0)

        def arguments(self):
            return self.getTypedRuleContext(rulesParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return rulesParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)




    def arguments(self):

        localctx = rulesParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arguments)
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.argument()
                self.state = 56
                self.match(rulesParser.COMMA)
                self.state = 57
                self.arguments()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.argument()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(rulesParser.TypeContext,0)


        def ID(self):
            return self.getToken(rulesParser.ID, 0)

        def getRuleIndex(self):
            return rulesParser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)




    def argument(self):

        localctx = rulesParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.type_()
            self.state = 63
            self.match(rulesParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_T(self):
            return self.getToken(rulesParser.INT_T, 0)

        def DOUBLE_T(self):
            return self.getToken(rulesParser.DOUBLE_T, 0)

        def BOOLEAN_T(self):
            return self.getToken(rulesParser.BOOLEAN_T, 0)

        def VOID_T(self):
            return self.getToken(rulesParser.VOID_T, 0)

        def getRuleIndex(self):
            return rulesParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = rulesParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 480) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def O_B(self):
            return self.getToken(rulesParser.O_B, 0)

        def statements(self):
            return self.getTypedRuleContext(rulesParser.StatementsContext,0)


        def C_B(self):
            return self.getToken(rulesParser.C_B, 0)

        def getRuleIndex(self):
            return rulesParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = rulesParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(rulesParser.O_B)
            self.state = 68
            self.statements()
            self.state = 69
            self.match(rulesParser.C_B)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(rulesParser.StatementContext,0)


        def statements(self):
            return self.getTypedRuleContext(rulesParser.StatementsContext,0)


        def empty(self):
            return self.getTypedRuleContext(rulesParser.EmptyContext,0)


        def getRuleIndex(self):
            return rulesParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = rulesParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_statements)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 30, 32, 34, 38, 39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.statement()
                self.state = 72
                self.statements()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.empty()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return rulesParser.RULE_empty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmpty" ):
                listener.enterEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmpty" ):
                listener.exitEmpty(self)




    def empty(self):

        localctx = rulesParser.EmptyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_empty)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SC(self):
            return self.getToken(rulesParser.SC, 0)

        def block(self):
            return self.getTypedRuleContext(rulesParser.BlockContext,0)


        def type_(self):
            return self.getTypedRuleContext(rulesParser.TypeContext,0)


        def items(self):
            return self.getTypedRuleContext(rulesParser.ItemsContext,0)


        def ID(self):
            return self.getToken(rulesParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(rulesParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(rulesParser.ExpressionContext,0)


        def PLUSPLUS(self):
            return self.getToken(rulesParser.PLUSPLUS, 0)

        def MINUSMINUS(self):
            return self.getToken(rulesParser.MINUSMINUS, 0)

        def RETURN(self):
            return self.getToken(rulesParser.RETURN, 0)

        def IF(self):
            return self.getToken(rulesParser.IF, 0)

        def O_P(self):
            return self.getToken(rulesParser.O_P, 0)

        def C_P(self):
            return self.getToken(rulesParser.C_P, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rulesParser.StatementContext)
            else:
                return self.getTypedRuleContext(rulesParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(rulesParser.ELSE, 0)

        def WHILE(self):
            return self.getToken(rulesParser.WHILE, 0)

        def getRuleIndex(self):
            return rulesParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = rulesParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(rulesParser.SC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.type_()
                self.state = 82
                self.items(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 84
                self.match(rulesParser.ID)
                self.state = 85
                self.match(rulesParser.ASSIGN)
                self.state = 86
                self.expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 87
                self.match(rulesParser.ID)
                self.state = 88
                self.match(rulesParser.PLUSPLUS)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 89
                self.match(rulesParser.ID)
                self.state = 90
                self.match(rulesParser.MINUSMINUS)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 91
                self.match(rulesParser.RETURN)
                self.state = 92
                self.match(rulesParser.SC)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 93
                self.match(rulesParser.RETURN)
                self.state = 94
                self.expression(0)
                self.state = 95
                self.match(rulesParser.SC)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 97
                self.match(rulesParser.IF)
                self.state = 98
                self.match(rulesParser.O_P)
                self.state = 99
                self.expression(0)
                self.state = 100
                self.match(rulesParser.C_P)
                self.state = 101
                self.statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 103
                self.match(rulesParser.IF)
                self.state = 104
                self.match(rulesParser.O_P)
                self.state = 105
                self.expression(0)
                self.state = 106
                self.match(rulesParser.C_P)
                self.state = 107
                self.statement()
                self.state = 108
                self.match(rulesParser.ELSE)
                self.state = 109
                self.statement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 111
                self.match(rulesParser.WHILE)
                self.state = 112
                self.match(rulesParser.O_P)
                self.state = 113
                self.expression(0)
                self.state = 114
                self.match(rulesParser.C_P)
                self.state = 115
                self.statement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 117
                self.expression(0)
                self.state = 118
                self.match(rulesParser.SC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def item(self):
            return self.getTypedRuleContext(rulesParser.ItemContext,0)


        def items(self):
            return self.getTypedRuleContext(rulesParser.ItemsContext,0)


        def getRuleIndex(self):
            return rulesParser.RULE_items

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItems" ):
                listener.enterItems(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItems" ):
                listener.exitItems(self)



    def items(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = rulesParser.ItemsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_items, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.item()
            self._ctx.stop = self._input.LT(-1)
            self.state = 129
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = rulesParser.ItemsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_items)
                    self.state = 125
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 126
                    self.item() 
                self.state = 131
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(rulesParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(rulesParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(rulesParser.ExpressionContext,0)


        def getRuleIndex(self):
            return rulesParser.RULE_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem" ):
                listener.enterItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem" ):
                listener.exitItem(self)




    def item(self):

        localctx = rulesParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_item)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(rulesParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.match(rulesParser.ID)
                self.state = 134
                self.match(rulesParser.ASSIGN)
                self.state = 135
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(rulesParser.INTEGER, 0)

        def DOUBLE(self):
            return self.getToken(rulesParser.DOUBLE, 0)

        def ID(self):
            return self.getToken(rulesParser.ID, 0)

        def TRUE(self):
            return self.getToken(rulesParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(rulesParser.FALSE, 0)

        def STRING(self):
            return self.getToken(rulesParser.STRING, 0)

        def O_P(self):
            return self.getToken(rulesParser.O_P, 0)

        def C_P(self):
            return self.getToken(rulesParser.C_P, 0)

        def parameters(self):
            return self.getTypedRuleContext(rulesParser.ParametersContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(rulesParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(rulesParser.ExpressionContext,i)


        def unaryoperator(self):
            return self.getTypedRuleContext(rulesParser.UnaryoperatorContext,0)


        def binaryoperator(self):
            return self.getTypedRuleContext(rulesParser.BinaryoperatorContext,0)


        def getRuleIndex(self):
            return rulesParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = rulesParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 139
                self.match(rulesParser.INTEGER)
                pass

            elif la_ == 2:
                self.state = 140
                self.match(rulesParser.DOUBLE)
                pass

            elif la_ == 3:
                self.state = 141
                self.match(rulesParser.ID)
                pass

            elif la_ == 4:
                self.state = 142
                self.match(rulesParser.TRUE)
                pass

            elif la_ == 5:
                self.state = 143
                self.match(rulesParser.FALSE)
                pass

            elif la_ == 6:
                self.state = 144
                self.match(rulesParser.STRING)
                pass

            elif la_ == 7:
                self.state = 145
                self.match(rulesParser.ID)
                self.state = 146
                self.match(rulesParser.O_P)
                self.state = 147
                self.match(rulesParser.C_P)
                pass

            elif la_ == 8:
                self.state = 148
                self.match(rulesParser.ID)
                self.state = 149
                self.match(rulesParser.O_P)
                self.state = 150
                self.parameters()
                self.state = 151
                self.match(rulesParser.C_P)
                pass

            elif la_ == 9:
                self.state = 153
                self.match(rulesParser.O_P)
                self.state = 154
                self.expression(0)
                self.state = 155
                self.match(rulesParser.C_P)
                pass

            elif la_ == 10:
                self.state = 157
                self.unaryoperator()
                self.state = 158
                self.expression(2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 168
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = rulesParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 162
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 163
                    self.binaryoperator()
                    self.state = 164
                    self.expression(2) 
                self.state = 170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(rulesParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(rulesParser.COMMA, 0)

        def parameters(self):
            return self.getTypedRuleContext(rulesParser.ParametersContext,0)


        def getRuleIndex(self):
            return rulesParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)




    def parameters(self):

        localctx = rulesParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameters)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.expression(0)
                self.state = 172
                self.match(rulesParser.COMMA)
                self.state = 173
                self.parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryoperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(rulesParser.MINUS, 0)

        def EXCLEM(self):
            return self.getToken(rulesParser.EXCLEM, 0)

        def getRuleIndex(self):
            return rulesParser.RULE_unaryoperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryoperator" ):
                listener.enterUnaryoperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryoperator" ):
                listener.exitUnaryoperator(self)




    def unaryoperator(self):

        localctx = rulesParser.UnaryoperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_unaryoperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryoperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TIMES(self):
            return self.getToken(rulesParser.TIMES, 0)

        def DEVIDE(self):
            return self.getToken(rulesParser.DEVIDE, 0)

        def MOD(self):
            return self.getToken(rulesParser.MOD, 0)

        def PLUS(self):
            return self.getToken(rulesParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(rulesParser.MINUS, 0)

        def LT(self):
            return self.getToken(rulesParser.LT, 0)

        def GT(self):
            return self.getToken(rulesParser.GT, 0)

        def LE(self):
            return self.getToken(rulesParser.LE, 0)

        def GE(self):
            return self.getToken(rulesParser.GE, 0)

        def EQ(self):
            return self.getToken(rulesParser.EQ, 0)

        def NE(self):
            return self.getToken(rulesParser.NE, 0)

        def LOG_AND(self):
            return self.getToken(rulesParser.LOG_AND, 0)

        def LOG_OR(self):
            return self.getToken(rulesParser.LOG_OR, 0)

        def getRuleIndex(self):
            return rulesParser.RULE_binaryoperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryoperator" ):
                listener.enterBinaryoperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryoperator" ):
                listener.exitBinaryoperator(self)




    def binaryoperator(self):

        localctx = rulesParser.BinaryoperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_binaryoperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 536772608) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.items_sempred
        self._predicates[12] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def items_sempred(self, localctx:ItemsContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




