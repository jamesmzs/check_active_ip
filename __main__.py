#!/bin/env python
import sys
import os
path = os.path.dirname(sys.modules[__name__].__file__)
path = os.path.join(path, '..')
sys.path.insert(0, path)
#from sub import check_active_ip,excel
from check_active_ip import check_active_ip,excel
