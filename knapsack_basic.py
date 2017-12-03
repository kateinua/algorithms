def knapsack(items, weight):

    values = [None]*(weight+1)*len(items)
    j = weight
    result = []

    def total_value(i, j):
        if i == 0:
            return 0
        v, w = items[i - 1]
        if not values[(i-1)*(weight+1)+j]:
            values[(i-1)*(weight+1)+j] = total_value(i - 1, j)
        if w > j:
            return values[(i-1)*(weight+1)+j]
        else:
            return max(values[(i-1)*(weight+1)+j], total_value(i - 1, j - w) + v)

    for i in range(len(items), 0, -1):

        print("i", total_value(i, j), "i-1", total_value(i - 1, j))
        print("j", j)
        if total_value(i, j) != total_value(i - 1, j):

            result.append(items[i - 1])
            j -= items[i - 1][1]

    result.reverse()
    #print("here",result)
    result_items = []
    for i in result:
        result_items.append(items.index(i))

    print(total_value(len(items), weight), result_items)

    return total_value(len(items), weight), result_items

knapsack([[7, 5], [8, 4], [9, 3], [10, 2], [1, 10], [3, 15], [8, 10], [6, 4], [5, 3], [7, 3]], 20)
