def flexible_calculator(operation, data_type, *numbers, **kwargs):
    if len(numbers) == 0:
        return None
    
    result = data_type(numbers[0])
    
    for i in range(1, len(numbers)):
        if operation == "ADD":
            result += data_type(numbers[i])
        elif operation == "SUB":
            result -= data_type(numbers[i])
        elif operation == "MUL":
            result *= data_type(numbers[i])
        elif operation == "DIV":
            divisor = data_type(numbers[i])
            if divisor == 0:
                return None  # Return None if division by zero
            result /= divisor
    
    return result


if __name__ == "__main__":
    print(f"flexible_calculator('ADD', int, 1) = {flexible_calculator('ADD', int, 1)}")
    print(f"flexible_calculator('ADD', int, 1, 2) = {flexible_calculator('ADD', int, 1, 2)}")
    print(f"flexible_calculator('ADD', int, 1, 2, 3, 4) = {flexible_calculator('ADD', int, 1, 2, 3, 4)}")
    print(f"flexible_calculator('MUL', int, 2, 3, 4) = {flexible_calculator('MUL', int, 2, 3, 4)}")
    print(f"flexible_calculator('DIV', float, 10, 5, 2) = {flexible_calculator('DIV', float, 10, 5, 2)}")
    print(f"flexible_calculator('DIV', float, 5, 0) = {flexible_calculator('DIV', float, 5, 0)}")