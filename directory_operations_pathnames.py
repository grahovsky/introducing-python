import os

# Create with mkdir()
os.mkdir('poems')
print(os.path.exists('poems'))

# Delete with rmdir()
os.rmdir('poems')
print(os.path.exists('poems'))

# List Contents with listdir()
print(os.listdir('.'))

# Change Current Directory with chdir()
os.chdir('exercises')
print(os.listdir('.'))

# List Matching Files with glob()
import glob
print(glob.glob('z*'))

# Pathnames
win_file = 'eek\\urk\\snort.txt'
print(win_file)
win_file = r'eek\urk\snort.txt'
print(win_file)

# Get a Pathname with abspath()
print(os.path.abspath('oops.txt'))

# Get a symlink Pathname with realpath()
print(os.path.realpath('jeepers.txt'))

# Build a Pathname with os.path.join()
win_file = os.path.join("eek", "urk")
print(win_file)
win_file = os.path.join(win_file, "snort.txt")
print(win_file)

# Use pathlib
from pathlib import Path
file_path = Path('eek') / 'urk' / 'snort.txt'
print(type(file_path))
print(file_path)

print(file_path.name)
print(file_path.suffix)
print(file_path.stem)

from pathlib import PureWindowsPath
PureWindowsPath(file_path)
print(type(PureWindowsPath(file_path)))
print(PureWindowsPath(file_path))