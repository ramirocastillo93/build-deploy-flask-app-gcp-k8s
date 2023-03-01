import re

class VerifyDate:        
    def verifyDate(date):
        pattern = "(?:19\d{2}|20[01][0-9]|2023)[-/.](?:0[1-9]|1[012])[-/.](?:0[1-9]|[12][0-9]|3[01])\b"
        try:
            re.match(pattern, date)
            return True
        except:
            return False