fout = open('oops.txt', 'wt')
print('Oops, I created a file.', file=fout)
fout.close()

poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''
print(len(poem))

fout = open('relativity', 'wt')
fout.write(poem)
fout.close()

fout = open('relativity', 'wt')
print(poem, file=fout, sep='', end='')
fout.close()

fout = open('relativity', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
         break
    fout.write(poem[offset:offset+chunk])
    offset += chunk
fout.close()

# Read a Text File with read(), readline(), or readlines()
fin = open('relativity', 'rt' )
poem = fin.read()
fin.close()
print(len(poem))

poem = ''
fin = open('relativity', 'rt' )
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment
fin.close()
print(len(poem))

poem = ''
fin = open('relativity', 'rt' )
while True:
    line = fin.readline()
    if not line:
        break
    poem += line
fin.close()
print(len(poem))

poem = ''
fin = open('relativity', 'rt' )
for line in fin:
    poem += line
fin.close()
print(len(poem))

fin = open('relativity', 'rt' )
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')
for line in lines:
    print(line, end='')


# Write a Binary File with write()
print('\n','{0:!^30s}'.format('binary'))
bdata = bytes(range(0, 256))
print(len(bdata))

fout = open('bfile', 'wb')
fout.write(bdata)
fout.close()

fout = open('bfile', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
         break
    fout.write(bdata[offset:offset+chunk])
    offset += chunk

# Read a Binary File with read()
fin = open('bfile', 'rb')
bdata = fin.read()
print(len(bdata))
fin.close()

# Close Files Automatically by Using with
with open('relativity', 'wt') as fout:
   fout.write(poem)

# Change Position with seek()
fin = open('bfile', 'rb')
print(fin.tell())

fin.seek(255)

# You can call seek() with a second argument: seek(offset, origin):
#     If origin is 0 (the default), go offset bytes from the start
#     If origin is 1, go offset bytes from the current position
#     If origin is 2, go offset bytes relative to the end

bdata = fin.read()
len(bdata)

print(bdata[0])

fin = open('bfile', 'rb')
# One byte before the end of the file:
fin.seek(-1, 2)
print(fin.tell())

fin = open('bfile', 'rb')
# This next example ends up two bytes before the end of the file:\
fin.seek(254, 0)
print(fin.tell())
# Now go forward one byte:
fin.seek(1, 1)
print(fin.tell())