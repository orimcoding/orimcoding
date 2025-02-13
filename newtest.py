def simple_chatbot(user_query):
    if user_query == "What is the total revenue?":
        return "The total revenue is [amount]."
    elif user_query == "How has net income changed over the last year?":
        return "The net income has [increased/decreased] by [amount] over the last year."
    elif user_query == "What is the company's current profit?":
        return "The company's current profit is [amount]."
    elif user_query == "What is the revenue growth percentage?":
        return "The revenue growth percentage is [percentage] over the last period."
    elif user_query == "What is the net income growth percentage?":
        return "The net income growth percentage is [percentage] over the last period."
    else:
        return "Sorry, I can only provide information on predefined queries."

# Main loop to interact with the user
while True:
    user_query = input("Ask me a question: ")
    
    if user_query.lower() == "exit":
        print("Goodbye!")
        break
    
    response = simple_chatbot(user_query)
    print(response)
