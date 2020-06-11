import check50

@check50.check()
def check0():
    """Check if approximation.py exists"""
    check50.exists("approximation.py")
    check50.include("check1.py")
    check50.include("check2.py")

@check50.check(check0)
def check1():
	"""Check if approximation.py runs"""
	check50.run("python3 approximation.py").exit(0)

@check50.check(check1)
def check2():
	"""Check if all functions can be imported"""
	check50.run("python3 check2.py").exit(0)

@check50.check(check2)
def check3():
	"""For p(x) = -4x^2 + 5x + 3, check if p(0) = 3"""
	check50.run("python3 check3.py").stdout("3").exit(0)

@check50.check(check2)
def check4():
	"""For p(x) = -4x^2 + 5x + 3, check if p(-1) = 3"""
	check50.run("python3 check4.py").stdout("-6").exit(0)

@check50.check(check2)
def check5():
	"""For p(x) = -4x^2 + 5x + 3, check if p(2) = 3"""
	check50.run("python3 check5.py").stdout("4").exit(0)

@check50.check(check2)
def check6():
	"""For f(x) = x^4 + 3x^3 + 17.5x^2 - 13.39, check if f'(x) = 4x^3 + 9x^2 + 35x"""
	check50.run("python3 check6.py").stdout("(0.0, 35.0, 9.0, 4.0)").exit(0)

@check50.check(check2)
def check7():
	"""For f(x) = 4x^3 + 9x^2 +35x, check if f'(x) = 12x^2 + 18x + 35"""
	check50.run("python3 check7.py").stdout("(35.0, 18.0, 12.0)").exit(0)

@check50.check(check2)
def check8():
	"""For f(x) = 12x^2 + 18x + 35, check if f'(x) = 24x + 18"""
	check50.run("python3 check8.py").stdout("(18.0, 24.0))").exit(0)

@check50.check(check2)
def check9():
	"""check if a root of 2x^2 - 5x + 3 is 1"""
	check50.run("python3 check9.py").stdout("1.0").exit(0)

@check50.check(check2)
def check10():
	"""check if a root of 2x^2 - 5x + 3 is 1.5"""
	check50.run("python3 check10.py").stdout("1.5").exit(0)

