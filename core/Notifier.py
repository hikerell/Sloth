import logging
import smtplib
import email.mime.text

logger = logging.getLogger(__name__)
#GMAIL SMTP should enable less-secure-app-login feature
#https://support.google.com/accounts/answer/6010255
#https://stackabuse.com/how-to-send-emails-with-gmail-using-python/

class GmailNotifier(object):
	"""docstring for GmailNotifier"""
	def __init__(self, gmailuser, gmailpasswd):
		super(GmailNotifier, self).__init__()
		self.gmailuser = gmailuser
		self.gmailpasswd = gmailpasswd
		self.HOST = 'smtp.gmail.com'
		self.PORT = 25

	def send(self, receiver, subject, message):
		# Create SMTP Object
		smtp = smtplib.SMTP()
		# show the debug log
		#smtp.set_debuglevel(1)

		# connet
		try:
			logger.debug('GmailNotifier.send connecting ...')
			smtp.connect(self.HOST, self.PORT)
			# gmail uses ssl
			logger.debug('GmailNotifier.send tls starting...')
			smtp.starttls()

			logger.debug('GmailNotifier.send login...')
			smtp.login(self.gmailuser, self.gmailpasswd)

			# fill content with MIMEText's object 
			msg = email.mime.text.MIMEText(message)
			msg['From'] = self.gmailuser
			msg['To'] = ';'.join([receiver])
			msg['Subject']= subject
			logger.debug(msg.as_string())
			smtp.sendmail(self.gmailuser, [receiver], msg.as_string())
			smtp.quit()
		except Exception as e:
			logger.error(e)

if __name__=='__main__':
	notifier = GmailNotifier('acmfly@gmail.com', 'Gooqygst_2018')
	notifier.send('hikerell@gmail.com', 'efuzzer: test', 'this email is just for test!')