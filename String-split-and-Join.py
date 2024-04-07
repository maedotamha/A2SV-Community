def split_and_join(line):
    splitted = line.split(" ")
    result = "-".join(splitted)
    return(result)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
