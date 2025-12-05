def binpack(items, S):
    items = sorted(items, reverse=True)
    bins = []

    for item in items:
        placed = False
        for b in bins:
            if sum(b) + item <= S:
                b.append(item)
                placed = True
                break
        if not placed:
            bins.append([item])
    return bins

if __name__ == "__main__":
    items = [9, 3, 3, 6, 10, 4, 6, 8, 6, 3]
    B = 10

    bins = binpack(items, B)

    for i in range(len(bins)):
        print(f"bin {i+1}: {bins[i]}")