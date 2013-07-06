# -*- coding: utf-8 -*-
import ast


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
    else:
        import ipdb; ipdb.set_trace()

class ModuleVisitor(ast.NodeVisitor):
    def visit(self, node, output):
        print node.__class__.__name__
        for node in node.body:
            dispatch(node, output)

class ExprVisitor(ast.NodeVisitor):
    def visit(self, node, output):
        print node.__class__.__name__
        dispatch(node.value, output)

class BinOpVisitor(ast.NodeVisitor):
    def visit(self, node, output):
        print node.__class__.__name__
        dispatch(node.right, output)
        dispatch(node.op, output)
        dispatch(node.left, output)

class NumVisitor(ast.NodeVisitor):
    def visit(self, node, output):
        output.write(str(node.n))

class AddVisitor(ast.NodeVisitor):
    def visit(self, node, output):
        output.write(" + ")
