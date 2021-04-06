file_name = str(input("Enter the file name: "))
file_name += ".sublime-snippet"

cdata = ""

isFile = (input("DO you want to snippet from a file:(Y/N) "))

if isFile == 'Y' or isFile == 'y':
    s_fileName = str(input("Enter the file name with it's extension: "))
    _a = open(s_fileName, "r")
    if _a.mode == 'r':
        cdata = _a.read()
else:
    i = 1
    while True:
        tmp = str(
            input("Enter the " + str(i) + " line:(when you are done input 'exit') "))
        i += 1
        if tmp == "exit":
            break
        else:
            tmp += "\n"
            cdata += tmp


_f = open(file_name, "w+")

ctab = str(input("Enter the tab trigger: "))
cdes = str(input("Enter the snippet description: "))
__write_val = "<snippet>\n<content><![CDATA[\n" + cdata + "\n]]></content>\n<tabTrigger>" + \
    ctab + "</tabTrigger>\n<description>" + cdes + "</description>\n</snippet>"

_f.write(__write_val)
_f.close()

print("\nYour file is been created in the same directory, cut it and paste to the Sublime's User folder")
