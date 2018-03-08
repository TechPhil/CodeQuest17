file=open("ExampleInputs\Prob02.in.txt","r")
m1=3
m2=7
lines=file.readlines()
##print(lines)
lines.pop(0)
##print(lines)
for line in lines:
    line=line.strip()
    line=int(line)
    if line%m1==0 and line%m2!=0:
        print("LOCKHEED")
    elif line%m1!=0 and line%m2==0:
        print("MARTIN")
    elif line%m1==0 and line%m2==0:
        print("LOCKHEEDMARTIN")
    else:
        print(line)
    
