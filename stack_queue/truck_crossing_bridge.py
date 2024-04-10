def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    count = 0
    total_weight = 0

    while truck_weights:
        car = truck_weights[0]
        out = bridge.pop(0)
        total_weight -= out

        if (total_weight + car) > weight:
            bridge.append(0)
            count += 1
        else:
            add = truck_weights.pop(0)
            bridge.append(add)
            count += 1
            total_weight += add

    count += bridge_length

    print(count)

    return count


solution(2, 10, [7, 4, 5, 6])
solution(100, 100, [10])
solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
