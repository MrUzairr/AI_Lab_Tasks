def balance_brackets(s):
    open_bracket_count = 0
    close_bracket_count = 0

    for char in s:
        if char == '(':
            open_bracket_count += 1
        elif char == ')':
            if open_bracket_count > 0:
                open_bracket_count -= 1
            else:
                close_bracket_count += 1

    balanced_sequence = '(' * close_bracket_count + s + ')' * open_bracket_count

    return balanced_sequence

input_sequence = "(a+b(c)"
balanced_sequence = balance_brackets(input_sequence)
print("Input:", input_sequence)
print("Output:", balanced_sequence)
