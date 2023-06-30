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
        print("program")


    # Enter a parse tree produced by rulesParser#functions.
    def enterFunctions(self, ctx:rulesParser.FunctionsContext):
        pass

    # Exit a parse tree produced by rulesParser#functions.
    def exitFunctions(self, ctx:rulesParser.FunctionsContext):
        print("functions")


    # Enter a parse tree produced by rulesParser#function.
    def enterFunction(self, ctx:rulesParser.FunctionContext):
        pass

    # Exit a parse tree produced by rulesParser#function.
    def exitFunction(self, ctx:rulesParser.FunctionContext):
        print("function")


    # Enter a parse tree produced by rulesParser#arguments.
    def enterArguments(self, ctx:rulesParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by rulesParser#arguments.
    def exitArguments(self, ctx:rulesParser.ArgumentsContext):
        print("arguments")


    # Enter a parse tree produced by rulesParser#argument.
    def enterArgument(self, ctx:rulesParser.ArgumentContext):
        pass

    # Exit a parse tree produced by rulesParser#argument.
    def exitArgument(self, ctx:rulesParser.ArgumentContext):
        print("argument")


    # Enter a parse tree produced by rulesParser#type.
    def enterType(self, ctx:rulesParser.TypeContext):
        pass

    # Exit a parse tree produced by rulesParser#type.
    def exitType(self, ctx:rulesParser.TypeContext):
        ("type")


    # Enter a parse tree produced by rulesParser#block.
    def enterBlock(self, ctx:rulesParser.BlockContext):
        pass

    # Exit a parse tree produced by rulesParser#block.
    def exitBlock(self, ctx:rulesParser.BlockContext):
        print("block")


    # Enter a parse tree produced by rulesParser#statements.
    def enterStatements(self, ctx:rulesParser.StatementsContext):
        pass

    # Exit a parse tree produced by rulesParser#statements.
    def exitStatements(self, ctx:rulesParser.StatementsContext):
        print("statments")


    # Enter a parse tree produced by rulesParser#empty.
    def enterEmpty(self, ctx:rulesParser.EmptyContext):
        pass

    # Exit a parse tree produced by rulesParser#empty.
    def exitEmpty(self, ctx:rulesParser.EmptyContext):
        print("empty")


    # Enter a parse tree produced by rulesParser#statement.
    def enterStatement(self, ctx:rulesParser.StatementContext):
        pass

    # Exit a parse tree produced by rulesParser#statement.
    def exitStatement(self, ctx:rulesParser.StatementContext):
        print("statement")


    # Enter a parse tree produced by rulesParser#items.
    def enterItems(self, ctx:rulesParser.ItemsContext):
        pass

    # Exit a parse tree produced by rulesParser#items.
    def exitItems(self, ctx:rulesParser.ItemsContext):
        print("items")


    # Enter a parse tree produced by rulesParser#item.
    def enterItem(self, ctx:rulesParser.ItemContext):
        pass

    # Exit a parse tree produced by rulesParser#item.
    def exitItem(self, ctx:rulesParser.ItemContext):
        print("item")


    # Enter a parse tree produced by rulesParser#expression.
    def enterExpression(self, ctx:rulesParser.ExpressionContext):
        pass

    # Exit a parse tree produced by rulesParser#expression.
    def exitExpression(self, ctx:rulesParser.ExpressionContext):
        print(ctx.getText())
        print("expr")


    # Enter a parse tree produced by rulesParser#parameters.
    def enterParameters(self, ctx:rulesParser.ParametersContext):
        pass

    # Exit a parse tree produced by rulesParser#parameters.
    def exitParameters(self, ctx:rulesParser.ParametersContext):
        print("param")


    # Enter a parse tree produced by rulesParser#unaryoperator.
    def enterUnaryoperator(self, ctx:rulesParser.UnaryoperatorContext):
        pass

    # Exit a parse tree produced by rulesParser#unaryoperator.
    def exitUnaryoperator(self, ctx:rulesParser.UnaryoperatorContext):
        print("uop")


    # Enter a parse tree produced by rulesParser#binaryoperator.
    def enterBinaryoperator(self, ctx:rulesParser.BinaryoperatorContext):
        pass

    # Exit a parse tree produced by rulesParser#binaryoperator.
    def exitBinaryoperator(self, ctx:rulesParser.BinaryoperatorContext):
        print("bop")



del rulesParser