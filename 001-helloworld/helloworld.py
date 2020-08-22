import os
import sys

where_am_i = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(where_am_i, "../deps"))

import numpy as np



print(os.path.join(where_am_i, "../deps"))