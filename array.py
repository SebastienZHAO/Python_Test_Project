students = ['zhao yi qian', "zhao cheng xiu"]
print(students)
print(students[0].title(), students[-1].title())

str_line1 = ["A1", "B1"]
str_line2 = ["A2", "B2"]
my_metrics = [str_line1, str_line2]
print(my_metrics[0][0], my_metrics[0][1], my_metrics[1][0], my_metrics[1][1])

print("len my_metrics is :", len(my_metrics))
new_message = students[1].upper() + " " + my_metrics[-2][-1]
print(new_message, '\n\n')

int_line1 = [11, 12]
int_line2 = [21, 22]
my_metrics = [int_line1, int_line2]
print(my_metrics[0][0], my_metrics[0][1], my_metrics[-1][0], my_metrics[-1][-1])

my_metrics = [int_line1, int_line2, "the third line"]
print(my_metrics)
print(my_metrics[2])
del my_metrics[2]
print(my_metrics)


new_message = students[0].title() + " " + str(my_metrics[-2][-2])
print(new_message)

my_metrics[0][1] = 'zhao zhen hui'
print(my_metrics[0][0], my_metrics[0][1].upper(), my_metrics[-1][0], my_metrics[-1][-1])
print(my_metrics)


students.append("zhang li li")
print(students)

str_line3 = ["A3", "B3"]
my_metrics.append(str_line3)
print(my_metrics)

motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)
motorcycles.insert(1, "ducati")
print(motorcycles)

#popped_motorcycle = motorcycles.pop()
#popped_motorcycle = motorcycles.pop(0)
#popped_motorcycle = motorcycles.pop(1)
#popped_motorcycle = motorcycles.pop(2)
popped_motorcycle = motorcycles.pop(3)

print(motorcycles)
print(popped_motorcycle)
#del motorcycles[1]
#print(motorcycles)

motorcycles.remove("yamaha")
print(motorcycles)

invite_member = ["lilian", "zoe", "theodore", "sebastien"]
print("invite guests below: \r\n", invite_member[0].title(), invite_member[1].title(),invite_member[2].title(),invite_member[3].title());
absent_guest = invite_member[-1]
print(absent_guest, "will be absent")
invite_member[-1] = "Janey"
print("send invitation to below persons:", invite_member)

invite_member.insert(0, "Benny")
invite_member.insert(2, "Henry")
invite_member.append("Joe")
print("I got a bigger table, come on babies:", invite_member)
invite_member.sort()
print("I need rearrange my guests in order of letter from A to Z:", invite_member)
#invite_member.sort(reverse = True)
#print("I need rearrange my guests in order of letter from Z to A:", invite_member)

print("sorted", sorted(invite_member, reverse = True))
print(invite_member)

print("I'm sorry, I can only invite two people to have a dinner!")
#popped_guest = invite_member.pop()
print("I'm sorry to inform ", invite_member.pop(), "that you will be absent as the dinner is cancelded")
#popped_guest = invite_member.pop()
print("I'm sorry to inform ", invite_member.pop(), "that you will be absent as the dinner is cancelded")
#popped_guest = invite_member.pop()
print("I'm sorry to inform ", invite_member.pop(), "that you will be absent as the dinner is cancelded")
#popped_guest = invite_member.pop()
print("I'm sorry to inform ", invite_member.pop(), "that you will be absent as the dinner is cancelded")
#popped_guest = invite_member.pop()
print("I'm sorry to inform ", invite_member.pop(), "that you will be absent as the dinner is cancelded")

print("Congrats,", invite_member[0], "will receive the invitation for dinner");
print("Congrats,", invite_member[1], "will receive the invitation for dinner");

del invite_member[0]
del invite_member[0]
print("invite_member list is :", invite_member)
