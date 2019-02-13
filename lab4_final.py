#Task 1
import string

count = 0
d = {}
l = []

def add_to_dictionary(word):
  global d
  d[word] = d.get(word,0)+1 
    
def remove_special_char(word):
  global count
  word = word.strip(special_char)
  if(word):
    count += 1
    add_to_dictionary(word)    
    #print(word)
    
fin1 = open("book.txt")

special_char = string.punctuation
lst_special_char = list(special_char)
#print(lst_special_char)
      
for line in fin:
  line = line.strip()
  words = line.split()
  for word in words:
    word = word.lower()
    remove_special_char(word)
    
fin1.close()

#task 2
 
fin2 = open("book.txt")

special_char = string.punctuation
lst_special_char = list(special_char)
#print(lst_special_char)
      
for line in fin:
  line = line.strip()
  words = line.split()
  for word in words:
    word = word.lower()
    remove_special_char(word)

print(d)
print(count)

print()

#Task 3

for key,value in d.items():
  l.append((value,key))
  #print(key,"",value)
#print(d)
l.sort(reverse = True)
for val,key in l[:20]:
  print(key," ",val)
  
fin2.close()

#Task 4

fin4 = open("words.txt")
s = set()
for line in fin4:
  line = line.strip()
  words = line.split()
  for word in words:
    s.add(word)
print(s)

fin_book = open("book.txt")

for line in fin_book:
  line = line.strip()
  words = line.split()
  for word in words:
    if word not in s:
      print(word)

#Task 5
import math
import matplotlib.pyplot as plt
frequency = []
rank = 0
words = []
log_f = []
log_r = []

def hist(fin):
  d = {}
  for line in fin:
    line = line.strip()
    words = line.split()
    for word in words:
      d[word] = d.get(word,0)+1   
  return d
    
def sortingOfDict(d):
  #keys = sorted(d.keys())
  sorted_list = []
  for key,val in d.items():
    sorted_list.append((val,key))
  sorted_list.sort(reverse=True)
  return sorted_list
    
fin = open("book.txt")
d = hist(fin)
sorted_dict = sortingOfDict(d)
fout = open("lab4_task5.txt","w")
for i in range(len(sorted_dict)):
  for j in range(2):
    if(isinstance(sorted_dict[i][j],int)):
      frequency.append(sorted_dict[i][j])
    else:
      words.append(sorted_dict[i][j])
  
fout.write("WORD\tlog(f)\tlog(r)\n")
fout.write("=====================================\n")
for w,f in zip(words,frequency):
  rank = rank+1
  log_f.append(math.log(f))
  log_r.append(math.log(rank))
  fout.write("%s\t%.2f\t%.2f\n" %(w,math.log(f),math.log(rank)))
  
plt.plot(log_f,log_r)
plt.show()

#Task 6
import os
import sys

walkdir = sys.argv[0]
print(walkdir)

rootDir = os.path.abspath('.')
print(rootDir)
for dirName,subdirList,fileList in os.walk(rootDir):
  print("Directory : %s" %dirName)
  for fname in fileList:
    print("\t%s" %fname)

#Task 7
try:
  def sed(pattern_str,replacement_str,file1,file2):
    fin = open(file1)
    fout = open(file2,'w')
    for line in fin:
      line = line.strip()
      words = line.split(' ')    
      for i in range(len(words)):
        if(words[i] == pattern_str):
          words[i] = replacement_str
    
    newstr = ' '.join(words)
    fout.write(newstr + "\n")
  
  data = sed("AAH","abcd","Samplefile.txt","newfile.txt")
  print("done")
  
except:
  print("Error occured")

#Task 8
import os

def walk(dirname):
    names = []
    if '__pycache__' in dirname:
        return names

    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            names.append(path)
        else:
            names.extend(walk(path))
    return names


def compute_checksum(filename):
    cmd = 'md5sum ' + filename
    return pipe(cmd)


def check_diff(name1, name2):
    cmd = 'diff %s %s' % (name1, name2)
    return pipe(cmd)

def pipe(cmd):
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    assert stat is None
    return res, stat


def compute_checksums(dirname, suffix):
    d = {}
    for name in dirname:
        if name.endswith(suffix):
            res, stat = compute_checksum(name)
            checksum, _ = res.split()

            if checksum in d:
                d[checksum].append(name)
            else:
                d[checksum] = [name]

    return d


def check_pairs(names):
    for name1 in names:
        for name2 in names:
            if name1 < name2:
                res, stat = check_diff(name1, name2)
                if res:
                    return False
    return True


def print_duplicates(d):
    for key, names in d.items():
        if len(names) > 1:
            print('The following files have the same checksum:')
            for name in names:
                print(name)

            if check_pairs(names):
                print('And they are identical.')


if __name__ == '__main__':
    d = compute_checksums(dirname='.', suffix='.py')
    print_duplicates(d)
