print(''' 
 ,---,--. ,--,-'  '-|  ,---. ,---.,--,--,      ,---.,--.--.,---. `--',---. ,---,-'  '-. 
| .-. \  '  /'-.  .-|  .-.  | .-. |      \    | .-. |  .--| .-. |,--| .-. | .--'-.  .-' 
| '-' '\   '   |  | |  | |  ' '-' |  ||  |    | '-' |  |  ' '-' '|  \   --\ `--. |  |   
|  |-.-'  /    `--' `--' `--'`---'`--''--'    |  |-'`--'   `---.-'  /`----'`---' `--'   
`--' `---'                                    `--'             '---'                    
''')
#Getting input from user
n = int(input("Enter the number that you want convert into roman integer:"))
num = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
rom = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')

result = ''
#using for loop
for i in range(len(num)) :
    count = int(n / num[i])
    result += str(rom[i] * count)
    n -= num[i] * count
print(result)