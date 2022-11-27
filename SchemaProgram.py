def calcpay(start,end,pay):
    ob=18
    ob_hours=end-ob
    hours=end-start
    if ob_hours > 0:
        hours=hours-ob_hours
        hours=hours+ob_hours*1.25
    payperday=pay*hours
    tax=0.67
    payaftertax=payperday*tax
    print(f"{payperday} kr innan skatt.")
    print(f"{payaftertax} kr efter skatt.")


calcpay(6,12,275)