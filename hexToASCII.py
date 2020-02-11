# codecs.encode(b"c", "hex")

import codecs

string = '3c'

string = codecs.decode(string, "hex").decode("utf-8")

type(string)

codecs.encode(b"3c 63", "hex")