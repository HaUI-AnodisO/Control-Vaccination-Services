import os

# Load Gemini API configuration
os.environ["GEMINI_API_KEY"] = 'AIzaSyDPwsWtk_tcdP6vNQZV0GH4NeaTUi7SsZY'

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
