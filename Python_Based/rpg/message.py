class Message:
    message = "sigma phony zebras"
    
    def Call_Sign(self):
        print(self.message)

    def Change_Message(self):
        self.message = input("Enter new message:\n")