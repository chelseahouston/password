import re

def user_password():
  username = input("Create a username: ")
  password = input("Create a password: ")
  confirmpassword = input("Confirm password: ")

# CONFRIM PASSWORD
  if confirmpassword != password:
    print("Passwords do not match. Please try again.")
    user_password()

# CHECK FOR AT LEAST ONE NUMBER
  if re.search('[0-9]', password):
    num = "strong"
  else:
    num = "weak"

# CHECK FOR AT LEAST ONE LOWERCASE CHAR
  if re.search('[a-z]', password):
      lc = "strong"
  else:
    lc = "weak"

# CHECK FOR AT LEAST ONE UPPERCASE CHAR
  if re.search('[A-Z]', password):
      uc = "strong"
  else:
    uc = "weak"

  # CHECK PASSWORD LENGTH
  if len(password) <= 5:
    pwl = "weak"
  elif len(password) >5 and len(password) <=7:
    pwl = "medium"
  else:
    pwl = "strong"
  
  # PRINT IF PASSWORD IS STRONG
  if pwl == "strong" and uc == "strong" and lc == "strong" and num == "strong":
        print("Strong Password")

  # PRINT IF PASSWORD IS WEAK
  elif uc == "weak" and num == "weak" and pwl == "weak":
    print("Weak Password")
  elif lc == "weak" and num == "weak" and pwl == "weak":
    print("Weak Password")
  elif num == "weak" and pwl == "weak":
    print("Weak Password")
  elif uc == "weak" and pwl == "weak":
    print("Weak Password")
  elif lc == "weak" and pwl == "weak":
    print("Weak Password")

  # PRINT IF PASSWORD IS MEDIUM
  else:
    print("Medium Password")
user_password()
  
  
