def rr():
    print("RR")

def npsjf():
    def calculate(numOfProcesses, arrivalTime, burstTime, completed, currentTime, processCount, finishingTime, turnaroundTime, waitingTime, avgWaitingTime, avgTurnaroundTime):

        while processCount < numOfProcesses:
            shortestJob = -1
            shortestBurstTime = float('inf')

            for i in range(numOfProcesses):
                if not completed[i] and arrivalTime[i] <= currentTime and burstTime[i] < shortestBurstTime:
                    shortestBurstTime = burstTime[i]
                    shortestJob = i

            if shortestJob != -1:
                finishingTime[shortestJob] = currentTime + burstTime[shortestJob]
                currentTime = finishingTime[shortestJob]
                turnaroundTime[shortestJob] = finishingTime[shortestJob] - arrivalTime[shortestJob]
                waitingTime[shortestJob] = turnaroundTime[shortestJob] - burstTime[shortestJob]
                avgWaitingTime += waitingTime[shortestJob]
                avgTurnaroundTime += turnaroundTime[shortestJob]
                completed[shortestJob] = True
                processCount += 1

                # Display the process in the Gantt Chart
                print(f"  P{shortestJob}  |", end='')

            else:
                # If no eligible process, increment time
                currentTime += 1

        avgWaitingTime /= numOfProcesses
        avgTurnaroundTime /= numOfProcesses

        return avgWaitingTime, avgTurnaroundTime

    while True:
        try:
            numOfProcesses = int(input("Enter the number of processes: "))
            break
        except ValueError as ve:
            print("You have entered wrong value.\n")

    print()

    #allocate size according to number of processes
    arrivalTime = [0] * numOfProcesses
    burstTime = [0] * numOfProcesses
    waitingTime = [0] * numOfProcesses
    finishingTime = [0] * numOfProcesses
    turnaroundTime = [0] * numOfProcesses
    avgWaitingTime = 0
    avgTurnaroundTime = 0

    for i in range(numOfProcesses):

        while True:
            try:
                print(f"Enter details for Process P{i}:")
                inputBurstTime = int(input("Burst Time: "))
                inputArrivalTime = int(input("Arrival Time: "))
                break
            except ValueError as ve:
                print("You have entered wrong value.\n")
                inputBurstTime = 0
                inputArrivalTime = 0

        burstTime[i] = inputBurstTime
        arrivalTime[i] = inputArrivalTime
        print()

    # Sort processes by their arrival time
    for i in range(numOfProcesses - 1):
        for j in range(numOfProcesses - i - 1):
            if arrivalTime[j] > arrivalTime[j + 1]:
                # Swap arrival time and burst time
                arrivalTime[j], arrivalTime[j + 1] = arrivalTime[j + 1], arrivalTime[j]
                burstTime[j], burstTime[j + 1] = burstTime[j + 1], burstTime[j]

    currentTime = 0

    print("\nGantt Chart:")
    print("|", end='')

    completed = [False] * numOfProcesses
    processCount = 0

    avgWaitingTime, avgTurnaroundTime = calculate(numOfProcesses, arrivalTime, burstTime, completed, currentTime, processCount, finishingTime, turnaroundTime, waitingTime, avgWaitingTime, avgTurnaroundTime)

    # Displaying the table
    print()
    print("\nDetails Table:")
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print("Process\t      Arrival Time\t      Burst Time\t      Finishing Time\t      Turnaround Time\t      Waiting Time")
    print("--------------------------------------------------------------------------------------------------------------------------------")

    for i in range(numOfProcesses):
        print(f"P{i}\t\t{arrivalTime[i]}\t\t\t {burstTime[i]}\t\t\t {finishingTime[i]}\t\t\t  {turnaroundTime[i]}\t\t\t{waitingTime[i]}")

    print("---------------------------------------------------------------------------------------------------------------------------------")
    print(f"Total Average Waiting Time: {avgWaitingTime}")
    print(f"Total Average Turnaround Time: {avgTurnaroundTime}")

