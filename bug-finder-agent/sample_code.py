# sample_code.py --- with bugs

def divide(a, b):
    return a / b  # ⚠️ division by zero risk

def add_item(value, lst=[]):   # ⚠️ mutable default argument
    lst.append(value)
    return lst

def unsafe_eval(x):            # ⚠️ security vulnerability
    return eval(x)

def find_max(nums):            # ⚠️ missing return
    if not nums:
        return None
    max_v = nums[0]
    for n in nums:
        if n > max_v:
            max_v = n
    # missing return here

def main():
    print(divide(10, 0))
    print(add_item(1))
    print(add_item(2))
    print(unsafe_eval("2+3"))
    print(find_max([2, 7, 1]))

if __name__ == "__main__":
    main()
