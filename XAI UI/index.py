import reflex as rx
import aiohttp
from typing import List, Optional

class XAIState(rx.State):
    greeting: str = ""
    response: str = ""
    citations: List[str] = []
    prompt: str = ""
    loading: bool = False
    error: str = ""

    async def fetch_greeting(self):
        self.loading = True
        self.error = ""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.api_url}/api/greeting") as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        self.greeting = data["response"]
                        self.citations = data["citations"] or []
                    else:
                        self.error = f"Failed to fetch greeting: {resp.status}"
        except Exception as e:
            self.error = f"Error: {str(e)}"
        self.loading = False

    async def send_prompt(self):
        if not self.prompt:
            return
        self.loading = True
        self.error = ""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.api_url}/api/chat",
                    json={"prompt": self.prompt}
                ) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        self.response = data["response"]
                        self.citations = data["citations"] or []
                        self.prompt = ""  # Clear input
                    else:
                        self.error = f"Failed to send prompt: {resp.status}"
        except Exception as e:
            self.error = f"Error: {str(e)}"
        self.loading = False

    async def fetch_farewell(self):
        self.loading = True
        self.error = ""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.api_url}/api/farewell") as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        self.response = data["response"]
                        self.citations = data["citations"] or []
                    else:
                        self.error = f"Failed to fetch farewell: {resp.status}"
        except Exception as e:
            self.error = f"Error: {str(e)}"
        self.loading = False

def index():
    return rx.vstack(
        rx.heading("XAI Chat", size="lg"),
        rx.cond(
            XAIState.greeting,
            rx.text(XAIState.greeting, color="blue", margin="10px"),
            rx.text("Loading greeting...", color="gray")
        ),
        rx.hstack(
            rx.input(
                placeholder="Enter your prompt",
                value=XAIState.prompt,
                on_change=XAIState.set_prompt,
                width="300px"
            ),
            rx.button(
                "Send",
                on_click=XAIState.send_prompt,
                is_loading=XAIState.loading,
                color="green"
            ),
            rx.button(
                "Farewell",
                on_click=XAIState.fetch_farewell,
                is_loading=XAIState.loading,
                color="red"
            ),
            spacing="10px"
        ),
        rx.cond(
            XAIState.response,
            rx.box(
                rx.text("Nugget: ", font_weight="bold"),
                rx.text(XAIState.response, margin="10px"),
                rx.cond(
                    XAIState.citations,
                    rx.vstack(
                        rx.text("Citations:", font_weight="bold"),
                        rx.foreach(
                            XAIState.citations,
                            lambda citation: rx.text(citation, color="gray")
                        ),
                        margin="10px"
                    )
                )
            )
        ),
        rx.cond(
            XAIState.error,
            rx.text(XAIState.error, color="red", margin="10px")
        ),
        rx.cond(
            XAIState.loading,
            rx.text("Loading...", color="gray")
        ),
        spacing="20px",
        padding="20px",
        align_items="center"
    )

app = rx.App()
app.add_page(index, on_load=XAIState.fetch_greeting)
