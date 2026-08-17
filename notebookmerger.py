import os

with open ('science-notes.txt', 'r') as f:
    for line in f:
        print(line.strip())
print()

with open ('maths-notes.txt', 'r') as f:
    for line in f:
        words = line.split()
        print(len(words), 'words -->', line.strip())

if os.path.exists('all-notes.txt'):
    print('all-notes.txt already exists')
else:
    print('\nall-notes.txt doesnt exist --- creating now')

content = ''
with open('science-notes.txt', 'r') as f:
    content += '--science-notes.txt--\n'
    content += f.read()+'\n'

with open('maths-notes.txt', 'r') as f:
    content += '\n--maths-notes.txt--\n'
    content += f.read()+'\n'

with open('all-notes.txt','w') as f:
    f.write(content)
print()

if os.path.exists('all-notes.txt'):
    os.remove('all-notes.txt')
    print('all notes succesfully removed')
else:
    print('all notes does not exist')
    

