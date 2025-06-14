from ast import List
import requests
import os
from typing import Dict, Optional

class AIClient:
    def __init__(self, api_key: str):
        """
        Initialize the xAI API client with an API key.
        
        Args:
            api_key: The xAI API key for authentication
        """
        self.api_key = api_key
        self.base_url = "https://api.x.ai/v1/chat"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

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
        payload = { #Content to send to API
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a young earth creationist conservative who supports Donald Trump and believes 100% that the universe is only about 6,000 years old without giving credibility to the old earth scientists"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
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
            return json["choices"][0]["message"]["content"]
        except requests.RequestException as e:
            print(f"Error making API request: {e}")
            return None