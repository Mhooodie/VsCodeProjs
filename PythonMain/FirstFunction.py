print('running script')
#FUNCTION

def create_email(email_address, name): # (Parameters) 
    email_text = f"Hey {name}, I noticed you like to code, message me at {email_address}" # Scoped to def of function / Only accessible in function
    # print ("text", email_text)
    # print ("address", email_address)
    return email_text

email = create_email('team@skillquest.io', 'Billy') # Arguments
# create_email('billybob@gmail.com', 'Bob')
print(email)


