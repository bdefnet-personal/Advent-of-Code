#The levels are either all increasing or all decreasing.
#Any two adjacent levels differ by at least one and at most three.

ALLOW_ONE_UNSAFE = True

def is_good_report(report: list[int]) -> bool:
    
    prev = report[0]
    prev_sign = "POS" if report[1] - prev > 0 else "NEG"
    for num in report[1:]:
        diff = num - prev
        if abs(diff) > 3 or diff == 0:
            return False
        
        curr_sign = "POS" if diff > 0 else "NEG"
        if curr_sign != prev_sign:
            return False

        prev = num
        prev_sign = curr_sign

    return True

with open('input.txt', 'r') as f:
    content = f.read()

    num_good_reports = 0    
    for reportRaw in content.strip().split('\n'):
        report = list(map(int, reportRaw.split()))

        if is_good_report(report):
            num_good_reports += 1
        elif ALLOW_ONE_UNSAFE:
            for i in range(len(report)):
                if i == 0:
                    if is_good_report(report[1:]):
                        num_good_reports += 1
                        break
                elif i == len(report) - 1:
                    if is_good_report(report[:-1]):
                        num_good_reports += 1
                        break
                else:
                    if is_good_report(report[0:i] + report[i+1:]):
                        num_good_reports += 1
                        break

    print(f"Num Good Reports: {num_good_reports}")

