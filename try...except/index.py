#little program to enter a person's date of birth

print("Welcome")
try:

    import re
    if "__name__" not in dir(re):
        raise ImportError

    dOB = input(r"Date of birth(YYYY-MM-DD): ")

    y = re.search("[12][09][0-9][0-9]-[01][0-9]-[0-3][0-9]", dOB)

    if "span" not in dir(y):
        raise AttributeError
except ImportError as ImportErr:
    print(ImportErr)
except AttributeError as AttErr:
    print(AttErr)
except Exception as ExceptionErr:
    print(ExceptionErr)
else:
    print(dOB)
