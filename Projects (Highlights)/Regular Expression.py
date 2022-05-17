import re           # Import re module in order to use regular expressions in python

def regex():
    f = open('regex.csv', 'w')
    _in = raw_input("Please enter path to text file: ")
    _regexData = open(_in, "r").read()
    _pattern = r"[0-9A-Fa-f]{32}"           # MD5 Hashes assigned to the object "_pattern"
    _md5List = re.findall(_pattern, _regexData)
    f.write ("MD5\r")
    for _md5 in _md5List:
        print _md5
        f.write (_md5 + "\r")

regex()
