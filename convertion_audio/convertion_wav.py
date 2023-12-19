from pydub import AudioSegment
import os

def convert_to_wav(input_file, output_folder):
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"The file {input_file} does not exist.")
        return

    # Load the audio file using Pydub
    audio = AudioSegment.from_file(input_file)

    # Extract the file name (without extension) from the input file path
    input_file_name = os.path.splitext(os.path.basename(input_file))[0]

    # Create the output file path by combining the output folder and the input file name with the .wav extension
    output_file_path = os.path.join(output_folder, f"{input_file_name}.wav")

    # Save the file in WAV format
    audio.export(output_file_path, format="wav")

if __name__ == "__main__":
    # Ask for the path of the audio file
    audio_file_path = input("Enter the path of the audio file: ")

    # Ask for the output folder where the WAV file should be saved
    wav_output_folder = input("Enter the output folder path for the WAV file: ")

    # Ensure that the output folder exists
    os.makedirs(wav_output_folder, exist_ok=True)

    # Call the function to convert the file to WAV
    convert_to_wav(audio_file_path, wav_output_folder)

    print(f"Conversion completed. WAV file saved at: {os.path.join(wav_output_folder, os.path.basename(audio_file_path))}.wav")