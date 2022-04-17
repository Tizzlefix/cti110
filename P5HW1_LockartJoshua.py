# CTI-110
# P5HW1 - Score List
# Joshua Lockart 
# 4/16/2022


def scores_list():

    #grabbing user input for scores
    count = int(input("How many scores do you want to enter? "))

    print("How many scores do you want to enter?", count)
    print("\n")
    
    #Assigning variable i to a list
    i, mylist = 1, []
    
    #Setting up while loop
    while True:
        if(len(mylist) == count): 
            break
        score = int(input("Enter score #"+ str(i) + ':'))
        print("Enter score #"+ str(i) + ':', score)
        if score < 0 or score > 100:
            print("\nINVALID Score entered!!!!") 
            print("Score should be between 0 and 100")
        else:
            mylist.append(float(score))
            i+=1
    
    #Sorting list, separating lowest score and getting score average
    mylist.sort()
    lowest_score = mylist[0]
    score_avg = sum(mylist) / len(mylist)

    #Putting user's list entries through statements
    if score_avg > 90: 
        grade = "A" 
    elif score_avg >= 80 and score_avg < 90: 
        grade = "B" 
    elif score_avg >= 70 and score_avg < 80:
        grade = "C"
    elif score_avg >= 60 and score_avg < 70:
        grade = "D"
    else:
        grade = "F"

    #printing Results 
    print("\n\n--------------Results-----------")
    print("Lowest Score      :",lowest_score)
    print("Modified List     :",mylist)
    print("Scores Average    :",score_avg)
    print("Grade             :",grade)
    print("-----------------------------------")
scores_list()