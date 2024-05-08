def solution(prices):
    answer = []

    for i in range(len(prices)):
        price = prices[i]
        count = 0
        for j in range(i + 1, len(prices)):
            # print("i :", i, ", j :", j)

            if prices[j] >= price:
                # print("prices[j] :", prices[j], " >= price :", price)
                count += 1
            else:
                # print("prices[j] :", prices[j], "< price :", price)
                # print("break")
                count += 1
                break

        # print("append value", count)
        answer.append(count)

    return answer


# print(solution([3, 2, 1, 1]))
