with open('D:\ARCHIVES\Computer_stuff\ATOM\old.txt') as fobj:
    text = fobj.read()
name = 0
a_file = open("D:\ARCHIVES\Computer_stuff\ATOM\old.txt", "r")
lines = a_file.readlines()
last_lines = lines[-5:]
print(last_lines)
for element in last_lines:
    print(element)
    element=float(element)
    if element>1:
        name=name+1
        print("+1")
a_file.close()
name=str(name)
print(name)
with open('D:\ARCHIVES\Computer_stuff\ATOM\old.txt', 'a') as fobj:
    if not text.endswith('\n'):
        fobj.write('\n')
    fobj.write(name)
