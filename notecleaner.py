wert = int(input('How many characters do you want to preview?: '))
file = open('notes.txt','r')

print(file.read(wert))
file.close()
print()

file = open('notes.txt', 'r')
line = file.readlines()
file.close()
print('Total lines:' , len(line) )

for i in range(len(line)):

    print( i+1, line[i].strip())

print()

word = input('Filter lines: ')
file = open('notes.txt', 'r')
for x in file:
    if x.startswith(word):
        print('skipped', x.strip())
    else:
        print('kept', x.strip())

file.close()
print()


file = open('notes.txt', 'r')
dert = file.readlines()
file.close()
odd = open('oddlines.txt', 'w')
for j in range(0, len(dert), 2):

    odd.write(dert[i])
    
odd.close()
