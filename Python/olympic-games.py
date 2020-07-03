
def olympicYear(year):
    while year < 2021:
        if not((year==1916)or(year==1940)or(year==1944)):
            print(year)
        year+=4

startYear=1896
olympicYear(startYear)