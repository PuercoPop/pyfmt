# -*- coding: utf-8 -*-
import ast
from log import log
from printers import PrinterVisitor


if __name__ == "__main__":
    with open("samples/arithmetic.py", "r") as f:
        source_ast = ast.parse(f.read())
    with open("my_file.py", "w") as output:
        PrinterVisitor(output).visit(source_ast)
