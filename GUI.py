import sys
from tkinter import *
from tkinter.filedialog import*
from antlr4 import *
from generator.MiniJavaLexer import MiniJavaLexer
from generator.MiniJavaParser import MiniJavaParser
from recorrector.ErrorChecker import ErrorChecker
root=Tk()
def fileopen():
	fd=LoadFileDialog(root)
	filenpath=fd.go()
	code = open(filenpath).read()
	lexer = MiniJavaLexer(code)
    stream = CommonTokenStream(lexer)
    parser = MiniJavaParser(stream)
    tree = parser.goal()
    print(tree.toStringTree(recog=parser))

    checker = ErrorChecker()
    walker = ParseTreeWalker()
    walker.walk(checker, tree)
    print(checker.classMethodMap)
	#code.close()

menubar=Menu(root)

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="open",command=fileopen)
filemenu.add_separator()
filemenu.add_command(label="exit",command=root.quit)
menubar.add_cascade(label="file",menu=filemenu)
root.config(menu=menubar)

mainloop()