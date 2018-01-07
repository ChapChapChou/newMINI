# Generated from /Users/MiniJava/MiniJava.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniJavaParser import MiniJavaParser
else:
    from MiniJavaParser import MiniJavaParser

# This class defines a complete listener for a parse tree produced by MiniJavaParser.
class MiniJavaListener(ParseTreeListener):

    # Enter a parse tree produced by MiniJavaParser#goal.
    def enterGoal(self, ctx:MiniJavaParser.GoalContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#goal.
    def exitGoal(self, ctx:MiniJavaParser.GoalContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#mainClass.
    def enterMainClass(self, ctx:MiniJavaParser.MainClassContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#mainClass.
    def exitMainClass(self, ctx:MiniJavaParser.MainClassContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#classDeclaration.
    def enterClassDeclaration(self, ctx:MiniJavaParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#classDeclaration.
    def exitClassDeclaration(self, ctx:MiniJavaParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#varDeclaration.
    def enterVarDeclaration(self, ctx:MiniJavaParser.VarDeclarationContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#varDeclaration.
    def exitVarDeclaration(self, ctx:MiniJavaParser.VarDeclarationContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:MiniJavaParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:MiniJavaParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#parameters.
    def enterParameters(self, ctx:MiniJavaParser.ParametersContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#parameters.
    def exitParameters(self, ctx:MiniJavaParser.ParametersContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:MiniJavaParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:MiniJavaParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#type.
    def enterType(self, ctx:MiniJavaParser.TypeContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#type.
    def exitType(self, ctx:MiniJavaParser.TypeContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#block.
    def enterBlock(self, ctx:MiniJavaParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#block.
    def exitBlock(self, ctx:MiniJavaParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#if.
    def enterIf(self, ctx:MiniJavaParser.IfContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#if.
    def exitIf(self, ctx:MiniJavaParser.IfContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#while.
    def enterWhile(self, ctx:MiniJavaParser.WhileContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#while.
    def exitWhile(self, ctx:MiniJavaParser.WhileContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#print.
    def enterPrint(self, ctx:MiniJavaParser.PrintContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#print.
    def exitPrint(self, ctx:MiniJavaParser.PrintContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#assign.
    def enterAssign(self, ctx:MiniJavaParser.AssignContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#assign.
    def exitAssign(self, ctx:MiniJavaParser.AssignContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#arrayAssign.
    def enterArrayAssign(self, ctx:MiniJavaParser.ArrayAssignContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#arrayAssign.
    def exitArrayAssign(self, ctx:MiniJavaParser.ArrayAssignContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#constant.
    def enterConstant(self, ctx:MiniJavaParser.ConstantContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#constant.
    def exitConstant(self, ctx:MiniJavaParser.ConstantContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#newIntArray.
    def enterNewIntArray(self, ctx:MiniJavaParser.NewIntArrayContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#newIntArray.
    def exitNewIntArray(self, ctx:MiniJavaParser.NewIntArrayContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#this.
    def enterThis(self, ctx:MiniJavaParser.ThisContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#this.
    def exitThis(self, ctx:MiniJavaParser.ThisContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#length.
    def enterLength(self, ctx:MiniJavaParser.LengthContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#length.
    def exitLength(self, ctx:MiniJavaParser.LengthContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#notExpression.
    def enterNotExpression(self, ctx:MiniJavaParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#notExpression.
    def exitNotExpression(self, ctx:MiniJavaParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#binaryOperation.
    def enterBinaryOperation(self, ctx:MiniJavaParser.BinaryOperationContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#binaryOperation.
    def exitBinaryOperation(self, ctx:MiniJavaParser.BinaryOperationContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#parenthesesExpression.
    def enterParenthesesExpression(self, ctx:MiniJavaParser.ParenthesesExpressionContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#parenthesesExpression.
    def exitParenthesesExpression(self, ctx:MiniJavaParser.ParenthesesExpressionContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#newClass.
    def enterNewClass(self, ctx:MiniJavaParser.NewClassContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#newClass.
    def exitNewClass(self, ctx:MiniJavaParser.NewClassContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#logicOperation.
    def enterLogicOperation(self, ctx:MiniJavaParser.LogicOperationContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#logicOperation.
    def exitLogicOperation(self, ctx:MiniJavaParser.LogicOperationContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#comparasionOperation.
    def enterComparasionOperation(self, ctx:MiniJavaParser.ComparasionOperationContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#comparasionOperation.
    def exitComparasionOperation(self, ctx:MiniJavaParser.ComparasionOperationContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#variable.
    def enterVariable(self, ctx:MiniJavaParser.VariableContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#variable.
    def exitVariable(self, ctx:MiniJavaParser.VariableContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#arrayAccess.
    def enterArrayAccess(self, ctx:MiniJavaParser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#arrayAccess.
    def exitArrayAccess(self, ctx:MiniJavaParser.ArrayAccessContext):
        pass


    # Enter a parse tree produced by MiniJavaParser#methodCall.
    def enterMethodCall(self, ctx:MiniJavaParser.MethodCallContext):
        pass

    # Exit a parse tree produced by MiniJavaParser#methodCall.
    def exitMethodCall(self, ctx:MiniJavaParser.MethodCallContext):
        pass


