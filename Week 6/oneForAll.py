"""One For All"""

def main():
    """Main Function"""

    gen = int(input())

    if gen != 0:
        for i in range(gen):
            gen_name = input()
            if i % 2 == 0:
                print("-"*i, end="")
                print(gen_name, end="")
            else:
                print("*"*i, end="")
                print(gen_name, end="")

        print("_%d" %gen)
    else:
        print("")

main()
