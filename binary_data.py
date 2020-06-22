# Binary Data


# bytes and bytearray

blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes)

the_byte_array = bytearray(blist)
print(the_byte_array)

# the_bytes[1] = 127
# TypeError: 'bytes' object does not support item assignment

the_byte_array[1] = 127
print(the_byte_array)

# Convert Binary Data with struct
import struct
valid_png_header = b'\x89PNG\r\n\x1a\n'
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
    b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
if data[:8] == valid_png_header:
    width, height = struct.unpack('>LL', data[16:24]) # The > means that integers are stored in big-endian format. Each L specifies a four-byte unsigned long integer.
    # struct.unpack('>16x2L6x', data)
    print('Valid PNG, width', width, 'height', height)
else:
    print('Not a valid PNG')

print(data[16:20])
# b'\x00\x00\x00\x9a'
print(data[20:24])
# b'\x00\x00\x00\x8d'

print(0x9a)
# 154
print(0x8d)
# 141

print(struct.pack('>L', 154))
# b'\x00\x00\x00\x9a'
print(struct.pack('>L', 141))
# b'\x00\x00\x00\x8d'


# Other Binary Data Tools


# pip install construct
from construct import Struct, Const, Int8ub, Array, Byte
# adapted from code at https://github.com/construct

format = Struct(
    "signature" / Const(b"BMP"),
    "width" / Int8ub,
    "height" / Int8ub,
    "pixels" / Array(3 * 2, Byte),
)
print(format.build(dict(width=3, height=2, pixels=[7,8,9,11,12,13])))
# b'BMP\x03\x02\x07\x08\t\x0b\x0c\r'
print(format.parse(b'BMP\x03\x02\x07\x08\t\x0b\x0c\r'))

# Convert Bytes/Strings with binascii()
import binascii
valid_png_header = b'\x89PNG\r\n\x1a\n'
print(binascii.hexlify(valid_png_header))
# b'89504e470d0a1a0a'
print(binascii.unhexlify(b'89504e470d0a1a0a'))
# b'\x89PNG\r\n\x1a\n'