class EmailService:
    def send_mail(self, message):
        print(f"Sending Email -------> {message}")

class SMSService:
    def send_sms(self, message="SMS Notification"):
        print(f"Sending SMS -------> {message}")

class NotificationManager:
    def __init__(self):
        self.service = EmailService()
        self.sms_service = SMSService()

    def send_notification(self, message):
        self.service.send_mail(message)
    
    def send_sms(self, message):
        self.sms_service.send_sms(message)
    
notification_manger = NotificationManager()
notification_manger.send_notification("Hello, I am from email service")
notification_manger.send_sms("Hello, I am from email service")