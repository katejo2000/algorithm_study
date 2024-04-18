def solution(n, times):
    start = 1
    end = max(times) * n

    while start <= end:
        sum = 0
        mid = (start + end) // 2

        for time in times:
            people = mid // time
            sum += people

        if sum < n:
            start = mid + 1
        else:
            end = mid - 1

    return start


# print(solution(6, [2, 5]))  # return 28
