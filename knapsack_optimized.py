def knapsack(items, weight):

    values = [[0] * (weight + 1) for i in range(2)]
    j = weight
    result = []
    #for_result = [0]*(len(items)+1)
    test = [0]*len(items)
    for i, (val, w) in enumerate(items):

        for capacity in range(weight + 1):
            if w > capacity:
                values[1][capacity] = values[0][capacity]
            else:
                if values[0][capacity - w] + val > values[0][capacity]:
                    test[items.index([val, w])] += 1
                values[1][capacity] = max(values[0][capacity], values[0][capacity - w] + val)
        print(values[1])
        '''if values[1][j] != values[0][j]:
            result.append([val, w])
            j -= w'''
        #for_result[i+1] = values[1][j]
        #print(values)
        values[0], values[1] = values[1], [0] * (weight + 1)
    #for_result = for_result[:-1]
    #print(for_result)
    print(test)
    #test.reverse()
    final = []
    size = len(items)
    maxweight = weight
    for i in range(len(test)):
        print(i, test[size-i-1], maxweight-j)

        if test[size-i-1] > maxweight - j:
            final.append(i)
            #print(items[size - i-1])
            j-= items[size - i-1][1]

    for i in range(len(final)):
        final[i] = size - 1 - final[i]

    final.reverse()
    print(final)
    #for i in range(len(items), 0, -1):

    #    if for_result[i] != for_result[i-1]:
    #        result.append(items[i - 1])
    #        j -= items[i - 1][1]

        #print(len(values[0]), len(values[1]))

        #print(values[0])
    total_value = values[0][-1]
    result = result
    #result.reverse()
    #print("here",for_result)
    result_items = []
    for i in result:
        result_items.append(items.index(i))

    print(total_value, final)
    # values[len(items)][weight]
    return total_value, final

knapsack([[7, 5], [8, 4], [9, 3], [10, 2], [1, 10]], 10)
