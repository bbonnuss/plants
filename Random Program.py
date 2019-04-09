def random_number(n):
    import time
    x = time.time()
    x %= 1
    x *= 100000000000000
    x //= 100000000000
    #print (x)
    count = 1
    
    while count <= n:
        if x / 1000 <= (count / n):
            return count
        count += 1
        


def main():
    while True:
        try:
            n = int(input("How many number you want? : "))
            print ("Random Number 1 - %d"%n)
            break
        except ValueError:
            print ("Enter only countable number")
            continue
    control = 0
    while True:
        if control == 0:
            print ("====================")
            print ("%d"%random_number(n))
            print ("====================")
            control = 1

        x = input ("Random Again? (y/n)")
        if x == "y":
            print ("====================")
            print ("%d"%random_number(n))
            print ("====================")
            continue
        elif x == "n":
            break
        
        
if __name__ == '__main__':  
    main()


