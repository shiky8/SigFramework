import attack_ss7 , test

def main_cli():
    print(test.logo())
    print("\033[33m[-][-]\033[0m\t\tSignaling Exploitation Framework\t")
    print("\033[33m[-][-]\033[0m\t\tIt is an modefied vertion of:\033[31m Sigploit 1.1\033[0m\t\t")
    print("\033[33m[-][-]\033[0m\t\tAuthor:\033[32mMohamed Shahat(@shiky8)\033[0m\t")
    print()
    while True:
        print(("0) SS7 Simulator".rjust(8) + "\t\t2G/3G Voice and SMS attacks"))
        print(("1) SS7 Attack".rjust(8) + "\t\t2G/3G Voice and SMS attacks"))
        print(("2) to exit ".rjust(8)))
        choice = str(input("\033[34msig\033[0m\033[37m>\033[0m "))
        if( choice=="0" ):
            test.main()
            break
        elif(choice=="1"):
            attack_ss7.main()
            break
        elif(choice=="exit" or choice=="2"):
            exit(0)

if __name__ == "__main__":
    main_cli()

    


