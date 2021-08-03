'''
2. Write a python program to read the content of a file and find how many upper case letters, lower case letters and digits existed in the file.
'''
file = open('SampleCount.txt','r')
data = file.read()
print('Contents of a file is')
print(data)
digit = upper = lower = special = 0
for ch in data:
  if ch.islower():
    lower += 1
  elif ch.isuppe():
    upper += 1
  elif ch.isdigit():
    digit += 1
  else:
    special += 1
print('Number of Upper case letters in a file is',upper)
print('Number of Lower case letters in a file is',lower)
print('Number of Digit in a file is',digit)
print('Number of Special Characters in a file is',special)
file.close()            
