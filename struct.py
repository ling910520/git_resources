import struct 
  
# Format: h is short in C type 
# Format: l is long in C type 
# Format 'hhl' stands for 'short short long' 
var = struct.pack('hhl',1,2,3) 
print(var) 


# Format: i is int in C type 
# Format 'iii' stands for 'int int int' 
var = struct.pack('iii',1,2,3) 
print(var) 

import struct 
  
# '?' -> _BOOL , 'h' -> short, 'i' -> int and 'l' -> long 
var = struct.pack('?hil', True, 2, 5, 445) 
print(var) 
tup = struct.unpack('?hil', var) 
print(tup) 
tup[0]