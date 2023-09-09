import subprocess as subp
from os.path import join
import time

def start_record(name):
    log_dir = 'video/' # путь куда положить файл с записью
    CORE_DIR = 'C:\\Users\\IvanS\\OneDrive\\Документы\\Я\\ffmpeg-6.0-full_build-shared\\bin' # путь где лежит ffmpeg.exe
    video_file = join(log_dir, 'video_' + name + '.mp4')
    FFMPEG_BIN = join(CORE_DIR, 'ffmpeg.exe')

    command = [
        FFMPEG_BIN,
        '-f', 'gdigrab',
        '-framerate', 'ntsc',
        '-offset_x', '-1920',
        '-offset_y', '0',
        '-video_size', '1920x1080',
        '-i', 'desktop',
        # '-list_devices', 'true',
        '-f', 'dshow',
        # '-i', 'dummy',
        '-i', 'audio=@device_cm_{33D9A762-90C8-11D0-BD43-00A0C911CE86}\wave_{8D96F64C-944C-4E3F-B6F2-E0C185CAB755}',
        video_file
    ]
    print(" ".join(command))
    ffmpeg = subp.Popen(command, stdin=subp.PIPE)
    return ffmpeg
    

def end_record(ffmpeg):
    ffmpeg.communicate(b"q")
    ffmpeg.stdin.close()

def main():
    ffmpeg = start_record("1")
    time.sleep(10)
    end_record(ffmpeg)

if __name__ == "__main__":
    main()