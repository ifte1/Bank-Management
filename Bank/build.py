#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")


name = "pyb publish"
default_task = "publish"


@init
def set_properties(project):
    project.set_property("dir_docs", "pyb")
