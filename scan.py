import re

def extract_strings_recursive(test_str, tag):
    # finding the index of the first occurrence of the opening tag
    start_idx = test_str.find("<" + tag + ">")
 
    # base case
    if start_idx == -1:
        return []
 
    # extracting the string between the opening and closing tags
    end_idx = test_str.find("</" + tag + ">", start_idx)
    res = [test_str[start_idx+len(tag)+2:end_idx]]
 
    # recursive call to extract strings after the current tag
    res += extract_strings_recursive(test_str[end_idx+len(tag)+3:], tag)
 
    return res

# example usage
test_str = '<ln>4600063046 AccAssign 30 1 K 1100 2017.06.28 2017.06.05 2024.07.31 Z 2 601</ln>'
tag = "b"

def main():
    lines = extract_strings_recursive(test_str, "ln")
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()


