

import re

class MessagingService:
    def send_message(self):
        pass

class SMSMessagingService(MessagingService):
    def send_message(self):
        print("Enter the valid Mobile Number")
        mob_num = input()

        if re.match(r'^[6789]\d{9}$', mob_num):
            self.send_sms(mob_num)
        else:
            print("Invalid Mobile Number !!!")

    def send_sms(self, mob_num):
        print("Enter the SMS Message to send")
        text = input()
        print("Message: ({}) is sent to {}\n".format(text, mob_num))


class EmailMessagingService(MessagingService):
    def send_message(self):
        print("Enter the valid Email Address")
        email = input()

        if re.match(r'^[A-Za-z0-9+_.-]+@[A-Za-z-]+\.[A-Za-z]+$', email):
            self.send_email(email)
        else:
            print("Invalid Email Address !!!")

    def send_email(self, email):
        print("Enter the Email Message to send")
        text = input()
        print("Message ({}) is sent to {}\n".format(text, email))


class WhatsAppMessagingService(MessagingService):
    def send_message(self):
        print("Enter the valid Mobile Number")
        mob_num = input()

        if re.match(r'^[6789]\d{9}$', mob_num):
            print("WhatsApp available? Type true or false")
            is_whatsapp = input()
            self.send_whatsapp(mob_num, is_whatsapp)
        else:
            print("Invalid Mobile Number !!!")

    def send_whatsapp(self, mob_num, is_whatsapp):
        if is_whatsapp == 'true':
            print("Enter the WhatsApp Message to send")
            text = input()
            print("Message: ({}) is sent to {}\n".format(text, mob_num))
        else:
            print("WhatsApp unavailable !!!")

class Message:
    def main(self):
        print("Select\n1.SMS\n2.WhatsApp\n3.Email")
        option = int(input())
        
        if option == 1:
            sms_service = SMSMessagingService()
            sms_service.send_message()
        elif option == 2:
            whatsapp_service = WhatsAppMessagingService()
            whatsapp_service.send_message()
        elif option == 3:
            email_service = EmailMessagingService()
            email_service.send_message()


message = Message()
message.main()
