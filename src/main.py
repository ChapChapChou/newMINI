import sys
from antlr4 import *
from generator.MiniJavaLexer import MiniJavaLexer
from generator.MiniJavaParser import MiniJavaParser
from recorrector.ErrorChecker import ErrorChecker

def main(argv):
    code = FileStream(argv[1])
    lexer = MiniJavaLexer(code)
    stream = CommonTokenStream(lexer)
    parser = MiniJavaParser(stream)
    tree = parser.goal()
    print(tree.toStringTree(aim=parser))

    checker = ErrorChecker()
    walker = ParseTreeWalker()
    walker.walk(checker, tree)
    print(checker.classMethodMap)


if __name__ == '__main__':
    main(sys.argv)
