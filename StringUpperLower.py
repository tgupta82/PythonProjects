def main(input):
    output = ''
    for x in range(len(input)):
        if ((x + 1) % 2) == 0:
            output += input[x].upper()
        else:
            output += input[x].lower()
    return output


print(main("NeeravGupta"))