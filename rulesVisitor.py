# Generated from C:/Users/MMNazari1380/PycharmProjects/CompilerFinalProject\rules.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .rulesParser import rulesParser
else:
    from rulesParser import rulesParser

# This class defines a complete generic visitor for a parse tree produced by rulesParser.

class rulesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by rulesParser#program.
    def visitProgram(self, ctx:rulesParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#functions.
    def visitFunctions(self, ctx:rulesParser.FunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#function.
    def visitFunction(self, ctx:rulesParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#arguments.
    def visitArguments(self, ctx:rulesParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#argument.
    def visitArgument(self, ctx:rulesParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#type.
    def visitType(self, ctx:rulesParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#block.
    def visitBlock(self, ctx:rulesParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#statements.
    def visitStatements(self, ctx:rulesParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#empty.
    def visitEmpty(self, ctx:rulesParser.EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#statement.
    def visitStatement(self, ctx:rulesParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#items.
    def visitItems(self, ctx:rulesParser.ItemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#item.
    def visitItem(self, ctx:rulesParser.ItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#expression.
    def visitExpression(self, ctx:rulesParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#parameters.
    def visitParameters(self, ctx:rulesParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#unaryoperator.
    def visitUnaryoperator(self, ctx:rulesParser.UnaryoperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by rulesParser#binaryoperator.
    def visitBinaryoperator(self, ctx:rulesParser.BinaryoperatorContext):
        return self.visitChildren(ctx)



del rulesParser