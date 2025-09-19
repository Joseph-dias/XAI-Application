import os
from AIClient import AIClient
from WebScraping import WebsiteScraping
from dotenv import load_dotenv
import time
import sys

load_dotenv()

def print_animated(text):
    for t in text:
        sys.stdout.write(t)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def main():
    # Load API key from environment variable
    api_key = os.getenv("XAI_API_KEY")
    
    if not api_key:
        print("Error: XAI_API_KEY environment variable not set")
        print("Please set it using: export XAI_API_KEY='your-api-key'")
        print("Get your API key from https://x.ai/api")
        return

    # Initialize client
    client = AIClient(api_key, 1000)

    webscraper = WebsiteScraping("https://babylonbee.com/news/jimmy-kimmel-i-am-the-first-victim-of-the-murder-of-charle-kirk")
    title, body = webscraper.getText()

    response = client.summarizeWebPage(title, body)

    if response: 
        print_animated(response)
        print()
        chatting = False
    else:
        print_animated("Something went wrong.")
        print()
        chatting = False

    while chatting:
        # Get the prompt
        prompt = input("Speak to me: ")

        if "bye" in prompt.lower():
            chatting = False
            response, citations = client.generate_text("Give me a farewell sign off, including a finishing note about the last topic discussed.")
        else:
            # Make API call
            response, citations = client.generate_text(prompt)
    
        if response:
            print()
            sys.stdout.write("\rNugget: ")
            sys.stdout.flush()

            print_animated(response)

            print()
            print()
            if citations:
                for c in citations:
                    print(c)
                print()
        else:
            print("Failed to get response")

if __name__ == "__main__":
    main()