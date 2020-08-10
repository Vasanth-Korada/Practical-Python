import smtplib

email_recp = ["vasanthkorada999@gmail.com","srikanth512000@gmail.com","palisettyaravind69@gmail.com"]
sender_email = "infytech2019@gmail.com"

for i in range(len(email_recp)):
    try:
        s = smtplib.SMTP(host='smtp.gmail.com',port=587)

        s.starttls()

        s.login(user=sender_email,password="8106237018")

        message = "Greetings from INFY TECH"

        s.sendmail(from_addr=sender_email,to_addrs=email_recp[i],msg=message)

        print(f"Email sent to {email_recp[i]}")

        s.quit()
    except:
        print("Error")








