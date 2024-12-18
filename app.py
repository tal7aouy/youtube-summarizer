from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.chains.summarize import load_summarize_chain
from langchain_anthropic import ChatAnthropic
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
import os

app = Flask(__name__)

def get_video_id(video_url):
    """Extracts the video ID from a YouTube URL."""
    try:
        if "youtu.be" in video_url:
            return video_url.split("/")[-1]
        elif "youtube.com" in video_url:
            query = video_url.split("v=")[-1]
            return query.split("&")[0] 
        else:
            raise ValueError("Invalid YouTube URL")
    except Exception as e:
        return None


def get_youtube_transcript(video_url, languages=("en-US", "ar")):
    """Fetches the transcript from YouTube."""
    try:
        video_id = get_video_id(video_url)
        if not video_id:
            return "Error: Could not extract video ID from the URL."
        
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages)
        text = " ".join([t['text'] for t in transcript])
        return text
    except Exception as e:
        return f"Error: {str(e)}"

def summarize_text(text):
    try:
        llm = ChatAnthropic(model='claude-3-opus-20240229', api_key=os.environ["ANTHROPIC_API_KEY"])
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_text(text)
        documents = [Document(page_content=t) for t in texts]
        summarize_chain = load_summarize_chain(llm, chain_type="map_reduce")
        summary_result = summarize_chain.invoke(documents)
        return summary_result['output_text']
    except Exception as e:
        return f"Error in summarization: {str(e)}"

@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():
    incoming_msg = request.form.get("Body")
    print(f"Incoming message: {incoming_msg}")  
    
    response = MessagingResponse()
    if "youtube.com" in incoming_msg or "youtu.be" in incoming_msg:
        print("Processing YouTube URL...")  
        transcript = get_youtube_transcript(incoming_msg)
        if "Error" in transcript:
            print(f"Error: {transcript}")  
            response.message(transcript)
        else:
            summary = summarize_text(transcript)
            print(f"Summary: {summary}")  
            response.message(summary)
    else:
        response.message("Please send a valid YouTube URL.")
    return str(response)

if __name__ == "__main__":
    app.run(port=5000)
