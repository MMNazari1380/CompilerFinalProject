# Generated from rules.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .rulesParser import rulesParser
else:
    from rulesParser import rulesParser

# This class defines a complete listener for a parse tree produced by rulesParser.
class rulesListener(ParseTreeListener):

    # Enter a parse tree produced by rulesParser#program.
    def enterProgram(self, ctx:rulesParser.ProgramContext):
        pass

    # Exit a parse tree produced by rulesParser#program.
    def exitProgram(self, ctx:rulesParser.ProgramContext):
        pass


    # Enter a parse tree produced by rulesParser#functions.
    def enterFunctions(self, ctx:rulesParser.FunctionsContext):
        pass

    # Exit a parse tree produced by rulesParser#functions.
    def exitFunctions(self, ctx:rulesParser.FunctionsContext):
        pass


    # Enter a parse tree produced by rulesParser#function.
    def enterFunction(self, ctx:rulesParser.FunctionContext):
        pass

    # Exit a parse tree produced by rulesParser#function.
    def exitFunction(self, ctx:rulesParser.FunctionContext):
        pass


    # Enter a parse tree produced by rulesParser#arguments.
    def enterArguments(self, ctx:rulesParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by rulesParser#arguments.
    def exitArguments(self, ctx:rulesParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by rulesParser#argument.
    def enterArgument(self, ctx:rulesParser.ArgumentContext):
        pass

    # Exit a parse tree produced by rulesParser#argument.
    def exitArgument(self, ctx:rulesParser.ArgumentContext):
        pass


    # Enter a parse tree produced by rulesParser#type.
    def enterType(self, ctx:rulesParser.TypeContext):
        pass

    # Exit a parse tree produced by rulesParser#type.
    def exitType(self, ctx:rulesParser.TypeContext):
        pass


    # Enter a parse tree produced by rulesParser#block.
    def enterBlock(self, ctx:rulesParser.BlockContext):
        pass

    # Exit a parse tree produced by rulesParser#block.
    def exitBlock(self, ctx:rulesParser.BlockContext):
        pass


    # Enter a parse tree produced by rulesParser#statements.
    def enterStatements(self, ctx:rulesParser.StatementsContext):
        pass

    # Exit a parse tree produced by rulesParser#statements.
    def exitStatements(self, ctx:rulesParser.StatementsContext):
        pass


    # Enter a parse tree produced by rulesParser#empty.
    def enterEmpty(self, ctx:rulesParser.EmptyContext):
        pass

    # Exit a parse tree produced by rulesParser#empty.
    def exitEmpty(self, ctx:rulesParser.EmptyContext):
        pass


    # Enter a parse tree produced by rulesParser#statement.
    def enterStatement(self, ctx:rulesParser.StatementContext):
        pass

    # Exit a parse tree produced by rulesParser#statement.
    def exitStatement(self, ctx:rulesParser.StatementContext):
        pass


    # Enter a parse tree produced by rulesParser#items.
    def enterItems(self, ctx:rulesParser.ItemsContext):
        pass

    # Exit a parse tree produced by rulesParser#items.
    def exitItems(self, ctx:rulesParser.ItemsContext):
        pass


    # Enter a parse tree produced by rulesParser#item.
    def enterItem(self, ctx:rulesParser.ItemContext):
        pass

    # Exit a parse tree produced by rulesParser#item.
    def exitItem(self, ctx:rulesParser.ItemContext):
        pass


    # Enter a parse tree produced by rulesParser#expression.
    def enterExpression(self, ctx:rulesParser.ExpressionContext):
        pass

    # Exit a parse tree produced by rulesParser#expression.
    def exitExpression(self, ctx:rulesParser.ExpressionContext):
        pass


    # Enter a parse tree produced by rulesParser#parameters.
    def enterParameters(self, ctx:rulesParser.ParametersContext):
        pass

    # Exit a parse tree produced by rulesParser#parameters.
    def exitParameters(self, ctx:rulesParser.ParametersContext):
        pass


    # Enter a parse tree produced by rulesParser#unaryoperator.
    def enterUnaryoperator(self, ctx:rulesParser.UnaryoperatorContext):
        pass

    # Exit a parse tree produced by rulesParser#unaryoperator.
    def exitUnaryoperator(self, ctx:rulesParser.UnaryoperatorContext):
        pass


    # Enter a parse tree produced by rulesParser#binaryoperator.
    def enterBinaryoperator(self, ctx:rulesParser.BinaryoperatorContext):
        pass

    # Exit a parse tree produced by rulesParser#binaryoperator.
    def exitBinaryoperator(self, ctx:rulesParser.BinaryoperatorContext):
        pass



del rulesParser