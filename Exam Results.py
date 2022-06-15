score = int(input("Please Enter Your Score without the %:"))

if score >= 100:
    print("Stop Lying !!!")

elif score >= 90 and score <= 100:
    print("Grade Results: A")

elif score >= 80 and score <= 90:
    print("Grade Results: B ")


elif score >= 70 and score <= 80:
    print("Grade Results: C ")

elif score >= 60 and score < 70:
    print("Grade Results: D ")

else:
    print("Sorry You Failed the Exam")
