<<<<<<< HEAD
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
=======
A focused AI-powered learning assistant designed to solve student doubts with structured, step-by-step explanations aligned to specific subjects and workshop content.

Unlike generic AI tools, this chatbot is trained on curated learning material, real classroom patterns, and common student mistakes, enabling it to deliver explanations that are simpler, more relevant, and easier to understand.

It supports:

Instant doubt resolution with clear examples
Concept breakdown tailored to student level
Guided learning instead of random answers
Context-aware responses based on syllabus and topics

Built using Python and advanced language models from OpenAI, the system integrates real-time interaction with personalized educational content to enhance student understanding and engagement.
>>>>>>> 058d4fc5906d2a0a3c7d7ebaa2181b6716aabef3
