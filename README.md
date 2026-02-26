# XAI Application

A conversational AI application powered by xAI's Grok API with both command-line and web-based interfaces. This project features "Nugget," a personalized AI assistant with distinct values and perspectives, accessible through a Python CLI or modern web UI.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Nugget Personality](#nugget-personality)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running The Application](#running-the-application)

## Overview

The XAI Application is a Python-based conversational AI platform that integrates with xAI's Grok model to create an interactive chatbot experience. It provides two distinct interfaces for users to interact with "Nugget," a customizable AI personality:

1. **Command-Line Interface (CLI)** - A terminal-based application for direct, real-time conversation
2. **Web User Interface (UI)** - A modern, responsive web application built with the Reflex framework

The application maintains conversation context across multiple exchanges, integrates with web search capabilities, and provides citations for information sourced from the web, social media, and news outlets.

## Features

### Core Capabilities

- **Conversational Memory** - Maintains full conversation history for contextual responses
- **Web Search Integration** - Access real-time information from:
  - Web pages (with safe search enabled)
  - X/Twitter posts
  - News articles (with safe search enabled)
- **Citation Management** - Automatically retrieves and displays sources for responses
- **Customizable AI Personality** - Define custom system prompts and behavioral guidelines
- **Token Control** - Configurable response length for optimized output
- **API Key Management** - Secure environment variable-based configuration
- **Error Handling** - Robust error management with user-friendly messages
- **Animated Text Output** (CLI) - Smooth character-by-character text animation
- **Async Operations** (Web UI) - Non-blocking API calls for responsive UI

### Advanced Features

- Multiple AI models support (default: grok-3-latest)
- Conversation farewell handling
- Real-time loading indicators
- Responsive web design
- State management for concurrent operations

# This File


### Directory Descriptions

**XAI Application/** - Contains the core API client and command-line interface
- Lightweight, terminal-based interaction
- Direct Python execution
- Ideal for server environments and scripting

**XAI UI/** - Contains the web-based user interface
- Built with Reflex framework
- Modern, responsive design
- Browser-based accessibility
- Real-time updates with reactive state

## Nugget Personality

"Nugget" is a distinct AI personality built into this application.

## Prerequisites

### Required Credentials

- **xAI API Key**: Obtain from [https://x.ai/api](https://x.ai/api)
- **Account**: Free tier available with usage limits

### Optional Requirements

- **Web Browser**: For Web UI (Chrome, Firefox, Safari, Edge)
- **Text Editor**: For configuration adjustments

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Joseph-dias/XAI-Application.git
cd XAI-Application
```

### Step 2: Obtain xAI API Key

1. Visit https://x.ai/api
2. Sign up or log in to your account
3. Generate an API key
4. Copy the API key securely

### Step 3: Set Up Environment Variables
1. **Option A:** Using Environment Variable (Recommended for Linux/macOS)
2. **Option B:** Using .env File (Recommended for Windows):  
   Create a .env file in the appropriate directory:  
   For CLI: XAI Application/.env  
   For Web UI: XAI UI/.env  

   ```Code
   XAI_API_KEY=your-api-key-here
   ```
### Step 4: Install Dependencies  
  
**For CLI Only:**
```bash
cd "XAI Application"
pip install -r requirements.txt
```

**For Web UI Only**
```bash
cd "XAI UI"
pip install -r requirements.txt
```

## Running the Application
```bash
python XAI_Application.py
```

### Basic Interaction
1. **Initial Greeting**: Nugget provides an automatic greeting
2. **Send Messages**: Type your message and press Enter
3. **Receive Responses**: Nugget responds with animated text
4. **View Citations**: Sources appear automatically below responses
5. **End Conversation**: Type "bye" to trigger farewell sequence

### Interactive Features
1. **Animated Text**: Responses appear with smooth character-by-character animation
2. **Live Indicators**: "Speaking to me:" prompt shows ready state
3. **Citation Display**: Sources displayed after responses
4. **Error Messages**: Clear feedback if API calls fail
5. **Loading States**: Visual indication when waiting for responses
