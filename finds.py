import pandas as pd
import csv
attributes=[['sunny','rainy'],['warm','cold'],['normal','high'],['strong','weak'],['warm','cool'],['same','change']]
training_data=[]
print(attributes)
n=len(attributes)

print("most general hypothesis : ['?','?','?','?','?','?']")

with open('/content/Untitled spreadsheet - Sheet1.csv','r')as csvfile:
  read=csv.reader(csvfile)
  for row in read:
    training_data.append(row)
for row in training_data:
  print(row)

print('\n the initial value of hypothesis is :')
hypothesis=['0']*n
print(hypothesis)

for j in range(n):
  hypothesis[j]=training_data[1][j]

print(hypothesis)

print("\n Find S :")
for i in range(1,len(training_data)):
  if training_data[i][n]=='yes':
    for j in range(n):
      if training_data[i][j]!=hypothesis[j]:
        hypothesis[j]="?"
      else:
        hypothesis[j]=training_data[i][j]
  print(hypothesis)

print("maximal specific hypotheis is :\n",hypothesis)