def psjf():
    def calculate(numOfProcesses, arrivalTime, burstTime, tempBurstTime, completed, currentTime, processCount, finishingTime, turnaroundTime, waitingTime, avgWaitingTime, avgTurnaroundTime, ganttChart):

        while processCount < numOfProcesses:
            shortestJob = -1
            shortestBurst = float('inf')

            for i in range(numOfProcesses):
                if not completed[i] and arrivalTime[i] <= currentTime and tempBurstTime[i] < shortestBurst:
                    shortestBurst = tempBurstTime[i]
                    shortestJob = i

            if shortestJob != -1:
                if ganttChart and ganttChart[-1] != f"P{shortestJob}":
                    ganttChart.append(f"P{shortestJob}")
                elif not ganttChart:
                    ganttChart.append(f"P{shortestJob}")

                tempBurstTime[shortestJob] -= 1
                if tempBurstTime[shortestJob] == 0:
                    finishingTime[shortestJob] = currentTime + 1
                    completed[shortestJob] = True
                    processCount += 1
                    turnaroundTime[shortestJob] = finishingTime[shortestJob] - arrivalTime[shortestJob]
                    waitingTime[shortestJob] = turnaroundTime[shortestJob] - burstTime[shortestJob]
                    avgWaitingTime += waitingTime[shortestJob]
                    avgTurnaroundTime += turnaroundTime[shortestJob]
            else:
                ganttChart.append("-")

            currentTime += 1

        if numOfProcesses > 0:
            avgWaitingTime /= numOfProcesses
            avgTurnaroundTime /= numOfProcesses

        return avgWaitingTime, avgTurnaroundTime

    def display_gantt_chart(gantt_chart):
        print("\nGantt Chart:")
        print("------------------------------------------------------------------------")
        print("|", end=" ")
        for proc in gantt_chart:
            print(f"{proc} |", end=" ")
        print("\n------------------------------------------------------------------------")

    while True:
        try:
            numOfProcesses = int(input("Enter the number of processes: "))
            break
        except ValueError as ve:
            print("You have entered wrong value.\n")

    print()

    arrivalTime = [0] * numOfProcesses
    burstTime = [0] * numOfProcesses
    tempBurstTime = [0] * numOfProcesses
    waitingTime = [0] * numOfProcesses
    finishingTime = [0] * numOfProcesses
    turnaroundTime = [0] * numOfProcesses
    avgWaitingTime = 0
    avgTurnaroundTime = 0
    ganttChart = []  # Dynamic size for Gantt Chart

    for i in range(numOfProcesses):

        while True:
            try:
                print(f"Enter details for Process P{i}:")
                inputBurstTime = int(input("Burst Time: "))
                inputArrivalTime = int(input("Arrival Time: "))
                break
            except ValueError as ve:
                print("You have entered wrong value.\n")
                inputBurstTime = 0
                inputArrivalTime = 0

        burstTime[i] = inputBurstTime
        tempBurstTime[i] = burstTime[i]
        arrivalTime[i] = inputArrivalTime
        print()

    currentTime = 0
    completed = [False] * numOfProcesses
    processCount = 0

    avgWaitingTime, avgTurnaroundTime = calculate(numOfProcesses, arrivalTime, burstTime, tempBurstTime, completed, currentTime, processCount, finishingTime, turnaroundTime, waitingTime, avgWaitingTime, avgTurnaroundTime, ganttChart)

    # Displaying the Gantt Chart
    display_gantt_chart(ganttChart)

    # Displaying the table
    print("\nDetails Table:")
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("Process\t      Arrival Time\t      Burst Time\t      Finishing Time\t      Turnaround Time\t      Waiting Time")
    print("--------------------------------------------------------------------------------------------------------------------------------------------")

    for i in range(numOfProcesses):
        print(f"P{i}\t\t{arrivalTime[i]}\t\t\t {burstTime[i]}\t\t\t {finishingTime[i]}\t\t\t  {turnaroundTime[i]}\t\t\t{waitingTime[i]}")

    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print(f"Total Average Waiting Time: {avgWaitingTime}")
    print(f"Total Average Turnaround Time: {avgTurnaroundTime}")

