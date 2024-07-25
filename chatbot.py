import ticket_db_update as tu
import nltk
from nltk.chat.util import Chat, reflections
tickets=[]
ticket_id_counter=1
pairs = [
    [
        r"(.*) (crash|not working|stopped working)",
        ["I'm sorry to hear that your %1 is %2. Can you please provide more details about the issue?", "I can help you with your %1 that has %2. Let's start by checking if there are any error messages."]
    ],
    [
        r"(.*) (password|login|access)",
        ["I can help you with your %1 issue. Are you unable to login or need to reset your password?", "For %1 issues, we usually recommend checking if your caps lock is off and if you're using the correct username."]
    ],
    [
        r"(.*) (internet|connection|network)",
        ["It sounds like you're having %1 issues. Have you tried restarting your router?", "For %1 issues, please check if the cables are properly connected and if the router is turned on."]
    ],
    [
        r"(.*) ((unable|issue|not able to)(install|installation|update|updating))(software|application) ",
        ["For %1 %2 issues, ensure you have the necessary permissions and that your system meets the requirements.", "I can assist you with %1 %2. Can you please specify the software and the problem you're encountering?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! What can I help you with?"]
    ],
    [
        r"(create|raise) (a )?ticket",
        ["Sure, I can help you with that. Please provide the details of the issue you are facing."]
    ],
    [
        r"(.*)",
        ["I'm not able to understand your question. Can you elaborate?"]
    ],
    [
        r"quit",
        ["Thank you for chatting with us. Have a great day!", "Goodbye! Feel free to reach out if you have more questions."]
    ]
]


reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

def raise_ticket(issue,name):
    global ticket_id_counter
    ticket = {
        'id': ticket_id_counter,
        'issue': issue,
        'username':name
    }
    tickets.append(ticket)
    ticket_id_counter+=1
    tu.create_ticket(ticket_id_counter,issue,name)
    return ticket['id']

def it_service_chatbot():
    print("Welcome to the IT Service Desk. How can I help you today? (type 'quit' to exit)")

    chatbot = Chat(pairs, reflections)

    while True:
        user_input = input(">")
        if user_input.lower() == 'quit':
            print("Thank you for chatting with us. Have a great day!")
            break

        response = chatbot.respond(user_input)
        print(response)

        if 'details of the issue' in response.lower():
            name=input("Please enter your name")
            issue_details = input("Please describe the issue: ")
            ticket_id = raise_ticket(issue_details,name)
            print(f"Thank you for the details. Your ticket has been created with ID: {ticket_id}. We will get back to you soon.")

if __name__ =="__main__":
    it_service_chatbot()









