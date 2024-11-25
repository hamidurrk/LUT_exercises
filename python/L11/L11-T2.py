# L11-T2: Potential pairs of elements
#
# Submitted by: Md Hamidur Rahman Khan
#

# def generate_pairs(lst: list, target:int) -> list:
#     return [f"{(lst[i], lst[j])}" for i in range(len(lst)) for j in range(i, len(lst)) if lst[i] + lst[j] == target]

def generate_pairs(lst: list, target: int, start: int = 0, ptr: int = 0, pairs: list = []) -> list:    
    if start >= len(lst):
        return pairs
    if ptr >= len(lst):
        return generate_pairs(lst, target, start + 1, start + 1, pairs)
    if lst[start] + lst[ptr] == target:
        pairs.append(f"{(lst[start], lst[ptr])}")
    return generate_pairs(lst, target, start, ptr + 1, pairs)

def get_numlist(numlist: list = []) -> list:
    user_input = input("Enter an integer (or type 'done' to finish input):\n")
    try:
        numlist.append(int(user_input))
        return get_numlist(numlist)
    except ValueError:
        return numlist if user_input == "done" else get_numlist(numlist)

def get_target() -> int:
    try:
        global target 
        target = int(input("Enter the target sum:\n"))
        return target
    except ValueError:
        return get_target() 

def main():
    pairs = generate_pairs(get_numlist(), get_target())
    print(f"Pairs with a sum of {target}:\n" + "\n".join(pairs)) if len(pairs) > 0 else print(f"No pairs found with a sum of {target}.")
    
main()