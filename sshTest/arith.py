"""
def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_operands = []
    operators = []
    second_operands = []

    for problem in problems:
        parts = problem.split()

        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not parts[0].isdigit() or not parts[2].isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        first_operands.append(parts[0])
        operators.append(parts[1])
        second_operands.append(parts[2])

    arranged_top_line = []
    arranged_bottom_line = []
    arranged_dash_line = []
    arranged_answer_line = []

    for i in range(len(problems)):
        num1 = first_operands[i]
        op = operators[i]
        num2 = second_operands[i]

        max_width = max(len(num1), len(num2)) + 2

        arranged_top_line.append(num1.rjust(max_width))
        arranged_bottom_line.append(op + ' ' + num2.rjust(max_width - 2))
        arranged_dash_line.append('-' * max_width)

        if show_answers:
            if op == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            arranged_answer_line.append(answer.rjust(max_width))

    final_output = '    '.join(arranged_top_line) + '\n'
    final_output += '    '.join(arranged_bottom_line) + '\n'
    final_output += '    '.join(arranged_dash_line)

    if show_answers:
        final_output += '\n' + '    '.join(arranged_answer_line)

    return final_output

# --- Example Function Calls (for testing) ---
print(f'\n--- Example 1 (No Answers) ---')
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

print(f'\n--- Example 2 (With Answers) ---')
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

print(f'\n--- Example 3 (Too Many Problems Error) ---')
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))

print(f'\n--- Example 4 (Invalid Operator Error) ---')
print(arithmetic_arranger(["3 / 855", "3801 - 2"]))

print(f'\n--- Example 5 (Numbers Too Long Error) ---')
print(arithmetic_arranger(["24 + 85215", "3801 - 2"]))

print(f'\n--- Example 6 (Non-Digit Numbers Error) ---')
print(arithmetic_arranger(["98 + 3g5", "3801 - 2"]))

"""




def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_operands = []
    operators = []
    second_operands = []

    for problem in problems:
        parts = problem.split()

        num1_str = parts[0]
        operator = parts[1]
        num2_str = parts[2]

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not num1_str.isdigit() or not num2_str.isdigit():
            return 'Error: Numbers must only contain digits.'

        if len(num1_str) > 4 or len(num2_str) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        first_operands.append(num1_str)
        operators.append(operator)
        second_operands.append(num2_str)

    arranged_top_line = []
    arranged_bottom_line = []
    arranged_dash_line = []
    arranged_answer_line = []

    for i in range(len(problems)):
        num1 = first_operands[i]
        op = operators[i]
        num2 = second_operands[i]

        width = max(len(num1), len(num2)) + 2

        arranged_top_line.append(num1.rjust(width))
        arranged_bottom_line.append(op + ' ' + num2.rjust(width - 2))
        arranged_dash_line.append('-' * width)

        if show_answers:
            if op == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            arranged_answer_line.append(answer.rjust(width))

    result = '    '.join(arranged_top_line)
    result += '\n' + '    '.join(arranged_bottom_line)
    result += '\n' + '    '.join(arranged_dash_line)

    if show_answers:
        result += '\n' + '    '.join(arranged_answer_line)

    return result