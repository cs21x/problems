import check50

@check50.check()
def exists():
    """check0"""
    check50.exists("slowpayoff.py") # the actual check

@check50.check(exists)
def check0():
    """check1"""
    check50.run("python3 slowpayoff.py").stdin("100\n0.1\n").stdout("RESULT\nMonthly payment to pay off debt in 1 year: 10\nNumber of months needed: 11\nBalance: -5.16\n", regex=False).exit(0)