from antlr4 import *
from gen.MiniJavaParser import MiniJavaParser
from gen.MiniJavaListener import MiniJavaListener


class ErrorChecker(MiniJavaListener):

    def __init__(self):
        self.errNum = 0
        self.classMethodMap = {}
        self.variableValueMap = {}

    def printError(self, line, column, ErrorName):
        print('\033[1;31;40m')          #highlight in terminal
        print("Error %d  @ Line %d Column %d ErrorName:%s " % (self.errNum, line, column, ErrorName))
        print('\033[0m')

    def enterGoal(self, ctx:MiniJavaParser.GoalContext):
        pass

    def enterMainClass(self, ctx:MiniJavaParser.MainClassContext):
        name = ctx.IDENTIFIER(0).getText()
        if name in self.classMethodMap:
            self.errNum += 1
            self.printError(ctx.start.line, ctx.start.column, 'Redeclaration of class "%s"' % name)
        else:
            self.classMethodMap[name] = {}

    def enterClassDeclaration(self, ctx:MiniJavaParser.ClassDeclarationContext):
        name = ctx.IDENTIFIER(0).getText()
        if name in self.classMethodMap:
            self.errNum += 1
            self.printError(ctx.start.line, ctx.start.column, 'Redeclaration of class "%s"' % name)
        else:
            self.classMethodMap[name] = {}

        if ctx.getChild(2).getText() == "extends":
            extendsClassName = ctx.IDENTIFIER(1).getText()
            if extendsClassName not in self.classMethodMap:
                self.errNum += 1
                self.printError(ctx.start.line, ctx.start.column, 'class "%s" not declared' % extendsClassName)

    def enterVarDeclaration(self, ctx:MiniJavaParser.VarDeclarationContext):
        name = ctx.IDENTIFIER().getText()
        if name.isalpha():
            self.printError(ctx.start.line, ctx.start.column, 'illegal calration variable "%s"' % name)
        if type(ctx.parentCtx.IDENTIFIER()) is list:
            parentName = ctx.parentCtx.IDENTIFIER(0).getText()
        else:
            parentName = ctx.parentCtx.IDENTIFIER().getText()
        if parentName in self.classMethodMap:
            if name in self.classMethodMap[parentName]:
                self.errNum += 1
                self.printError(ctx.start.line, ctx.start.column, 'Redeclaration of class variable "%s"' % name)
            else:
                self.classMethodMap[parentName][name] = ctx.type().getText()
        else:
            grandparentName = ctx.parentCtx.parentCtx.IDENTIFIER(0).getText()
            if name in self.classMethodMap[grandparentName][parentName]:
                self.errNum += 1
                self.printError(ctx.start.line, ctx.start.column, 'Redeclaration of variable "%s"' % name)
            else:
                self.classMethodMap[grandparentName][parentName][name] = ctx.type().getText()

        # variable init
        if len(ctx.children) > 3:
            self.variableValueMap[name] = True
        else:
            self.variableValueMap[name] = False

    def enterMethodDeclaration(self, ctx:MiniJavaParser.MethodDeclarationContext):
        name = ctx.IDENTIFIER().getText()
        parentName = ctx.parentCtx.IDENTIFIER(0).getText()
        if name in self.classMethodMap[parentName]:
            self.errNum += 1
            self.printError(ctx.start.line, ctx.start.column, 'Redeclaration of method "%s"' % name)
        else:
            self.classMethodMap[parentName][name] = {}

        if not type(ctx.parameters().parameterDeclaration()) is list:
            parameters = [ctx.parameters().parameterDeclaration()]
        else:
            parameters = ctx.parameters().parameterDeclaration()
        for parameter in parameters:
            name = parameter.IDENTIFIER().getText()
            self.variableValueMap[name] = True


    def exitMethodDeclaration(self, ctx:MiniJavaParser.MethodDeclarationContext):
        if not type(ctx.parameters().parameterDeclaration()) is list:
            parameters = [ctx.parameters().parameterDeclaration()]
        else:
            parameters = ctx.parameters().parameterDeclaration()
        for parameter in parameters:
            name = parameter.IDENTIFIER().getText()
            if name in self.variableValueMap:
                del self.variableValueMap[name]

        if not type(ctx.varDeclaration()) is list:
            variables = [ctx.varDeclaration()]
        else:
            variables = ctx.varDeclaration()
        for variable in variables:
            name = variable.IDENTIFIER().getText()
            if name in self.variableValueMap:
                del self.variableValueMap[name]
                
    def enterType(self, ctx:MiniJavaParser.TypeContext):
        if ctx.IDENTIFIER() != None:
            name = ctx.IDENTIFIER()
            if name not in self.classMethodMap:
                self.errNum += 1
                self.printError(ctx.start.line, ctx.start.column, 'Unknown type "%s"' % name)

    def enterAssign(self, ctx:MiniJavaParser.AssignContext):
        name = ctx.IDENTIFIER().getText()
        self.variableValueMap[name] = True

    def enterVariable(self, ctx:MiniJavaParser.VariableContext):
        name = ctx.IDENTIFIER().getText()
        parentName = ctx.parentCtx.IDENTIFIER(0).getText()
        if parentName=="boolean":
        	not(name=="true" or name=="false")
        	self.printError(ctx.start.line, ctx.start.column, 'variable type should be boolean "%s"' % name)
        if parentName=="int":
        	not name.isdigit()
        	self.printError(ctx.start.line, ctx.start.column, 'variable type should be int"%s"' % name)
        
        if not name in self.variableValueMap:
            self.errNum += 1
            self.printError(ctx.start.line, ctx.start.column, 'Undeclared variable "%s"' % name)
        elif self.variableValueMap[name] == False:
            self.errNum += 1
            self.printError(ctx.start.line, ctx.start.column, 'Uninitiated variable "%s"' % name)

    def enterMethodCall(self, ctx:MiniJavaParser.MethodCallContext):
        name = ctx.IDENTIFIER().getText()
        flag = 0
        for instant in self.classMethodMap:
            if name in instant:
                flag = 1
        if flag == 0:
            self.errNum += 1
            self.printError(ctx.start.line, ctx.start.column, 'Unknown method "%s"' % name)