import os
import shutil

sortdata = []

for i in os.listdir(
        'D:\savergb4training_0701-store-rgb\savergb4training_0701-store-rgb\savergb-190701-store_select_5-1'):
    data = os.path.splitext(i)
    sortdata.append(int(data[0]))

    # if int(data[0]) % 5 == 0:
    #     shutil.copy('data/'+i,'sampling data')
sortdata.sort()

k = 0
num1 = 0
fetal1 = []
for i in range(len(sortdata)):
    if i % 15 == 0:
        fetal1.append(sortdata[i])
print(fetal1)

target = []
for i in fetal1[:100]:
    target.append(str(i) + '.jpeg')
print(target)

for i in target:
    with open('sampling1.txt', 'a+') as f:
        f.write(i + '\n')

for i in target:
    for j in os.listdir(
            'D:\savergb4training_0701-store-rgb\savergb4training_0701-store-rgb\savergb-190701-store_select_5-1'):
        if j == i:
            shutil.copy(
                'D:\savergb4training_0701-store-rgb\savergb4training_0701-store-rgb\savergb-190701-store_select_5-1/' + i,
                'data1')
