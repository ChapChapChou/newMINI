# Generated from /Users/MiniJava/MiniJava.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniJavaParser import MiniJavaParser
else:
    from MiniJavaParser import MiniJavaParser

# This class defines a complete generic visitor for a parse tree produced by MiniJavaParser.

class MiniJavaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniJavaParser#goal.
    def visitGoal(self, ctx:MiniJavaParser.GoalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#mainClass.
    def visitMainClass(self, ctx:MiniJavaParser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#classDeclaration.
    def visitClassDeclaration(self, ctx:MiniJavaParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MiniJavaParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:MiniJavaParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#parameters.
    def visitParameters(self, ctx:MiniJavaParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#parameterDeclaration.
    def visitParameterDeclaration(self, ctx:MiniJavaParser.ParameterDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#type.
    def visitType(self, ctx:MiniJavaParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#block.
    def visitBlock(self, ctx:MiniJavaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#if.
    def visitIf(self, ctx:MiniJavaParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#while.
    def visitWhile(self, ctx:MiniJavaParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#print.
    def visitPrint(self, ctx:MiniJavaParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#assign.
    def visitAssign(self, ctx:MiniJavaParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#arrayAssign.
    def visitArrayAssign(self, ctx:MiniJavaParser.ArrayAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#constant.
    def visitConstant(self, ctx:MiniJavaParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#newIntArray.
    def visitNewIntArray(self, ctx:MiniJavaParser.NewIntArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#this.
    def visitThis(self, ctx:MiniJavaParser.ThisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#length.
    def visitLength(self, ctx:MiniJavaParser.LengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#notExpression.
    def visitNotExpression(self, ctx:MiniJavaParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#binaryOperation.
    def visitBinaryOperation(self, ctx:MiniJavaParser.BinaryOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#parenthesesExpression.
    def visitParenthesesExpression(self, ctx:MiniJavaParser.ParenthesesExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#newClass.
    def visitNewClass(self, ctx:MiniJavaParser.NewClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#logicOperation.
    def visitLogicOperation(self, ctx:MiniJavaParser.LogicOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#comparasionOperation.
    def visitComparasionOperation(self, ctx:MiniJavaParser.ComparasionOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#variable.
    def visitVariable(self, ctx:MiniJavaParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#arrayAccess.
    def visitArrayAccess(self, ctx:MiniJavaParser.ArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#methodCall.
    def visitMethodCall(self, ctx:MiniJavaParser.MethodCallContext):
        return self.visitChildren(ctx)



del MiniJavaParser
