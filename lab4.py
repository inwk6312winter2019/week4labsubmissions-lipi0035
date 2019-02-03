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

#Task 4----half pending

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

#Task 6 ---half pending
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
  