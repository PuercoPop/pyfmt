# -*- coding: utf-8 -*-
import ast
import logging
from os.path import dirname, join, realpath
from printers import dispatch
# from . import settings

### LOG: SHOULD REFACTOR THIS ###
log_file = realpath(join(dirname(__file__), "log/", "trace.ast"))
logging.basicConfig(filename=log_file, filemode="w+",
                    level=logging.DEBUG)
log = logging.getLogger(__name__)
###






if __name__ == "__main__":
    source_ast = ast.parse("1 + 3")
    dispatch(source_ast)
