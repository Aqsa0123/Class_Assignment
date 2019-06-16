while True:
    x=int(input("enter num 1:"))
    y=int(input("enter num 2:"))
    def func(num1,num2):
        ans=input('for sum of these number type 1 +''\n''for subtraction type 2 -''\n''for multiplication type3 *''\n''for division type4 / :')
        if ans=='1':
            sum_int=num1+num2
            print(sum_int)
        elif ans=='2':
            sub_int=num1-num2
            print(sub_int)
        elif ans=='3':
            mul_int=num1*num2
            print(mul_int)
        elif ans=='4':
            divide_int=num1/num2
            print(divide_int)
          
          
    func(x,y)


