def choice(past):
    if past == []:
        return 'C'
    else:
        return past[-1]

def main():
    choice()
    print(choice)

if __name__ == "__main__":
    main()