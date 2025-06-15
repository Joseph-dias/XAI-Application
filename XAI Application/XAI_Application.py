import os
from AIClient import AIClient
from dotenv import load_dotenv
import time
import sys

load_dotenv()

def main():
    # Load API key from environment variable
    api_key = os.getenv("XAI_API_KEY")
    
    if not api_key:
        print("Error: XAI_API_KEY environment variable not set")
        print("Please set it using: export XAI_API_KEY='your-api-key'")
        print("Get your API key from https://x.ai/api")
        return

    # Initialize client
    client = AIClient(api_key)
    
    chatting = True

    while chatting:
        # Get the prompt
        prompt = input("Speak to me: ")

        if "bye" in prompt.lower():
            chatting = False
            result = "Talk to you later!"

        else:
            # Make API call
            result = client.generate_text(prompt)
    
        if result:
            print()
            sys.stdout.write("\rNugget: ")
            sys.stdout.flush()

            for c in result:
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.05)

            print()
            print()
        else:
            print("Failed to get response")

if __name__ == "__main__":
    main()