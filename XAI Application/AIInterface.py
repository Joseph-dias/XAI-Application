import os
from typing import Self
import gradio as gr
import AIClient as ai

class AIInterface:
    def __init__(self):
        # Load API key from environment variable
        self.api_key = os.getenv("XAI_API_KEY")
    
        if not self.api_key:
            print("Error: XAI_API_KEY environment variable not set")
            print("Please set it using: export XAI_API_KEY='your-api-key'")
            print("Get your API key from https://x.ai/api")
            return

        # Initialize client
        self.client = ai.AIClient(self.api_key)

    def chat_with_ai(self, message, history):

        response, citations = self.client.generate_text(message)

        if response: 
            yield response
        else:
            yield "Something went wrong."

    def getInterface(self):
        return gr.ChatInterface(
            chatbot=gr.Chatbot(type="messages", value=[{"role": "assistant", "content": self.client.get_greeting()}]),
            type="messages",
            fn=self.chat_with_ai,
            title="Chat with Nugget",
            description="Get on board for a wild ride!"
        )