file_path = "day1a.txt"
units = [
    "0","1","2","3","4","5","6","7","8","9",
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]

dict = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}

def func():
    try:
        sum = 0
        with open(file_path, 'r') as file:
            for line in file:
                arr = [None, None]
                this_num = 0
                first_segment_size = float('inf')
                last_segment_size = float('inf')
                print(line)

                for unit in units:
                    splitarr = line.split(unit)
                    if len(splitarr) == 1: continue

                    if splitarr[0] == '':
                        arr[0] = int(unit) if unit.isdigit() else dict[unit]
                        first_segment_size = 0
                    else:
                        if len(splitarr[0]) < first_segment_size:
                            first_segment_size = len(splitarr[0])
                            arr[0] = int(unit) if unit.isdigit() else dict[unit]
                    
                    if splitarr[len(splitarr)-1] == '':
                        arr[1] = int(unit) if unit.isdigit() else dict[unit]
                        last_segment_size = 0
                    else:
                        if len(splitarr[-1]) < last_segment_size:
                            last_segment_size = len(splitarr[-1])
                            arr[1] = int(unit) if unit.isdigit() else dict[unit]

                    # print(arr)

                    # if arr[0] is not None and arr[1] is not None:
                    #     break

                print(arr)
                sum += (arr[0] * 10) + arr[1]

                # break



        print(sum)
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")


func()

# x = '9one9pjtnncsqzhcszp5'.split('one')

# print(x)