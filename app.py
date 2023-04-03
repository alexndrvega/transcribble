import openai
import requests
from pydub import AudioSegment

# Load and process the sound file using pydub, needed as OpenAI's API only takes WAV format.

# Load Audio File
def  load_audio_file(file_path):
    audio = AudioSegment.from_file(file_path)
    return audio

# Convert Audio File
def conver_to_wav(audio):
    wav_audio = audio.export("converted_audio.wav", format="wav")
    return wav_audio


# You need to use your own API key, replace "your_api_key".

openai.api_key = "your_api_key"

# Feed converted_audio.wav file to OpenAI for transcription.
def transcrive_audio(file_path):
    with open(file_path, "rb") as file:
        response = requests.post(
            "https://api.openai.com/v1/voice/speech-to-text",
            headers={
                "Authorization": f"Bearer {openai,api_key}",
                "Content-Type": "audio/wav",
            },
            data=file.read(),
        )

    response.raise_for_status()
    return response.json()["text"]

# Error handling and exeptions.
def main():
    input_file = "path/to/your/audio_file.mp3"
    output_file = "transcription.txt"

    try:
        audio = load_audio_file(input_file)
        wav_audio = conver_to_wav(audio)
        transcription = transcrive_audio("converted_audio.wav")

        with open(output_file, "w") as f:
            f.write(transcription)
        
        print(f"Transcription saved to {output_file}")
    
    except Exception as e:
        print(f"An error ocurred: {e}")
