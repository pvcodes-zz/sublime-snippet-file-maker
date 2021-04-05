
file_name = str(input("Enter the file name: "))
file_name += ".sublime.snippet"
f= open(file_name,"w+")

cdata = str(input("Enter the snippet code: "))
ctab = str(input("Enter the tab trigger: "))
__write_val = "<snippet>\n<content><![CDATA[\n" + cdata + "\n]]></content>\n<tabTrigger>" + ctab + "</tabTrigger>\n<description>Description not provided</description>\n</snippet>"

f.write(__write_val)
f.close()
