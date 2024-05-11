def solution(progresses, speeds):
    times = []
    result = []

    for task in progresses:
        speed = speeds.pop(0)

        time = (100 - task) // speed
        if (100 - task) % speed != 0:
            time += 1

        times.append(time)

    while times:
        if times[0] > 0:
            times = [val - times[0] for val in times]
        else:
            times.pop(0)
            count = 1
            while times:
                if times[0] <= 0:
                    count += 1
                    times.pop(0)
                else:
                    break
            result.append(count)

    return result


print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([93, 30, 55], [1, 30, 5]))
