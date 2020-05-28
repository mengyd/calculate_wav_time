import wave
import os

def scan_wav(directory: str = None, sublevel = None):
    dir_duration = 0

    print("\t" * sublevel, "|", "+" * 30)
    print("\t" * sublevel, "|", "计算文件夹 <", directory, "> ...")

    with os.scandir(directory) as filelist:
        for file in filelist:
            if file.is_dir() and not file.name.endswith("__MACOSX"): # if is directory
                dir_duration += scan_wav(directory+"/"+file.name, sublevel+1)
            elif file.name.endswith(".wav"): # if is wave file
                try:
                    audio = wave.open(directory+"/"+file.name, 'rb')
                    rate = audio.getframerate() # totle frame number
                    frames = audio.getnframes() # frame rate
                    duration = frames/rate # duration
                    dir_duration += duration
                except Exception:
                    pass
    
    print("\t" * sublevel, "|", format(dir_duration, '.0f'), "秒")
    print("\t" * sublevel, "|", format(dir_duration/60, '.0f'), "分钟", format(dir_duration%60, '.0f'), "秒")
    print("\t" * sublevel, "|", "-" * 30)
    return dir_duration

''' ----------------------------Main----------------------------- '''

total_duration = 0
sublevel_counter = 0
# get current working directory
workpath = os.getcwd()
print('<' * 40)
print("Working in:", workpath)
print('>' * 40)

total_duration = scan_wav(workpath, sublevel=sublevel_counter)

print("*" * 40)
print("总时长：")
print(format(total_duration, '.0f'), "秒")
print(format(total_duration/60, '.0f'), "分钟", format(total_duration%60, '.0f'), "秒")

# pause
os.system('pause')
