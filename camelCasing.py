# Complete the solution so that the function will break up camel casing, using a space between words.

# Link: https://www.codewars.com/kata/5208f99aee097e6552000148/python
def camel_case_breaker(text):
    final_string = ''
    for letter in text:
        if letter.isupper():
            final_string += ' ' + letter
        else:
            final_string += letter
    return final_string


if __name__ == '__main__':
    print(camel_case_breaker('helloWorldAndBye'))
