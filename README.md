# Student Study Helper AI Chatbot

A Streamlit-based chatbot that helps students with their studies using either Gemini or OpenAI.

## Features

- Interactive chat interface
- AI-powered responses using Gemini or OpenAI
- Conversation history stored in session
- Personalized responses based on chat history

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Create a `.env` file with either a Gemini key (recommended for your setup) or an OpenAI key:
   Gemini option:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   GEMINI_MODEL=gemini-2.5-flash
   ```

   OpenAI option:
   ```
   OPENAI_API_KEY=your_api_key_here
   OPENAI_MODEL=gpt-4o-mini
   ```

3. Run the app:
   ```
   streamlit run app.py
   ```

## Future Enhancements

- Store study progress in a database
- Generate quizzes
- Note-taking features
- User authentication
