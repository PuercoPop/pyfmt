# -*- coding: utf-8 -*-
import ast
from log import log
from printers import dispatch


if __name__ == "__main__":
    source_ast = ast.parse("1 + 3; 4 / 2")
    with open("my_file.py", "w") as output:
        dispatch(source_ast, output)
