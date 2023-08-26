import openai

openai.api_key = "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" 

def get_chatbot_response(messages, user_message):
    messages.append({"role": "user", "content": user_message})
    
    try:
        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat_completion["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        return reply, messages
    except Exception as e:
        return "An error occurred while processing your request.", messages

def initialize_chat():
    return [
        {"role": "system", "content": "Your Personal Chatbot Assistant is here! Ask me anything you want to know..."},
    ]

if __name__ == '__main__':
    print("Starting the Chatbot...")
    messages = initialize_chat()
    print(messages[0]['content'])