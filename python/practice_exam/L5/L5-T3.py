def is_containing(part, container):
    count = 0
    for i in range(len(container)):
        for j in range(len(part)):
            if i < len(container):
                print(container[i], part[j])
                if container[i] == part[j]:
                    count += 1
                    i += 1
                else:
                    count = 0
        if count == len(part):
            return True
    return False

print(is_containing("part", "apartment"))
