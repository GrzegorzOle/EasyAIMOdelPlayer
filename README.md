# Easy AI Model Player

Zainstaluj wymagania systemowe: Upewnij się, że masz zainstalowany CMake oraz odpowiednie kompilatory, które będą potrzebne do skompilowania biblioteki.

### Instalacja CMake - Windows
CMake jest narzędziem do zarządzania procesem budowania aplikacji. Aby zainstalować CMake:

Przejdź na oficjalną stronę CMake: https://cmake.org/download/
Wybierz wersję dla Windows (np. "Windows x64 Installer").
Zainstaluj CMake, zaznaczając opcję dodania CMake do zmiennych środowiskowych systemu (opcja Add CMake to the system PATH podczas instalacji).
Po instalacji, możesz sprawdzić, czy CMake został poprawnie zainstalowany, uruchamiając wiersz polecenia (CMD) i wpisując:

```commandline
cmake --version
```

### Instalacja kompilatorów (Microsoft Build Tools)
Do kompilacji projektów w Windows potrzebne są odpowiednie narzędzia budowania, takie jak Microsoft Visual C++ Build Tools. Możesz je zainstalować, wykonując poniższe kroki:

* Przejdź na stronę: https://visualstudio.microsoft.com/pl/visual-cpp-build-tools/
* Pobierz instalator Build Tools for Visual Studio.
* Uruchom instalator i wybierz następujące składniki:
* Desktop development with C++ (Rozwój aplikacji desktopowych w C++)
* W zależności od potrzeb, możesz także dodać inne opcje, np. zestawy SDK dla różnych wersji Windows.
* Po wybraniu odpowiednich składników kliknij Install.

Kompilatory Visual C++ będą teraz dostępne, co jest wymagane do budowania wielu bibliotek C++

```commandline
pip install gradio
```
Zainstaluj llama_cpp za pomocą pip: Najnowszą wersję llama_cpp można zainstalować bezpośrednio przez pip, wykonując następujące polecenie:

```commandline
pip install llama-cpp-python
```

Opcjonalnie: Instalacja z obsługą GPU: Jeśli posiadasz kartę GPU (na przykład NVIDIA RTX 3060) i chcesz skorzystać z akceleracji GPU, musisz upewnić się, że masz zainstalowane CUDA oraz odpowiednie sterowniki. Potem zainstaluj llama_cpp z obsługą GPU:

```commandline
LLAMA_CUBLAS=1 pip install llama-cpp-python
```
Użyty w projekcie model można pobrać: [Bielik-11B-v2.2-Instruct-GGUF](https://huggingface.co/speakleash/Bielik-11B-v2.2-Instruct-GGUF/tree/main)

Bezpośrednio w kodzie zmień wartości lokalne (ścieżki). 