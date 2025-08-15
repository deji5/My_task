define_days = ('monday', 'tuesday', 'wenessday')
mon = input("enter activities")
tue = input("enter activities")
wed = input("enter activities")
activities =(mon, tue, wed)
schedule = {define_days:activities for define_days,
            activities in zip(define_days, activities)}
print(schedule)