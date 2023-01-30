# qol = quality of life
# noy = number of years
# qaly = sum of quality of life
loop_times = int(input())
sum_of_life = 0
while loop_times > 0:
    line = input()
    qol , noy = line.split()
    qol = float(qol)
    noy = float(noy)
    qaly = qol * noy
    sum_of_life += qaly
    loop_times = loop_times - 1
print("%.2f" % sum_of_life)
