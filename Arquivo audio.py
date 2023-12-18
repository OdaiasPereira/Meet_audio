import os
import speech_recognition as sr
import rewrite3 as r
from pydub import AudioSegment

def transcribe_audio_file():
    # Ask the user for the audio file path
    audio_file_path = input("Enter the audio file path: ")

    # Convert the path to an absolute path
    audio_file_path = os.path.abspath(audio_file_path)

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_file_path) as source:
        print(f"Transcribing audio file: {audio_file_path}")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        # Listen for audio input
        audio = recognizer.record(source)

        try:
            # Use Google Web Speech API to transcribe the speech in Portuguese (Brazil)
            text = recognizer.recognize_google(audio, language="pt-BR")
            print("Transcription: {}".format(text))
            return text
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Web Speech API; {0}".format(e))
        except Exception as e:
            print("An unexpected error occurred: {0}".format(e))

if __name__ == "__main__":
    # Call the transcription function and store the result in a variable
    transcribed_text = transcribe_audio_file()


    r.rewrite_text(transcribed_text)

    # Now you can use the 'transcribed_text' variable as needed

