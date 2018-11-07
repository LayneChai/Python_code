#列表反转方法
# listNode = [1,2,3,4,5]
# newList = list(reversed(listNode))

#字符串反转方法
# result = s[::-1]



# s=[]
# for i in range(10001):
#     if i == 0:
#         s.append(1)
#     else:
#         s.append(s[i-1]+(i-1)*4+1)
# t = int(input().strip()) #去掉前后的空格
# for i in range(t):
#     a = int(input().strip())
#     print(s[a])

# a = int(input().strip())
# n = int(input().strip())
# flag = 0
# l = []
# while n:
#     d= (flag+a*n)%10
#     flag = int((flag+a*n)/10)  #向下取整
#     l.append(str(d))
#     # print(flag,d)
#     n-=1
#
# # print(l)
# while flag:
#     d=flag%10
#     flag=int(flag/10)
#     l.append(d)
# res = ''.join(l)
# res = res[::-1]  #字符串中的第一个位置是0  最后一个是-1 因为开始的时候是从0开始然后每-1走一步就是走到最后一个在向前走就反转了
# print(res)
# len = l.__len__()-1
# while len:
#     print(l[len])
#     len-=1

#下边的这种方法  在列表和字符串上都可用
# res = 'asdfg'
# # print(res[:])  # [:] 提取从开头（默认位置0）到结尾（默认位置-1）的整个字符串
# print(res[:2:-1]) #当吧步长设置为-1的时候且开始位置为空的时候 相当于从最后一个位置(_-1 )开始向前找

#列表反转的第二种方法
# listnode = [5,7,2,8,3,9]
# newlist = list(reversed(listnode))
# # newlist = sorted(listnode,reverse=True)  降序排列
# print(newlist)
