# A module is basically a file containing a set of functions to include in your applications.
# There are core python modules, modules you can install using the pip package manager
# (including Django) as well as custom modules

import datetime
from time import time
from datetime import date


# today = datetime.date.today()
today = date.today()
timestamp = time()

print(today)
print(timestamp)