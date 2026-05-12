

day = input("Enter day : ")

match day :

    case "Mon":
        print("Start of the week")
    
    case "Fri":
        print("Weekend is coming")
    
    case "Sat" :
        print("Weekend Started")
    
    case "Sun" :
        print("Weekend Started")
    
    case _ :
        print("Weekday")
