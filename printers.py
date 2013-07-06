# -*- coding: utf-8 -*-
import ast


def dispatch(node):
    if isinstance(node, ast.Module):
        mv = ModuleVisitor()
        mv.visit(node)
    elif isinstance(node, ast.Expr):
        ev = ExprVisitor()
        ev.visit(node)
    elif isinstance(node, ast.BinOp):
        bov = BinOpVisitor()
        bov.visit(node)
    elif isinstance(node, ast.Num):
        nv = NumVisitor()
        nv.visit(node)
    elif isinstance(node, ast.Add):
        av = AddVisitor()
        av.visit(node)
    else:
        import ipdb; ipdb.set_trace()

class ModuleVisitor(ast.NodeVisitor):
    def visit(self, node):
        print node.__class__.__name__
        for node in node.body:
            dispatch(node)

class ExprVisitor(ast.NodeVisitor):
    def visit(self, node):
        print node.__class__.__name__
        dispatch(node.value)

class BinOpVisitor(ast.NodeVisitor):
    def visit(self, node):
        print node.__class__.__name__
        dispatch(node.right)
        dispatch(node.op)
        dispatch(node.left)

class NumVisitor(ast.NodeVisitor):
    def visit(self, node):
        print node.n

class AddVisitor(ast.NodeVisitor):
    def visit(self, node):
        print "+"
