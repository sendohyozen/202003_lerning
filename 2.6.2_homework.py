# 班级同学的成绩存放在列表中，list=[523, 435, 712, 566, 613, 675, 620, 689, 643],请将列表内的成绩从大到小进行排序。
# 提示：列表排序问一下度娘。
list1=[523, 435, 712, 566, 613, 675, 620, 689, 643]
print(list1)
list1.sort()
print(list1)



# 现有一个列表，存放了小区邻居的工资收入，list=[10000,8500,
# 9000,7000,8000,8000,9000,20000,15000,16000,5000] ，算一下小区邻居的平均工资收入。
list1=[10000,8500,9000,7000,8000,8000,9000,20000,15000,16000,5000]
sum = 0
for i in list1:
    # print(i)
    sum = sum + i

print(sum)
mean= sum/len(list1)
print(len(list1))
print(mean)