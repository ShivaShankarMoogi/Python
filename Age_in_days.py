from datetime import date

Year = int(input("Enter a Year :"))
Month = int(input("Enter a Month :"))
Day = int(input("Enter a day :"))

Current_date = date.today()

follow_on_date = date(2023,1,1)

Age_in_days = (follow_on_date - date(Year,Month,Day)).days

print("On January 1st 2023 you turned :",Age_in_days,"old")

