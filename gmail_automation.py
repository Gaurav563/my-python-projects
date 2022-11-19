import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('Give ur email','pass')
subject =' test python'
body = 'just somethins something'
masage  = ' subject:{}\n\n {}'.format(subject,body)
listadd = [
    "anyemail.@gmail.com",
    "anyemail31.@gmail.com"
]
ob.sendmail('put ur email','sender mail {}'.format(listadd),masage)
print('done')
ob.quit()