def pri():
    def calculate(numOfProcesses, arrivalTime, burstTime, priority, completed, currentTime, processCount, finishingTime, turnaroundTime, waitingTime, avgWaitingTime, avgTurnaroundTime):

        while processCount < numOfProcesses:
            highestPriorityJob = -1
            highestPriority = float('inf')

            for i in range(numOfProcesses):
                if not completed[i] and arrivalTime[i] <= currentTime and priority[i] < highestPriority:
                    highestPriority = priority[i]
                    highestPriorityJob = i

            if highestPriorityJob != -1:
                # If burst time is the same, choose FCFS
                samePriorityCount = 0
                for i in range(numOfProcesses):
                    if not completed[i] and arrivalTime[i] <= currentTime and priority[i] == highestPriority and burstTime[i] == burstTime[highestPriorityJob]:
                        samePriorityCount += 1

                if samePriorityCount > 1:
                    # If multiple processes have the same priority and burst time, choose FCFS
                    for i in range(numOfProcesses):
                        if not completed[i] and arrivalTime[i] <= currentTime and priority[i] == highestPriority and burstTime[i] == burstTime[highestPriorityJob]:
                            highestPriorityJob = i
                            break

                finishingTime[highestPriorityJob] = currentTime + burstTime[highestPriorityJob]
                currentTime = finishingTime[highestPriorityJob]
                turnaroundTime[highestPriorityJob] = finishingTime[highestPriorityJob] - arrivalTime[highestPriorityJob]
                waitingTime[highestPriorityJob] = turnaroundTime[highestPriorityJob] - burstTime[highestPriorityJob]
                avgWaitingTime += waitingTime[highestPriorityJob]
                avgTurnaroundTime += turnaroundTime[highestPriorityJob]
                completed[highestPriorityJob] = True
                processCount += 1

                print(f"  P{highestPriorityJob}  |", end='')

            else:
                currentTime += 1

        avgWaitingTime /= numOfProcesses
        avgTurnaroundTime /= numOfProcesses

        return avgWaitingTime, avgTurnaroundTime

    while True:
        try:
            numOfProcesses = int(input("Enter the number of processes: "))
            break
        except ValueError as ve:
            print("You have entered wrong value.\n")

    print()

    arrivalTime = [0] * numOfProcesses
    burstTime = [0] * numOfProcesses
    waitingTime = [0] * numOfProcesses
    finishingTime = [0] * numOfProcesses
    turnaroundTime = [0] * numOfProcesses
    priority = [0] * numOfProcesses
    avgWaitingTime = 0
    avgTurnaroundTime = 0

    for i in range(numOfProcesses):

        while True:
            try:
                print(f"Enter details for Process P{i}:")
                inputBurstTime = int(input("Burst Time: "))
                inputArrivalTime = int(input("Arrival Time: "))
                inputPriority = int(input("Priority: "))
                break
            except ValueError as ve:
                print("You have entered wrong value.\n")
                inputBurstTime = 0
                inputArrivalTime = 0
                inputPriority = 0

        burstTime[i] = inputBurstTime
        arrivalTime[i] = inputArrivalTime
        priority[i] = inputPriority
        print()

    # Sort processes by their arrival time and priority
    for i in range(numOfProcesses - 1):
        for j in range(numOfProcesses - i - 1):
            if arrivalTime[j] > arrivalTime[j + 1] or (arrivalTime[j] == arrivalTime[j + 1] and priority[j] > priority[j + 1]):
                # Swap arrival time, burst time, and priority
                arrivalTime[j], arrivalTime[j + 1] = arrivalTime[j + 1], arrivalTime[j]
                burstTime[j], burstTime[j + 1] = burstTime[j + 1], burstTime[j]
                priority[j], priority[j + 1] = priority[j + 1], priority[j]

    currentTime = 0

    print("\nGantt Chart:")
    print("|", end='')

    completed = [False] * numOfProcesses
    processCount = 0

    avgWaitingTime, avgTurnaroundTime = calculate(numOfProcesses, arrivalTime, burstTime, priority, completed, currentTime, processCount, finishingTime, turnaroundTime, waitingTime, avgWaitingTime, avgTurnaroundTime)

    # Displaying the table
    print()
    print("\nDetails Table:")
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print("Process\t      Arrival Time\t      Burst Time\t      Priority\t      Finishing Time\t      Turnaround Time\t      Waiting Time")
    print("--------------------------------------------------------------------------------------------------------------------------------")

    for i in range(numOfProcesses):
        print(f"P{i}\t\t{arrivalTime[i]}\t\t\t {burstTime[i]}\t\t\t {priority[i]}\t\t\t {finishingTime[i]}\t\t\t  {turnaroundTime[i]}\t\t\t{waitingTime[i]}")

    print("---------------------------------------------------------------------------------------------------------------------------------")
    print(f"Total Average Waiting Time: {avgWaitingTime}")
    print(f"Total Average Turnaround Time: {avgTurnaroundTime}")

print("Please choose a scheduling algorithm.")
print("1. Round Robin")
print("2. Non-Preemptive Shortest Job First")
print("3. Pre-emptive Shortest Job First")
print("4. Non-Preemptive Priority")

while True:
    try:
        selection = int(input("Please enter a number (1-4): "))
        if selection < 1 or selection > 4:
            print("Number out of range.\n")
        else:
            if selection ==  1:
                print()
                rr()
            elif selection == 2:
                print()
                npsjf()
            elif selection == 3:
                print()
                psjf()
            else:
                print()
                pri()
            break
    except ValueError as ve:
        print("You have entered wrong value.\n")