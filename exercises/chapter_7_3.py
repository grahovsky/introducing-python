
import binascii

hex_str = '47494638396101000100800000000000ffffff21f9' + \
          '0401000000002c000000000100010000020144003b'

gif = (binascii.unhexlify(hex_str))
print(len(gif))

print(type(b'GIF89a'))
print(gif[:6] == b'GIF89a')

import struct

width, height = struct.unpack('<HH', gif[6:10])
print('Valid PNG, width', width, 'height', height)