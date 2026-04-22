class Message:
    message = "Sup brother"

    def Call_Sign(self):
        print(self.message)

    def Change_Message(self):
        self.message = input("Enter new message:\n")