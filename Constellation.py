no_of_cols = int(input())
row_one = input().split()
row_two = input().split()
row_three = input().split()
i = 0
while i<no_of_cols-2:
    if row_one[i] == "#" and row_two[i] == "#" and row_three[i] == "#":
        print("#", end="")
        i += 1
        continue
    elif row_one[i] == "." and row_two[i] == "." and row_three[i] == ".":
        i += 1
        continue
    elif row_one[i] == row_one[i+2] == "." and row_one[i+1] == "*":
        if row_two[i] == row_two[i+1] == row_two[i+2] == "*":
            if row_three[i] == row_three[i+2] == "*" and row_three[i+1] == ".":
                print("A", end="")
                i += 3
                continue
    elif row_one[i] == row_one[i+2] == "*" and row_one[i+1] == ".":
        if row_two[i] == row_two[i+2] == "*" and row_two[i+1] == ".":
            if row_three[i] == row_three[i+1] == row_three[i+2] == "*": 
                print("U", end="")
                i += 3
                continue
    elif row_one[i] == row_one[i+1] == row_one[i+2] == "*":
        if row_two[i] == row_two[i+1] == row_two[i+2] == "*":
            if row_three[i] == row_three[i+1] == row_three[i+2] == "*":
                print("E", end="")
                i += 3
                continue
        elif row_two[i] == row_two[i+2] == "." and row_two[i+1] == "*":
            if row_three[i] == row_three[i+1] == row_three[i+2] == "*":
                print("I", end="")
                i += 3
                continue
        elif row_two[i] == row_two[i+2] == "*" and row_two[i+1] == ".":
            if row_three[i] == row_three[i+1] == row_three[i+2] == "*":
                print("O", end="")
                i += 3
                continue
    i += 1