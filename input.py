n = input("n:")
list_ = []
for i in range(int(n)):
    list_.append(list(map(int,input("i:").split())))
#list1_ = [int(i) for i in list_]
#list2_ = list(map(int, list_))
print(list_)
