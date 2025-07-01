import speech_recognition as sr
from gtts import gTTS
import winsound
from pydub import AudioSegment
import pyautogui
import webbrowser
from pydub.utils import which

AudioSegment.converter = which("ffmpeg")
AudioSegment.ffprobe = which("ffprobe")

# Fungsi normalisasi input suara
def normalize_command(command):
    replacements = {
        "alpha": "alfa",
        "yutub": "youtube",
        "yutup": "youtube",
        # Tambah variasi lainnya di sini
    }
    for wrong, correct in replacements.items():
        command = command.replace(wrong, correct)
    return command

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language='id-ID')
        print("You said:", command)
        return normalize_command(command.lower())
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return None
    except sr.RequestError:
        print("Unable to access the Google Speech Recognition API.")
        return None

def respond(response_text):
    print(response_text)
    tts = gTTS(text=response_text, lang='id')
    tts.save("response.mp3")
    sound = AudioSegment.from_mp3("response.mp3")
    sound.export("response.wav", format="wav")
    winsound.PlaySound("response.wav", winsound.SND_FILENAME)

tasks = []
listeningToTask = False

def main():
    global tasks
    menunggu_trigger = True

    while True:
        command = listen_for_command()

        if not command:
            continue

        if menunggu_trigger:
            if "alpha" in command or "alfa" in command:
                respond("Iya tuan")
                menunggu_trigger = False
            else:
                print("Menunggu kamu panggil: 'ita' atau 'alfa'")
        else:
            # Mode mendengarkan perintah
            if "buka youtube" in command:
                respond("Membuka YouTube untuk Anda.")
                webbrowser.open("https://www.youtube.com/")
            elif "ambil screenshot" in command:
                pyautogui.screenshot("screenshot.png")
                respond("Saya telah mengambil screenshot.")
            elif "siapa penciptamu" in command:
                respond("Dzakiy Al Husaini")
            elif "untuk apa kamu dibuat" in command:
                respond("tugas infor- eh maksudnya untuk membantu keseharian tuanku")
            elif "tambah tugas" in command:
                respond("Apa tugasnya?")
                task = listen_for_command()
                if task:
                    tasks.append(task)
                    respond(f"Tugas '{task}' telah ditambahkan. Total {len(tasks)} tugas.")
            elif "daftar tugas" in command:
                if tasks:
                    respond("Ini daftar tugas Anda:")
                    for task in tasks:
                        respond(task)
                else:
                    respond("Tidak ada tugas saat ini.")
            elif "keluar" in command:
                respond("Sampai jumpa!")
                break
            else:
                respond("Maaf, saya belum mengerti perintah itu.")

            # Kembali ke mode trigger setelah selesai perintah
            menunggu_trigger = True

if __name__ == "__main__":
    respond("Halo semua, aku adalah asistenmu. Panggil aku alfa.")
    main()
