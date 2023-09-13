import csv

training_data=[]

with open('/content/data.csv','r')as csvfile:
  read=csv.reader(csvfile)
  for row in read:
    training_data.append(row)

x=len(training_data[0])
n=x-1
print(n)

print('\nThe value of general hypothesis is :')
genhypothesis=['?']*n
print(genhypothesis)

print("\nData in the csv file")

for i in range(0,n-1):
  print(training_data[i])

print('\nThe initial value of hypothesis is :')
hypothesis=['0']*n
print(hypothesis)

x=1
for j in range(n):
  if(training_data[x][n]=='yes'):
    hypothesis[j]=training_data[x][j]
  else:
    x=x+1
print("\nthe first positive hypothesis :")
print(hypothesis)

print("\n Find S :")
for i in range(1,len(training_data)):
  if training_data[i][n]=='yes':
    for j in range(n):
      if training_data[i][j]!=hypothesis[j]:
        hypothesis[j]="?"
      
  print(hypothesis)

print("\nmaximal specific hypotheis is :\n")
print(hypothesis)
