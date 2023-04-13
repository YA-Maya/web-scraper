import requests
import pyttsx3
import openai

# Set up the API key
api_key = "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"
api_url = "https://api.openai.com/v1/engines/text-davinci-002/completions"
openai.api_key = api_key

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Initialize the text-to-speech engine
tts_engine = pyttsx3.init()
speech_rate = 155
tts_engine.setProperty("rate", speech_rate)

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
        # The prompt response
        message = response.json()["choices"][0]["text"].strip()
        return message
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return "Sorry, I'm unable to generate a response at the moment."

# # Function to process user input
# def process_user_input(user_input):
#     # prompt = f"User: {user_input}\nChatbot:"
#     chatbot_response = generate_response(prompt)
#     return chatbot_response

# Function to speak the chatbot response
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()
    
def setup_game():
    # set the rules & setting for the game
    initial_game_prompt = "I want you to act as a text based adventure game. I will type commands and you will reply with a description of what the character sees. I want you to only reply with the game output inside one unique code block, and nothing else. do not write explanations. do not type commands unless I instruct you to do so. when i need to tell you something in english, i will do so by putting text inside curly brackets {like this}. my first command is wake up"
    chatbot_response = generate_response(initial_game_prompt)
    print(chatbot_response)
    # speak(response)
    
    
    # TODO make the image school sketch style
def generate_image(prompt):
    response = openai.Image.create(
    prompt= f"{prompt}",
    n=1,
    size="512x512")
    image_url = response['data'][0]['url']
    print(image_url)
    

# Function to run a simple test loop
def main():
    # print("Welcome to the GPT Chatbot!")
    # print("Type 'quit' to exit the chat.\n")
    print("youre in a game (intro)")
    
    setup_game()

    while True:
        
        user_input = input("prompt: ") #TODO pick word

        if user_input.lower() == 'quit':
            break

        chatbot_response = generate_response(user_input)
        print(f"narrator: {chatbot_response}")
        # speak(chatbot_response)
        
        # generate_image(chatbot_response)



if __name__ == "__main__":
    main()