import smtplib as s
ob = s.SMTP("smtp.gmail.com",587) # creating an object ob of the smtplib module as s of class SMTP
# when we create object ob for class SMTP within module smtplib as s we pass smtp server and port number as constructoror__init__ method parameters for SMTP class
ob.starttls()
ob.login("funsuktestwangdu@gmail.com","passwordgoeshere")
subject = "Sending mail using python"
body = "This is only educational purposes"
message = "Subject:{}\n\n{}".format(subject,body)
listofAddresses=["anmolbava96@gmail.com"]
ob.sendmail("techsoftindia2019",listofAddresses,message)
print("message sent successfully...")
ob.quit()

# This program is a good example of how we can import a package smtplib then use a class with in package(SMTP class) and create a object of the class SMTP ob. Once ob is created SMTP's class constructor is called and passed two parameters smtp server and port number
# Also ob object is used to call functions like starttls(),login(username,password)