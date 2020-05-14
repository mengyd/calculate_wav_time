import wave
import os

def scan_wav(directory: str = None):
    dir_duration = 0
    # if not directory.endswith("__MACOSX"):
    print("\t", "+" * 30)
    print("\t", "计算文件夹 <", directory, "> ...")

    # if not directory.endswith("__MACOSX"):
    # dir_duration = 0
    with os.scandir(directory) as filelist:
        for file in filelist:
            if file.is_dir() and not file.name.endswith("__MACOSX"):
                dir_duration += scan_wav(directory+"/"+file.name)
            elif file.name.endswith(".wav"):
                try:
                    audio = wave.open(directory+"/"+file.name, 'rb')
                    rate = audio.getframerate() # 总帧数
                    frames = audio.getnframes() # 采样频率
                    duration = frames/rate # 样本时长
                    dir_duration += duration
                except Exception:
                    pass
    # print("文件夹 <", directory + "/" + file.name, "> 内容：")
    print("\t", dir_duration, "秒")
    print("\t", dir_duration/60, "分钟")
    print("\t", "-" * 30)
    return dir_duration

''' ----------------------------Main----------------------------- '''

total_duration = 0
# get current working directory
workpath = os.getcwd()
print('<' * 40)
print("Working in:", workpath)
print('>' * 40)

total_duration = scan_wav(workpath)

print("*" * 40)
print("总时长：")
print(total_duration, "秒")
print(total_duration/60, "分钟")

# pause
os.system('pause')
