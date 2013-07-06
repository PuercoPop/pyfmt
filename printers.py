# -*- coding: utf-8 -*-
import ast
from log import log


class PrinterVisitor(ast.NodeVisitor):
    def __init__(self, output):
        super(PrinterVisitor, self).__init__()
        self.output = output

    def visit_Add(self, node):
        self.output.write(" + ")

    def visit_Sub(self, node):
        self.output.write(" - ")

    def visit_Div(self, node):
        self.output.write(" / ")

    def visit_Pow(self, node):
        self.output.write(" ** ")

    def visit_Mod(self, node):
        self.output.write(" % ")

    def visit_Num(self, node):
        self.output.write(str(node.n))

    def visit_Expr(self, node):
        self.generic_visit(node)
        self.output.write("\n")
