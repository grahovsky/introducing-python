#first use file_input_output for create resources

# Check Existence with exists()
import functools
import os
print(os.path.exists('oops.txt'))

print(os.path.exists('./oops.txt'))

print(os.path.exists('waffles'))

print(os.path.exists('.'))

print(os.path.exists('..'))

# Check Type with isfile()
name = 'oops.txt'
print(os.path.isfile(name))
print(os.path.isdir(name))

print(os.path.isdir('.'))
print(os.path.isabs(name))

# fix for repeat
os.chmod('oops.txt', 0o777)

# Copy with copy()
import shutil
shutil.copy('oops.txt', 'ohno.txt')

# Delete a File with remove()
if os.path.exists('ohwell.txt'):
    os.remove('ohwell.txt')

# Change Name with rename()
os.rename('ohno.txt', 'ohwell.txt')

# Delete a File with remove()
if os.path.exists('yikes.txt'):
    os.remove('yikes.txt')

# Link with link() or symlink()
os.link('oops.txt', 'yikes.txt')
print(os.path.isfile('yikes.txt'))
print(os.path.islink('yikes.txt'))

# need root/admin
# os.symlink('oops.txt', 'jeepers.txt')
# print(os.path.islink('jeepers.txt'))

# Change Permissions with chmod()
os.chmod('oops.txt', 0o400)

# Change Ownership with chown()
# uid = 5
# gid = 22
# os.chown('oops', uid, gid)