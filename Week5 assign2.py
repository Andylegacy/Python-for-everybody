"""Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F """

1

score = float(input("Enter Score: "))

2

if score >= 0.9:

3

     print(" A")

4

elif score >= 0.8:

5

     print("B")

6

elif score >= 0.7:

7

     print("C")

8

elif score >= 0.6:

9

     print("D")

10

elif score < 0.6:   

11

     print("F")
