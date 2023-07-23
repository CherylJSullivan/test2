import os

# Set your environment variables
os.environ["EMAIL_SECRET"] = "secret_email_value"
os.environ["PASSWORD_SECRET"] = "secret_password_value"

# Optional: Print the environment variables to confirm their values
print(os.environ["EMAIL_SECRET"])
print(os.environ["PASSWORD_SECRET"])
