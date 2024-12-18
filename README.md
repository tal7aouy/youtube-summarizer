# WhatsApp YouTube Summarizer

This is a Python Flask application that integrates with Twilio's WhatsApp API to summarize YouTube video content. The application uses LangChain with the Anthropic LLM (Claude) for text summarization and the `youtube_transcript_api` library to retrieve YouTube video transcripts.

### Features

- **YouTube Video Transcription**: Extracts the transcript from YouTube videos using the YouTube Transcript API.
- **Summarization**: Summarizes the extracted video content using LangChain with Anthropic's Claude LLM.
- **WhatsApp Integration**: Sends the video summary back to users via WhatsApp using Twilio's API.

### Requirements

1. Python 3.x
2. Flask
3. Twilio
4. YouTube Transcript API
5. LangChain
6. Anthropic (Claude) API Key

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tal7aouy/youtube-summarizer.git
   cd youtube-summarizer
   ```

````

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**:
   Create a `.env` file in the project root directory and add your Twilio and Anthropic API keys:

   ```
   ANTHROPIC_API_KEY=your_anthropic_api_key
   ```

5. **Run the Flask server**:

   ```bash
   flask run
   ```

6. **Set up the Twilio webhook**:

   - Set your **ngrok** URL or local Flask server URL as the webhook for incoming messages from Twilio.
   - Example: `https://your_ngrok_url/whatsapp`

7. **Test with WhatsApp**:
   - Send a YouTube video URL to your Twilio WhatsApp number.
   - The bot will respond with a summary of the video.

### Sample Interaction

**You send**:

```
https://youtu.be/5sLYAQS9sWQ
```

**Bot responds**:

```
GPT, a large language model, generates human-like text by predicting the next word in a sentence. Fine-tuning allows GPT to specialize in tasks like chatbots, content creation, and code generation, with more applications expected as the technology evolves.
```

### Troubleshooting

- If the bot is not responding to WhatsApp, make sure the webhook is properly configured in the **Twilio Console**.
- If you're encountering issues with the YouTube transcript, verify the video is available in the requested languages.

### Author

- **Name**: tal7aouy
- **Email**: talhaouy@gmail.com

---

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

```
````
