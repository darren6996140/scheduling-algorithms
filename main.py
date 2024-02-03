""""
print("Please choose a scheduling algorithm.")

print("1. Round Robin")
print("2. Non-Preemptive Shortest Job First")
print("3. Pre-emptive Shortest Job First")
print("4. Non-Preemptive Priority")
"""

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

    numOfProcesses = int(input("Enter the number of processes: "))
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
        print(f"Enter details for Process P{i}:")
        burstTime[i] = int(input("Burst Time: "))
        arrivalTime[i] = int(input("Arrival Time: "))
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
    print("P SJF")

def pri():
    print("priority")

npsjf()

"""
while True:
    try:
        selection = int(input("Please enter a number (1-4): "))
        if selection < 1 or selection > 4:
            print("Number out of range.")
        else:
            if selection ==  1:
                rr()
            elif selection == 2:
                npsjf()
            elif selection == 3:
                psjf()
            else:
                pri()
            break
    except ValueError as ve:
        print("You have entered wrong value.")
"""