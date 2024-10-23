import gradio as gr
from llama_cpp import Llama
import time  # Import modułu do pomiaru czasu

# Ścieżka do modelu GGUF (dostosuj ścieżkę do swojego pliku lub umieść w tym samym folderze)
model_path = "D:/AI/models/lmstudio-community/Bielik-11B-v2.2-Instruct.Q4_K_M-GGUF/Bielik-11B-v2.2-Instruct.Q4_K_M.gguf"

# Inicjalizacja modelu z wykorzystaniem GPU
llm = Llama(model_path=model_path, use_mmap=True, verbose=False, n_ctx=4096, n_batch=32, use_opencl=True) # n_gpu_layers=50,

# Funkcja interakcji z modelem, mierząca czas odpowiedzi
def chat_with_model(prompt):
    start_time = time.time()  # Zapisanie czasu początkowego
    response = llm(prompt, max_tokens=1024, temperature=0.2, top_p=0.9, stop=["User:", "Assistant:", "Użytkownik:"])
    end_time = time.time()    # Zapisanie czasu końcowego
    elapsed_time = end_time - start_time  # Obliczenie czasu generowania odpowiedzi
    response_text = response["choices"][0]["text"]

    # Dołączenie informacji o czasie generowania do odpowiedzi
    response_with_time = f"{response_text}\n\n**Czas generowania odpowiedzi: {elapsed_time:.2f} sekundy**"
    return response_text, response_with_time

# Funkcja Gradio do obsługi historii konwersacji
def interactive_chat(user_input, history):
    # Inicjalizacja historii, jeśli jest pusta
    history = history or []

    # Dodanie bieżącego zapytania użytkownika do formatu promptu
    formatted_input = f"User: {user_input}\nAssistant:"
    prompt = "\n".join([f"User: {item[0]}\nAssistant: {item[1]}" for item in history]) + f"\n{formatted_input}"

    # Uzyskanie odpowiedzi z modelu oraz czasu generowania
    response_text, response_with_time = chat_with_model(prompt)

    # Dodanie „czystej” odpowiedzi do historii dla przyszłych zapytań
    history.append((user_input, response_text))  # Przechowuj tylko czystą odpowiedź

    # Aktualizacja historii widocznej w Gradio (ostatni element zawiera czas generowania)
    display_history = history[:-1] + [(user_input, response_with_time)]

    return display_history, history, ""  # Zwracamy widoczną historię z czasem oraz surową historię

# Definiowanie interfejsu Gradio z użyciem CSS do dostosowania wysokości komponentu
with gr.Blocks(css=".chatbot {height: 90vh;} .textbox {height: 10vh;}") as demo:
    gr.Markdown("<h1><center>Chatbot Bielik-11B-v2.2-Instruct.Q4_K_M.gguf</center></h1>")

    # Komponent chatbot z określoną klasą CSS dla stylizacji
    chatbot = gr.Chatbot(elem_classes="chatbot")

    with gr.Row():
        with gr.Column():
            user_input = gr.Textbox(placeholder="Wprowadź tekst...", elem_classes="textbox")
        with gr.Column():
            submit_btn = gr.Button("Wyślij")

    # Definiowanie stanu i akcji przycisku
    state = gr.State()
    submit_btn.click(interactive_chat, inputs=[user_input, state], outputs=[chatbot, state, user_input])

# Uruchomienie interfejsu z udostępnieniem publicznym wyłączonym (share=False)
# Jeżeli chcesz zmienić zasięg poąłczeń poza localhost zmień wartość server_name np.: server_name="192.168.200.1"
demo.launch(server_port=8089, server_name="localhost", share=False)