def parent_function (person,coin):
        #coin = 3  

        def function():
            nonlocal coin 
            coin -= 1

            if coin > 1:
                print("\n" + person  + " " "has" + str(coin) +" " "coins left")
            elif coin == 1 :
                print("\n" + person  + "has" + str(coin) + "coins left")
            else:
                 print("\n" + person  + "has" +" no coins left")

        return function
tommy = parent_function("aga", 10)
jenny = parent_function("jenny", 10)
tommy()
jenny(
     
)



