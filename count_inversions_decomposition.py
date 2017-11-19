def count_inversions(data, x):
    for i in range(len(data)):
        new_list = []
        for j in range(len(data[x])):
                new_list.append(data[i].index(j+1)) if j+1 in data[i] else -1
        data[i] = new_list

    for i in range(len(data)):
        list_temp = []
        for j in range(len(data[x])):
            if i != x:
                list_temp.append(data[i].index(data[x][j])) if data[x][j] in data[i] else -1
        if list_temp:
            data[i] = list_temp

    inversions = []
    for i in range(len(data)):
        c = 0
        if i != x:
            left = data[i][:len(data[i]) // 2]
            right = data[i][len(data[i]) // 2:]
            for j in range(len(left)):
                for k in range(1, len(left) - j):
                    if left[j] == -1 or left[j+k] == -1:
                        continue
                    elif left[j] > left[j+k]:
                        left[j], left[j+k] = left[j+k], left[j]
                        c += 1
            for j in range(len(right)):
                for k in range(1, len(right) - j):
                    if left[j] == -1 or left[j+k] == -1:
                        continue
                    elif right[j] > right[j+k]:
                        right[j], right[j+k] = right[j+k], right[j]
                        c += 1
            t = 0
            n = 0

            for s in range(len(data[i])):

                if n == len(right):
                    data[i][s] = left[t]
                    t += 1
                elif t == len(left):
                    data[i][s] = right[n]
                    n += 1
                elif left[t] <= right[n]:
                    data[i][s] = left[t]
                    t += 1
                else:
                    data[i][s] = right[n]
                    n += 1
                    c += len(right)-t

            inversions.append([i, c])
            inversions.sort(key=lambda x: x[1])
        else:
            continue

    print(inversions)
    return inversions
