import re

def dateVerification(date=str):
    pattern = "^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$"
    try:
        re.match(pattern, date)
        return True
    except:
        return False


dateVerification(1)