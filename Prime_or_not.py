def Prime(num):
    if num==1:
        print("1 is not a prime number.")
    else:
        list_prime_checker = range(1,num)
        k=0
        for i in list_prime_checker:
            if num%i==0:
                k+=1
            else:
                continue
        if k>1:
            print(str(num)+" is not a prime number.")
        else:
            print(str(num)+" is a prime number!")

Prime(1)

Prime(34)

Prime(1287)

Prime(11)

Prime(13)
