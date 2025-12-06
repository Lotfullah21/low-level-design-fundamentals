from abc import ABC, abstractmethod
# Step 1. Create a contract (interface)
class SendMessage:
    @abstractmethod
    def send(self, message):
        pass

# Step 2: Create the low level module (workers)
class SMSService(SendMessage):
    def send(self, message):
        print(f"Sending SMS -------> {message}")

class EmailService(SendMessage):
    def send(self, message):
        print(f"Sending Email -------> {message}")

# Step 3: Create the high level module (Manager)
class NotificationManager:
    def __init__(self, message_sender:SendMessage) -> None:
        self.message_sender = message_sender
        
    def send_notification(self, message):
        self.message_sender.send(message)

email_service = EmailService()
notification_manager = NotificationManager(email_service)
notification_manager.send_notification("Hello email")


# 2. Tomorrow we switch to SMS (We didn't touch the Notification Manager class!)
sms_service = SMSService()
notification_manager = NotificationManager(sms_service)
notification_manager.send_notification("Hello SMS")

