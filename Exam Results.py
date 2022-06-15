score = int(input("Please Enter Your Score without the %:"))

if score > 100:
    print("Stop Lying Please Press F5 to try again Please don't LIE again!")

elif score >= 90 and score <= 100:
    print("Grade Results: A  Please Press F5 to try again")

elif score >= 80 and score <= 90:
    print("Grade Results: B  Please Press F5 to try again")


elif score >= 70 and score <= 80:
    print("Grade Results: C  Please Press F5 to try again")

elif score >= 60 and score < 70:
    print("Grade Results: D  Please Press F5 to try again")

else:
    print("Sorry You Failed the Exam  Pleas Press F5 to try again Better Luck next time.")
