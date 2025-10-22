def histogram(points, bins):
    n = len(points)
    k = len(bins)

    binslist = [0] * k
    pointer = 0

    for i in range(k):
        a, b = bins[i]
        while pointer < n and points[pointer] < b:
            pointer += 1
            binslist[i] += 1

        if pointer == n:
            break
    
    rbins = []
    for i in range(k):
        width = bins[i][1] - bins[i][0]
        count = binslist[i]

        if width > 0:
            density = count / (n * width)
        else:
            density = 0
        rbins.append(density)

    return rbins
