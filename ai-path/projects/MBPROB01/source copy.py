# https://pl.spoj.com/problems/MBPROB01/


from datetime import datetime

# var = "2009-11-09 15:58:14"
# print(var)

# data = datetime.strptime(var, "%Y-%m-%d %H:%M:%S")
# print("year:", data.year)
# print("month:", data.month)
# print("day:", data.day)
# print("hour:", data.hour)
# print("minute:", data.minute)
# print("second:", data.second)



# submission content = date - user, contest, task, success

submissionsSorted = {}
problems = {}

def func(user):
    while True:
        line = input()

        if line[0] == '\\':
            break

        line = line.split('|')
        task = line[3].strip()
        
        if task in my_dict:
            my_dict[task] += 1
        else:
            my_dict[task] = 1


while True:
    line = input()

    if line == "----- END OF DATA -----":
        break

    if line != "----- BEGIN OF DATA -----":
        continue
    
    line = input()

    line = line.split(' ')
    user = line[2].strip()

    print(user)


    input()
    input()
    input()

    # print("begin")

    res = 0
    my_dict = {}

    while True:
        line = input()

        if line[0] == '\\':
            break

        line = line.split('|')
        task = line[3].strip()
        
        if task in my_dict:
            my_dict[task] += 1
        else:
            my_dict[task] = 1

        # print(line)

    # print("end")

    for key, val in my_dict.items():
        # print(key, val)
        res += (2**(val - 10) - 1)

    print(res)

    break
