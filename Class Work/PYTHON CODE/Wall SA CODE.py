# Room paint CODE
units = int(input("1:Imperial, 2:Metric -->  "))

if units == 1:
    meas = input("Enter the Measurement you want to use. inches/feet --> ")
elif units ==2:
    print('Enter the measurement you are using. cm/m -->  ')
    meas = input()
else:
    print("Invalid Input")

print('Enter Height')
height = float(input())
print('Enter Length')
length = float(input())
print('Enter Width')
width = float(input())

#Total surface area of walls =

SA = length*height*2 + width*height*2
CSA = length*width
print('Total wall surface area is', SA, meas)
print('Ceiling Surface area is', CSA, meas)
input()
