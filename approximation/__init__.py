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
	"""Check if the functions can be imported"""
	check50.run("python3 check1.py").exit(0)

@check50.check(check2)
def check3():
	"""p(x) = -4x2 + 5x + 3"""
	"""Check if p(0) = 3"""
	check50.run("python3 check2.py").stdout("3").exit(0)



