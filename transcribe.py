from dotenv import load_dotenv
import os
import assemblyai as aai

load_dotenv()

# Configure sua chave
aai.settings.api_key = os.getenv("ASSEMBLY_API_KEY")

def transcrever_audio_longo(arquivo):
    if not arquivo:
        return None

    config = aai.TranscriptionConfig(
        speaker_labels=True, 
        language_code="pt",
        language_detection=False, 
        speech_models=["universal-3-pro"],
        punctuate=True,
        format_text=True
    )

    transcriber = aai.Transcriber()
    
    # O método transcribe é síncrono e aguarda a finalização por padrão
    transcript = transcriber.transcribe(arquivo, config)

    if transcript.status == aai.TranscriptStatus.error:
        print(f"Erro na transcrição: {transcript.error}")
        return None

    return transcript.text
