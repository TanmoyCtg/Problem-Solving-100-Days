# #
# # def test5():
# #     stu = {'harsh': [25.0, 26.5, 28.0], 'anurag': [26.0, 28.0, 30.0]}
# #
# #     # print(len(stu))
# #
# #     for i in (list(stu.keys())):
# #         print(type(stu[i]))
# #     # h = stu['harsh']
# #     # a = stu['anurag']
# #     # print(h)
# #     # l = len(h)
# #     # anu = len(a)
# #     # sum = 0
# #     # for i in h:
# #     #     sum = sum + i
# #     # r = sum / l
# #     #
# #     # for i in a:
# #     #     sum = sum + i
# #     # rst = sum / anu
# #     #
# #     # if r < rst:
# #     #     return r
# #     # else:
# #     #     return rst
# #     #
# #     # print(round(r,2))
# #     # print(round(rst, 2))
# #
# # # test5()
# #
# # if __name__ == '__main__':
# #     N = int(input())
# #     empty_list = []
# #
# #     for _ in range(N):
# #
# #         s = input().split()
# #         cmd = s[0]
# #         args = s[1:]
# #
# #
# #     print(cmd)
# #     print(args)
# #     print(empty_list)
# #
# #
# #     # print(empty_list)
#
#
# thickness = int(input()) #This must be an odd number
# c = 'H'
#
# # #Top Cone
# for i in range(thickness+1):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#
# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#
#
# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))
#
# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
# #
#
# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# from collections import  defaultdict
#
# ordered_dictionary = defaultdict(int)
#
# print(ordered_dictionary)
import time, _thread

print('Start of program.')

def takeANap():

	time.sleep(5)
	print('Wake up!')

threadObj = _thread.start_new_thread(takeANap,())
print(threadObj)
print('End of program')

