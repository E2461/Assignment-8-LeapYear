
def is_leap_year(years):
    
    for year in years:
        if (year % 4) == 0:
           if (year % 100) == 0:
               if (year % 400) == 0:
                   print("{0} is a leap year".format(year))
               else:
                   print("{0} is not a leap year".format(year))
           else:
               print("{0} is a leap year".format(year))
        else:
           print("{0} is not a leap year".format(year))


years = [1800, 1900, 2000, 2019, 2020, 2100, 2200, 2300, 2400, 2500]
is_leap_year(years)
