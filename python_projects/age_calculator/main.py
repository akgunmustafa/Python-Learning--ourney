def ageCalculator(y, m, d):
    import datetime
    today=datetime.datetime.now().date()
    dob=datetime.date(y, m, d)
    age= int((today-dob).days / 365.25)
    print("Your Age is "+str(age))
print("Welcome to Age-Calculator")
year=input("Please write your 'birth year' (like:1995)  :")
month=input("Please write your 'birth month' (like:07)  :")
day=input("Please write your 'birth day' (like:28)  :")
ageCalculator(int(year),int(month),int(day))