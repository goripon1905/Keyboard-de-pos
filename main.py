import keyboard
from pydub import AudioSegment
from pydub.playback import play
import threading

print("終了するにはescキーを押してください...")
SOUND_FILE_PATH = "sound.wav"
sound = AudioSegment.from_wav(SOUND_FILE_PATH)

key_press_count = 0

def on_key_pressed(event):
    global key_press_count
    key_press_count += 1
    play_sound()

def play_sound():
    global key_press_count
    play_thread = threading.Thread(target=play, args=(sound,))
    play_thread.start()
    key_press_count -= 1
keyboard.on_press(on_key_pressed)

keyboard.wait("esc")
