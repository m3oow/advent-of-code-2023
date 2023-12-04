result = 0

digits_as_text = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def takeSecond(elem):
    return elem[1]

with open("input.txt") as file:
    for line in file:
        result_vector = []

        # A value may be present multiple times inn a string
        # find has to be performed multiple times with a shift
        # to find multiple occurences
        for idx, value in enumerate(digits_as_text):
            index = 0
            while index < len(line):
                index = line.find(value, index)
                if index == -1:
                    break
                result_vector.append((idx, index))
                index += len(value)

        for idx, value in enumerate(digits):
            index = 0
            while index < len(line):
                index = line.find(value, index)
                if index == -1:
                    break
                result_vector.append((idx, index))
                index += len(value)
        
        sorted_result_vector = sorted(result_vector, key=takeSecond)
        
        temp_value = int(f"{str(sorted_result_vector[0][0])}{str(sorted_result_vector[-1][0])}")
        result += temp_value

        # print(f"{line} => {result_vector} => {sorted_result_vector} => {temp_value} => {result}")
    print(f"The result is: {result}")
