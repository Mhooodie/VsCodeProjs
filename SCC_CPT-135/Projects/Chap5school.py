def main():
    num = input()
    num_len = len(num)
    num_len2 = num_len // 2
    num_front = 0
    num_back = num_len - 1
    num_score = 0

    while num_front < num_len2:
        if num[num_front] == num[num_back]:
            num_front += 1
            num_back -= 1
            num_score += 1
        else:
            break

    if num_score == num_len2:
        print("It is Symmetrical!")
    else:
        print("It is not Symmetrical")

if __name__ == "__main__":
    main()