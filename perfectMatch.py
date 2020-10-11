#perfect match
#input xxxxyyyyyxyxyyxyyx
#output "balanced" if equal x and y, else output "not balanced"



myString = input()
xcount = 0
ycount = 0

for i in range(len(myString)):

    if myString[i] == 'x':
        xcount = xcount + 1
    if myString[i] == 'y':
        ycount = ycount+1

if xcount == ycount:
    print("Ahhh, perfectly balanced...")
else:
    print("Not balanced, Thanos mad.")
