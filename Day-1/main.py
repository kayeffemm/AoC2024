file = "./input.txt"

left_arr = []
right_arr = []

with open(file, "r") as file:
    arr = file.readlines()
    print(arr)
    for line in arr:
        # Remove the space
        num1, num2 = line.split(" " * 3)

        # Make it an integer
        num1 = int(num1)
        num2 = int(num2.strip())

        # Add numbers to left and right lists
        left_arr.append(num1)
        right_arr.append(num2)

# Sort array
left_arr.sort()
right_arr.sort()

diff_sum = 0

for i in range(len(left_arr)):
    diff = abs(left_arr[i] - right_arr[i])
    diff_sum += diff

print(diff_sum) # solution part 1

sim_score_sum = 0

for num in left_arr:
    count = right_arr.count(num)
    sim_score_sum += (num * count)

print(sim_score_sum) # solution part 2