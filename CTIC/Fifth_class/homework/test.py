import re
f = open("v1alumnos2019.txt", 'r+')
text = f.read()
text = re.sub('M', '', text)
f.seek(0)
f.write(text)
f.truncate()
f.close()