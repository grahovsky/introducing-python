import os
import sys
import platform

print(sys.platform)
# print(os.uname())
print(platform.uname())
# print(os.getloadavg())

# print(os.system('date -u'))

import psutil
print(psutil.cpu_percent(True))
print(psutil.cpu_percent(percpu=True))



