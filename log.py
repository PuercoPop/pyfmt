# -*- coding: utf-8 -*-
import logging
from os.path import realpath, dirname, join


log_file = realpath(join(dirname(__file__), "log/", "debug.log"))
logging.basicConfig(filename=log_file, filemode="w+",
                    level=logging.DEBUG)
log = logging.getLogger(__name__)
