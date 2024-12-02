file = 'input.txt'

with open(file, 'r') as handle:
    arr = handle.readlines()

cleaned_input = []

for report in arr:
    cleaned_report = report.strip()
    split_report = cleaned_report.split(' ')
    report_as_int = []
    for num in split_report:
        report_as_int.append(int(num))

    cleaned_input.append(report_as_int)


def is_valid_report(report):

    def check_valid(arr):
        # Check if the levels are either all increasing or all decreasing
        is_increasing = all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))
        is_decreasing = all(arr[i] > arr[i + 1] for i in range(len(arr) - 1))
        is_monotonic = is_increasing or is_decreasing

        # Check if the difference between adjacent levels is valid
        is_difference_valid = all(1 <= abs(arr[i] - arr[i + 1]) <= 3 for i in range(len(arr) - 1))

        return is_monotonic and is_difference_valid

    if check_valid(report):
        return True

    # remove this loop to get solution to part 1.
    for i in range(len(report)):
        mod_list = report[:i] + report[i + 1:]
        if check_valid(mod_list):
            return True


count_safe_reports = 0

for report in cleaned_input:
    if is_valid_report(report):
        count_safe_reports += 1


print(count_safe_reports)
