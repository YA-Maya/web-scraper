const axios = require("axios");

// Set up the API key
const apiKey = "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";
const apiUrl = "https://api.openai.com/v1/engines/text-davinci-002/completions";

const headers = {
  "Content-Type": "application/json",
  "Authorization": `Bearer ${apiKey}`,
};

// Function to generate response using GPT API
async function generateResponse(prompt, tokens = 150, temperature = 0.5) {
  const data = {
    prompt: prompt,
    max_tokens: tokens,
    temperature: temperature,
    n: 1,
    stop: null,
  };

  try {
    const response = await axios.post(apiUrl, data, { headers: headers });

    if (response.status === 200) {
      // The prompt response
      const message = response.data.choices[0].text.trim();
      return message;
    } else {
      console.error(`Error: ${response.status} - ${response.statusText}`);
      return "Sorry, I'm unable to generate a response at the moment.";
    }
  } catch (error) {
    console.error(`Error: ${error.response.status} - ${error.response.statusText}`);
    return "Sorry, I'm unable to generate a response at the moment.";
  }
}

// Function to run a simple test loop
async function main() {
  console.log("You're in a game (intro)");

  // Setup game
  const initialGamePrompt =
    "I want you to act as a text based adventure game. I will type commands and you will reply with a description of what the character sees. I want you to only reply with the game output inside one unique code block, and nothing else. do not write explanations. do not type commands unless I instruct you to do so. when i need to tell you something in english, i will do so by putting text inside curly brackets {like this}. my first command is wake up";
  const chatbotResponse = await generateResponse(initialGamePrompt);
  console.log(chatbotResponse);

  // Interactive loop
  const readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  readline.question("prompt: ", async function handleInput(userInput) {
    if (userInput.toLowerCase() === "quit") {
      readline.close();
      return;
    }

    const chatbotResponse = await generateResponse(userInput);
    console.log(`narrator: ${chatbotResponse}`);

    readline.question("prompt: ", handleInput);
  });
}

main();
