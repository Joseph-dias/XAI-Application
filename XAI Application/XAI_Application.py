from AIInterface import AIInterface
from dotenv import load_dotenv

load_dotenv()

def main():
    interface = AIInterface()
    interface.getInterface().launch()

if __name__ == "__main__":
    main()