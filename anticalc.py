import os
import psutil
import ctypes
import pyaudio
import struct
import time

def bytebeat(t):
    return (t*(((t>>9)^((t>>9)-1)^1)%13)) & 255



def play_bytebeat():
    sample_rate = 8000
    duration = 5
    num_samples = sample_rate * duration
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt8,
                    channels=1,
                    rate=sample_rate,
                    output=True)

    for t in range(num_samples):
        sample = bytebeat(t)
        stream.write(struct.pack('B', sample))

    stream.stop_stream()
    stream.close()
    p.terminate()


def kill_calculator(proc):
    try:
        proc.terminate()  # Hesap Makinesini sonlandır
        print("Hesap Makinesi kapatıldı.")
    except psutil.NoSuchProcess:
        print("Hesap Makinesi zaten kapalı.")














def is_calculator_running():
    for proc in psutil.process_iter(['name','pid']):
        if 'calc' in proc.info['name'].lower():  # Genel kontrol
            return proc
    return None


def main():
    while True:
        proc = is_calculator_running()
        if proc:
            print("Hesap Makinesi çalışıyor, Bytebeat çalıyor...")

            ctypes.windll.user32.MessageBoxW(0, "You are banned from calculator.", "Windows", 1)
            kill_calculator(proc)  # Hesap makinesini kapat
            play_bytebeat()  # Bytebeat müziğini çal

        else:
            print("Hesap Makinesi çalışmıyor.")

        time.sleep(1)  # Her saniye kontrol et


if __name__ == "__main__":
    main()


