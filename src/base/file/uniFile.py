# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
An example of reading and writing Unicode strings:
Writes a Unicode string to a file in utf-8 and reads it back in.
'''

CODEC = 'utf-8'
FILE = 'unicode.txt'
hello_out = "Hello world\n"
bytes_out = hello_out.encode(CODEC)
f = open(FILE, "wb")
f.write(bytes_out)
f.close()

f = open(FILE, "rb")
bytes_in = f.read()
f.close
hello_in = bytes_in.decode(CODEC)
print(hello_in)