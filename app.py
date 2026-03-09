import streamlit as st
import os
from transcribe import transcrever_audio_longo

st.set_page_config(page_title="Transcritor de Áudio", page_icon="🎙️")

st.title("🎙️ Transcritor de Áudio")

# Inicializa o estado para guardar a transcrição, se não existir
if "transcricao" not in st.session_state:
    st.session_state.transcricao = None

arquivo_audio = st.file_uploader("Selecione um arquivo de áudio", type=["wav", "mp3", "m4a"])

if arquivo_audio is not None:
    st.audio(arquivo_audio)

    # Botão de ação
    if st.button("Transcrever Áudio", type="primary"):
        arquivo_temp = "temp_audio_file.m4a"
        
        with open(arquivo_temp, "wb") as f:
            f.write(arquivo_audio.getbuffer())

        with st.spinner("Processando o áudio..."):
            try:
                # Salva o resultado no session_state em vez de uma variável local
                st.session_state.transcricao = transcrever_audio_longo(arquivo_temp)
                st.success("Transcrição concluída!")
            except Exception as e:
                st.error(f"Erro: {e}")
            finally:
                if os.path.exists(arquivo_temp):
                    os.remove(arquivo_temp)

# Exibe o resultado se ele existir na "memória" do programa
if st.session_state.transcricao:
    st.divider()
    st.subheader("Resultado:")
    st.info(st.session_state.transcricao)
    
    # Adiciona um botão para baixar o texto (extra)
    st.download_button(
        label="Baixar Transcrição",
        data=st.session_state.transcricao,
        file_name="transcricao.txt",
        mime="text/plain"
    )