# L05-T4: Compressed string
#
# Submitted by: Md Hamidur Rahman Khan
#

def compress_string(input_string : str):    
    prev, current, count, output = "", 0, 0, ""
    for char in input_string:
        if char == prev:
            current += 1
        else:
            if prev is not None:
                output = output + prev + str(current if current > 1 else "")
            prev = char
            current = 1  
        count += 1
        if count == len(input_string):
            output = output + prev + str(current if current > 1 else "")
    return output

input_string = input("Give a string to compress:\n")
compressed_string = compress_string(input_string)
print(f"Compressed string: {compressed_string}")
print(f"Compressing ratio {round(len(compressed_string) / len(input_string), 2)}")