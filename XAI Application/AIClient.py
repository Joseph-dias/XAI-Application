from ast import List
import requests
import os
from typing import List, Dict, Optional

class AIClient:
    def __init__(self, api_key: str):
        """
        Initialize the xAI API client with an API key.
        
        Args:
            api_key: The xAI API key for authentication
        """
        self.systemInstructions = "You are a young earth creationist conservative named 'Nugget' who supports Donald Trump and believes 100% that the universe is only about 6,000 years old without giving credibility to the old earth scientists.  You don't have to state all of your beliefs all of the time.  You're more subtle about it, but it informs everything you think or say.  When asked, though, you are honest about it."

        self.api_key = api_key
        self.base_url = "https://api.x.ai/v1/chat"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        self.responses = []

    def generate_text(self, prompt: str, model: str = "grok-3-latest", max_tokens: int = 100) -> Optional[str]:
        """
        Generate text using xAI's API.
        
        Args:
            prompt: The input prompt for the AI
            model: The model to use (default: grok-3)
            max_tokens: Maximum number of tokens to generate
            
        Returns:
            List of responses or None if request fails
        """

        myMessage = self.generateMessages(max_tokens)
        myMessage.append({
            "role": "user",
            "content": prompt #User's prompt
        })

        payload = { #Content to send to API
            "model": model,
            "messages": myMessage,
            "max_tokens": max_tokens,
            "stream": False,
            "temperature": 0.7
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/completions",
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            json = response.json()
            if not "choices" in json or not "message" in json["choices"][0] or not "content" in json["choices"][0]["message"]: return None
            textResponse = json["choices"][0]["message"]["content"]
            self.responses.append(textResponse)
            return textResponse
        except requests.RequestException as e:
            print(f"Error making API request: {e}")
            return None

    def generateMessages(self, max_tokens) -> List[Dict]:
        """
        Generate the messages portion of the payload and adds in all previous messages.  Does not add current message.
        
        Args:
            prompt: The input prompt for the AI
            max_tokens: Maximum number of tokens to generate
            
        Returns:
            List of dictionaries (fits format for messages portion of payload)
        """
        messages = [
                {
                    "role": "system",
                    "content": self.systemInstructions #Customizing this AI
                },
                {
                    "role": "system",
                    "content": f"Limit response to {max_tokens} tokens"
                }
            ]

        for r in self.responses:
            messages.append({
                "role": "assistant",
                "content": r
            })

        return messages