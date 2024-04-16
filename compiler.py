import re
import os.path

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def remove_excess_space_and_comments(code):
    cleaned_code = []
    for line in code.split('\n'):
        line = line.strip()
        if line and not line.startswith('#'):
            cleaned_code.append(line)
    return cleaned_code

def tokenize_code(code):
    tokens = {
        'Keywords': [],
        'Identifiers': [],
        'Operators': [],
        'Delimiters': [],
        'Literals': []
    }
    for line in code:
        for keyword in re.findall(r'\b(def|return|print)\b', line):
            tokens['Keywords'].append(keyword)
        for identifier in set(re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', line)) - set(re.findall(r'\b(def|return|print)\b', line)):
            tokens['Identifiers'].append(identifier)
        for operator in re.findall(r'[=+]', line):
            tokens['Operators'].append(operator)
        for delimiter in re.findall(r'[\(\):]', line):
            tokens['Delimiters'].append(delimiter)
        for literal in re.findall(r'\b\d+\b', line):
            tokens['Literals'].append(literal)
    return tokens

def print_output(code):
    for line in code:
        print(line)

def print_tabular_form(tokens):
    print("\nTokenized Code:\n")
    print("{:<12} {}".format("Category", "Tokens"))
    for category, token_list in tokens.items():
        print("{:<12} {}".format(category, ', '.join(token_list)))

if __name__ == "__main__":
    file_path = os.path.abspath(input("Enter sample input(includes file extension): "))
    if os.path.exists(file_path):
        lines = read_input_file(file_path)
        cleaned_lines = remove_excess_space_and_comments(lines)
        print("After removing excess space and comments:\n")
        print_output(cleaned_lines)
        tokens = tokenize_code(cleaned_lines)
        print_tabular_form(tokens)
    else:
        print("Error: file doesn't exist")