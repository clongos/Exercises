print "          +++ Welcome to BioData App, Please fill-up the form. +++"
print "=============================================================================="
name = raw_input("       Full Name: ")
address = raw_input("       Address: ")
age = raw_input("       Age: ")
mobile = raw_input("       Mobile number: ")
hobby = raw_input("       Hobby: ")
school = raw_input("       School Name: ")
year = raw_input("       Year: ")
course = raw_input("       Course: ")
print "=============================================================================="
message = "       Hi so you\'re %s and you\'re %s years old,\n       you live in %s.You love %s and still studying\n       in %s taking up %s for %s years up to now.\n       We can contact you in these numbers: %s.\n       Thank you for your cooperation!" % (name,age,address,hobby,school,course,year,mobile)
print message
