import sendgrid
from sendgrid.helpers.mail import *

API_KEY = 'YOUR_API_KEY'  # Your API key which is generated for you when created the account
SUBJECT = 'Welcome Email'  # Subject of email.
HTML_CONTENT = '<p>Welcome to our mailing list!</p>'  # Content. We can also send attachments.

# Create a SendGrid client
sg = sendgrid.SendGridAPIClient(api_key=API_KEY)  # Create a client for accessing the API

# Create a mail helper object
from_email = Email('from_email')
to_email = Email('to_email')
content = Content('text/html', HTML_CONTENT)
mail = Mail(from_email, to_email, SUBJECT, content)  # Create a mail object

# Send the email
response = sg.send(mail)
print(response.status_code)  # If status code is 200, it is successful.
print(response.body)
print(response.headers)
