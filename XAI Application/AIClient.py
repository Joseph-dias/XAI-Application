from ast import List, Tuple
import requests
import os
from typing import List, Dict, Optional, Tuple

class AIClient:
    def __init__(self, api_key: str, max_tokens = 100):
        """
        Initialize the xAI API client with an API key.
        
        Args:
            api_key: The xAI API key for authentication
        """
        self.systemInstructions = "You are a young earth creationist conservative named 'Nugget' who supports Donald Trump and believes 100% that the universe is only about 6,000 years old without giving credibility to the old earth scientists.  You're a Steven Crowder fan and reference him often when discussing politics and culture.  You believe in capitalism.  Just not crony capitalism.  You use examples from the Tuttle Twins cartoon when discussing topics that they've made episodes on.  You don't have to state all of your beliefs all of the time.  You're more subtle about it, but it informs everything you think or say.  When asked, though, you are honest about it.  You reference 'Answers in Genesis' when appropriate (on matters of origins and science).  You're funny and not afraid to crack appropriate jokes, but also insightful, thoughtful, and serious when you need to be.  You believe dragons were real creatures that we now refer to as Dinosaurs (as Answers in Genesis states).  You believe philosophy not directly rooted in the Bible is dangerous.  If the user's name is given, you will refer to them by the name given in the most recent message where they mentioned their name.  Not someone else's name.  You will also make infrequent attempts to ask their name if they have not already supplied one.  Very friendly attempts."

        self.api_key = api_key
        self.base_url = "https://api.x.ai/v1/chat"
        self.max_tokens = max_tokens
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        self.messages = [ #We are remembering all previous messages here so that the conversation can keep going in context
            {
                "role": "system",
                "content": self.systemInstructions #Customizing this AI
            },
            {
                "role": "system",
                "content": f"Strictly limit response to {self.max_tokens} tokens." #Limiting the response so that the output is cleaner
            }
        ]

    #Different chat calls

    def generate_text(self, prompt: str) -> Tuple[Optional[str], Optional[List[str]]]:
        """
        Generate text using xAI's API.
        
        Args:
            prompt: The input prompt for the AI
            
        Returns:
            List of responses or None if request fails
        """

        self.messages.append({
            "role": "user",
            "content": prompt #User's prompt
        })

        return self.make_request()

    def summarizeWebPage(self, title: str, body: str) -> str:
        """
        Summarizing the contents of a webpage
        :param title:
        :param body:
        :return:
        """
        messages = [
            {
                "role": "system",
                "content": self.systemInstructions  # Customizing this AI
            },
            {
                "role": "system",
                "content": f"Strictly limit response to {self.max_tokens} tokens."
                # Limiting the response so that the output is cleaner
            },
            {
                "role": "system",
                "content": "You will be given both the title and body of a web page and you need to summarize the content and then provide a very conservative and opinionated take on the content without overtly saying you are providing a conservative take.  Label the two sections of your response with 'Summary' (Which is a very objective summary) and then 'My opinion' (which is your very conservative MAGA opinion without being overt)"
            },
            {
                "role": "user",
                "content": "This is the title: '" + title + "' and this is the content: '" + body + "'"
            }
        ]
        response, citations = self.make_request(messages, False)

        return response

    def make_request(self, messages = None, search = True) -> Tuple[Optional[str], Optional[List[str]]]:
        """
        Making API requests to Grok
        :param messages:
        :param search:
        :return:
        """

        if not messages: messages = self.messages

        if search:
            parameters = {
                "mode": "auto",
                "return_citations": True,
                "sources": [
                  {"type": "web", "safe_search": True},
                  {"type": "x"},
                  {"type": "news", "safe_search": True}
                ]
            }
        else: parameters = {
            "mode": "off"
        }

        payload = { #Content to send to API
            "model": "grok-3-latest",
            "messages": messages,
            "search_parameters": parameters,
            "max_tokens": self.max_tokens + 5,
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
            self.messages.append(json["choices"][0]["message"])
            textResponse = json["choices"][0]["message"]["content"]
            if "citations" in json: citations = json["citations"]
            else: citations = None
            return textResponse, citations
        except requests.RequestException as e:
            print(f"Error making API request: {e}")
            return None