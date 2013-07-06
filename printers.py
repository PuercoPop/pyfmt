# -*- coding: utf-8 -*-
import ast
from log import log


def dispatch(node, output):
    if isinstance(node, ast.Module):
        mv = ModuleVisitor()
        mv.visit(node, output)
    elif isinstance(node, ast.Expr):
        ev = ExprVisitor()
        ev.visit(node, output)
    elif isinstance(node, ast.BinOp):
        bov = BinOpVisitor()
        bov.visit(node, output)
    elif isinstance(node, ast.Num):
        nv = NumVisitor()
        nv.visit(node, output)
    elif isinstance(node, ast.Add):
        av = AddVisitor()
        av.visit(node, output)
    elif isinstance(node, ast.Sub):
        sv = SubVisitor()
        sv.visit(node, output)
    elif isinstance(node, ast.Div):
        dv = DivVisitor()
        dv.visit(node, output)
    elif isinstance(node, ast.Pow):
        pv = PowVisitor()
        pv.visit(node, output)
    elif isinstance(node, ast.Mod):
        mv = ModVisitor()
        mv.visit(node, output)
    else:
        import ipdb; ipdb.set_trace()


class BasePrinterVisitor(ast.NodeVisitor):
    def visit(self, node):
        log.info("In {node_name}".format(node_name=node.__class__.__name__))



class ModuleVisitor(BasePrinterVisitor):
    def visit(self, node, output):
        super(ModuleVisitor, self).visit(node)
        for node in node.body:
            dispatch(node, output)

class ExprVisitor(BasePrinterVisitor):
    def visit(self, node, output):
        super(ExprVisitor, self).visit(node)
        dispatch(node.value, output)
        output.write("\n")

class BinOpVisitor(BasePrinterVisitor):
    def visit(self, node, output):
        super(BinOpVisitor, self).visit(node)
        dispatch(node.right, output)
        dispatch(node.op, output)
        dispatch(node.left, output)

class NumVisitor(BasePrinterVisitor):
    def visit(self, node, output):
        super(NumVisitor, self).visit(node)
        output.write(str(node.n))

class AddVisitor(BasePrinterVisitor):
    def visit(self, node, output):
        super(AddVisitor, self).visit(node)
        output.write(" + ")

class SubVisitor(BasePrinterVisitor):
    def visit(self, node, output):
        super(SubVisitor, self).visit(node)
        output.write(" - ")

class DivVisitor(BasePrinterVisitor):
    def visit(self, node, output):
        super(DivVisitor, self).visit(node)
        output.write(" / ")

class PowVisitor(BasePrinterVisitor):
    def visit(self, node, output):
        super(PowVisitor, self).visit(node)
        output.write(" ** ")


class ModVisitor(BasePrinterVisitor):
    def visit(self, node, output):
        super(ModVisitor, self).visit(node)
        output.write(" % ")
