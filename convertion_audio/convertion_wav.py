from pydub import AudioSegment
import os

def convert_to_wav(input_file, output_file):
    # Verifica se o arquivo de entrada existe
    if not os.path.exists(input_file):
        print(f"O arquivo {input_file} não existe.")
        return

    # Carrega o arquivo de áudio usando Pydub
    audio = AudioSegment.from_file(input_file)

    # Salva o arquivo no formato WAV
    audio.export(output_file, format="wav")

if __name__ == "__main__":
    # Solicita o caminho do arquivo de áudio
    audio_file_path = input("Informe o caminho do arquivo de áudio: ")

    # Define o caminho de saída para o arquivo WAV
    wav_output_path = ("C:/Users/Odaias Pereira/PycharmProjects/convertion_log/convertion_audio/output_doc")


    # Chama a função para converter o arquivo para WAV
    convert_to_wav(audio_file_path, wav_output_path)

    print(f"Conversão concluída. Arquivo WAV salvo em: {wav_output_path}")