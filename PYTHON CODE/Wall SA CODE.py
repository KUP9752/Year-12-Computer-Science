# Room paint CODE
print('Enter the measurement you are using. cm/mm')
meas = input()
print('Enter Height')
height = int(input())
print('Enter Length')
length = int(input())
print('Enter Width')
width = int(input())

#Total surface area of walls =

SA = length*height*2 + width*height*2
print('Total surface area is', SA, meas)
input()
