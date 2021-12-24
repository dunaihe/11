def distr(histogram, i):
    A_list = [0] * i
    min = min(histogram)
    max = max(histogram)
    g = (max - min) / i
    for k in histogram:
        index = int((k - min) / g)
        if (k - min) != 0 and (k - min) % g == 0:
            index -= 1
        A_list[int(index)] += 1
    return A_list


assert distr([1.25, 1, 2, 1.75], 2) == [2, 2]
