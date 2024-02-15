from collections import deque

portions = [int(x) for x in input().split(", ")]
stamina = deque([int(x) for x in input().split(", ")])
conquered_peaks = []
counter = 0

peaks = [("Vihren", 80), ("Kutelo", 90), ("Banski Suhodol", 100), ("Polezhan", 60), ("Kamenitza", 70)]
starting_peaks = len(peaks)

while portions and stamina:
    current_portion = portions.pop()
    current_stamina = stamina.popleft()
    current_sum = current_portion + current_stamina
    if current_sum >= peaks[counter][1]:
        conquered_peaks.append(peaks[counter][0])
        counter += 1
        if counter > 4:
            break

if len(conquered_peaks) == starting_peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print(f"Conquered peaks: ")
    # print(f"{'\n'.join(conquered_peaks)}")
    for peak in conquered_peaks:
        print(peak)
