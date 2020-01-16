# Sunny Vinay
# timetable.py
# Creates a school timetable for six classes based on user input for teachers

# dictionary with teacher number and their subject
teacherSubjects = {}
# dictionary with teacher number and their amount of periods
teacherPeriods = {}
# dictionary with teacher number and their used periods
teacherUsedPeriods = {}
# array made of six dictionaries representing which teacher a class has for a certain subject
teachersForClass = [] 
# array made of six dictionaries representing which teacher a class has for a certain period
schedule  = [] 

numOfTeachers = input("How many teachers are there? ")
for t in range(1, int(numOfTeachers)+1):
    currentSubject = input("Enter the subject for Teacher " + str(t) + ": ")
    teacherSubjects[t] = currentSubject
    
    currentPeriods = input("Now enter the max number of periods for Teacher " + str(t) + ": ")
    teacherPeriods[t] = int(currentPeriods)
    teacherUsedPeriods[t] = 0

currentClass = 0
currentPeriod = 1
notPossible = False
counter = 0

def printTimeTable():
    print()
    periodNumber = 1
    classNumber = 1
    for classSchedule in schedule:
        print("Class " + str(classNumber) + ": ")
        print("Periods 1-4 in order")
        for day in range(1, 6):
            print("Day " + str(day) + " | " 
            + " " + teacherSubjects[classSchedule[periodNumber]] + "-T" + str(classSchedule[periodNumber]) + ", "
            + " " + teacherSubjects[classSchedule[periodNumber + 1]] + "-T" + str(classSchedule[periodNumber + 1]) + ", "
            + " " + teacherSubjects[classSchedule[periodNumber + 2]] + "-T" + str(classSchedule[periodNumber + 2]) + ", "
            + " " + teacherSubjects[classSchedule[periodNumber + 3]] + "-T" + str(classSchedule[periodNumber + 3]))
            periodNumber = periodNumber + 4
        print()  
        periodNumber = 1
        classNumber = classNumber + 1 

while True:
    if notPossible:
        print("Schedule not possible")
        break
    
    if currentClass == 6:
        printTimeTable()
        break
    
    for teacher in teacherSubjects:
        if currentPeriod == 21:
            currentPeriod = 1
            currentClass = currentClass + 1
        if currentClass == 6:
            break
        subject = teacherSubjects[teacher]
        amountOfPeriods = teacherPeriods[teacher]
        if len(teachersForClass) != currentClass:
            teacherDict = teachersForClass[currentClass]
        else:
            teacherDict = {}
            teachersForClass.append(teacherDict)
            
        if len(schedule) != currentClass:
            scheduleDict = schedule[currentClass]
        else:
            scheduleDict = {}
            schedule.append(scheduleDict)
        counter = counter + 1
        if subject not in teacherDict or teacher == teacherDict[subject]:
            if teacherUsedPeriods[teacher] < teacherPeriods[teacher]:
                breakLoop = False
                for cl in range(currentClass):
                    dict1 = schedule[cl]
                    if currentPeriod in dict1 and teacher == dict1[currentPeriod]:
                        breakLoop = True
                if breakLoop:
                    continue
                else:
                    scheduleDict[currentPeriod] = teacher
                    teacherUsedPeriods[teacher] = teacherUsedPeriods[teacher] + 1
                    if subject not in teacherDict:
                        teacherDict[subject] = teacher
                    currentPeriod = currentPeriod + 1
                    counter = 0
                       
    if counter >= len(teacherSubjects):
        notPossible = True

