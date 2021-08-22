a_score = 90
b_score = 80
c_score = 70
d_score = 60

score = int(input("Enter your test score"))

if score >= a_score:
    print("Your grade is A")
else:
    if score>= b_score:
        print("Your grade is B")
    else:
        if score>= c_score:
            print("Your grade is C")
        else:
            if score>= d_score:
                print("Your score is D")
            else:
                print("Your grade is E")
                