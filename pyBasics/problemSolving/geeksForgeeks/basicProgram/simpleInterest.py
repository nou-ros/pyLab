def simpleInterest(prinAmount, rate, time):
    print("The principal amount is: ", prinAmount);
    print("The time period is: ", time);
    print("The rate of interrest is: ", rate);

    simInterest = (prinAmount * rate * time)/100;
    print("Simple interest: ", simInterest);

simpleInterest(8, 6, 8)
