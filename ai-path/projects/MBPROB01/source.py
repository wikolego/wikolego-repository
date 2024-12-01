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

def func(user, contest):
    while True:
        line = input()

        if line[0] == '\\':
            break

        line = line.split('|')
        date = datetime.strptime(line[2].strip(), "%Y-%m-%d %H:%M:%S")
        task = line[3].strip()
        success = line[4].strip()
        submissionsSorted[date] = [user, contest, task, success]

while True:
    line = input()

    if line != "----- BEGIN OF DATA -----":
        continue
    
    while True:
        line = input()
        
        if line == "----- END OF DATA -----":
            break

        if line.startswith("Submissions by") == False:
            continue

        line = line.split(' ')
        user = line[2].strip()
        contest = line[5].strip()
        
        input()
        input()
        input()

        func(user, contest)

    break
        
    # print(user)

# for key, val in submissionsSorted:
#     print(key.year, "-", val)

# print(submissionsSorted[datetime.strptime("2009-11-09 15:58:14", "%Y-%m-%d %H:%M:%S")])

res = 0

for key, val in sorted(submissionsSorted.items()):
    print(val)