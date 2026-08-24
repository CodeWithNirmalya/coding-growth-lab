# QUESTION:Given a list of emails, filter only valid Gmail addresses.
emails = [
    "soumya.chatterjee@gmail.com",      # Valid Gmail
    "ananya.banerjee@gmail.com",        # Valid Gmail
    "ritwik.mukherjee@yahoo.com",       # Not Gmail
    "moumita.das@gmail.com",            # Valid Gmail
    "subhajit.roy@hotmail.com",         # Not Gmail
    "priyanka.sen@gmail",               # Invalid Gmail
    "arindam.ganguly@gmail.com",        # Valid Gmail
    "sreya.bose@outlook.com",           # Not Gmail
    "debashis.pal@gmail.com",           # Valid Gmail
    "koel.bhattacharya.gmail.com"       # Invalid (missing @)
]

email_filter = [email_id for email_id in emails if '@gmail.com' in email_id]
print(f'The genuine email id are {email_filter}')