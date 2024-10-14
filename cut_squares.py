def Solution(A, B):
    x = (A+B)//4  # First, combining the sticks and breaking them
    # If the square length is only from a single stick, then return it
    if x*4 <= max(A, B):
        return x
    # one part of the square is from one stick and rest is from another
    if x <= min(A, B) and x*3 <= max(A, B):
        return x
    # Two parts of square are from one stick and 2 parts from another.
    if x*2 <= min(A, B) and x*2 <= max(A, B):
        return x
    # If not reduce the stick length by 1
    return x-1


if __name__ == '__main__':
    print(Solution(13, 11))
    print(Solution(10, 21))
    print(Solution(2, 1))
    print(Solution(1, 8))
