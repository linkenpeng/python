
def dayUp(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup


dayFactor = 0.01
while dayUp(dayFactor) < 37.78:
    dayFactor += 0.001

print("工作日的努力{:.3f}".format(dayFactor))