#solution(for predict()) = last element of each series and subtract them from the series's below it
#i.e start elem - start elem of prev and so on

def predict(history_arr: list[int]) -> int:
    diff_table = [history_arr]

    def check_zero(arr: list[int]) -> bool:
        #checks if the current diff array is only made up of zero
        #in my problem set the last sequence always ends with a zero so thats why im not checking all elements
        if arr[-1] == 0:
            return True
        return False

    def calc_diff_arr(arr: list[int]) -> list[int]:
        diff_arr = [0] * (len(arr) - 1)
        for i in range(len(arr) - 1):
            diff_arr[i] = arr[i + 1] - arr[i]
        return diff_arr

    def extrapolate(diff_table: list[list], current_index: int) -> int:
        if check_zero(diff_table[current_index]):
            return 0
        return diff_table[current_index][0] - extrapolate(diff_table, current_index + 1)

    while True:
        diff_table.append(calc_diff_arr(diff_table[-1]))
        if check_zero(diff_table[-1]):
            break

    return extrapolate(diff_table, 0)

with open("problem_set.txt", "r") as file:
    total = 0
    for i in file:
        total += predict([int(j) for j in i.strip().split(" ")])
    print(total)
