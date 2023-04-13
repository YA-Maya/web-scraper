import openai
import requests

# Set up the API key
api_key = "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"
api_url = "https://api.openai.com/v1/engines/davinci-codex/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Function to generate response using GPT API
def generate_response(prompt, tokens=150, temperature=0.5):
    data = {
        "prompt": prompt,
        "max_tokens": tokens,
        "temperature": temperature,
        "n": 1,
        "stop": None
    }

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 200:
        message = response.json()["choices"][0]["text"].strip()
        return message
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return "Sorry, I'm unable to generate a response at the moment."

# Function to process user input
def process_user_input(user_input):
    prompt = f"User: {user_input}\nChatbot:"
    chatbot_response = generate_response(prompt)
    return chatbot_response

# Function to run a simple test loop
def main():
    print("Welcome to the GPT Chatbot!")
    print("Type 'quit' to exit the chat.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'quit':
            break

        chatbot_response = process_user_input(user_input)
        print(f"Chatbot: {chatbot_response}")

if __name__ == "__main__":
    main()
