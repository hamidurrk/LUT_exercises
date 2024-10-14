def compress_string(input_string):
    if not input_string:
        return "", 0.0  
    
    compressed = []
    count = 1
    length = len(input_string)
    
    for i in range(1, length):
        if input_string[i] == input_string[i-1]:
            count += 1
        else:
            if count > 1:
                compressed.append(f"{input_string[i-1]}{count}")
            else:
                compressed.append(input_string[i-1])
            count = 1
    
    if count > 1:
        compressed.append(f"{input_string[-1]}{count}")
    else:
        compressed.append(input_string[-1])
    
    compressed_string = ''.join(compressed)
    compression_ratio = round(len(compressed_string) / length, 2)
    
    return compressed_string, compression_ratio

input_string = input(str("Give a string to compress:\n"))
compressed_string, compression_ratio = compress_string(input_string)
print(f"Compressed string: {compressed_string}")
print(f"Compressing ratio {compression_ratio}")
