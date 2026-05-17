

rows = int(input("Enter rows : "))

for i in range (rows):

    for j in range(4):

        if i % 4 == 0:

            print("#",end="\t")

        elif i % 4 == 1:

            print("$",end="\t")
        
        elif i % 4 == 2:

            print("@",end="\t")

        else:

            print("*",end="\t")

    print()

'''
Enter rows : 4
#       #       #       #
$       $       $       $
@       @       @       @
*       *       *       *
'''
