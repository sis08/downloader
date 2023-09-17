import os, sys, time
try:
    from pytube import YouTube
except ImportError:
    os.system('pip install -U pip')
    os.system('pip install pytube')
    print(" \n \n____________________________________")
    print("모듈 설치가 완료되었습니다.\n코드를 재시작해주세요.\n(5초 후 자동 종료됩니다.)")
    time.sleep(5)
    sys.exit()
print("유튜브 URL을 입력해주세요.")
url_input = input("[ex) https://www.youtube.com/watch]: ")
print("파일 형식을 입력해주세요")
info_input = input("[영상/오디오]: ")
print("파일 이름을 입력해주세요.")
name_input = input("[ex) 유튜브]: ")
name = str(name_input)
if info_input == "오디오":
    if not "youtu" in url_input:
        print('오류: 잘못된 URL입니다.')
        time.sleep(10)
        sys.exit()
    else:
        youtube = YouTube(url_input)
        audio_stream = youtube.streams.filter(only_audio=True).first()
        audio_stream.download(filename=name + '.mp3')
        print("다운로드 완료\n10초 후 자동종료됩니다.")
        time.sleep(10)
        sys.exit()
elif info_input == "영상":
    if not "youtu" in url_input:
        print('오류: 잘못된 URL입니다.')
        time.sleep(10)
        sys.exit()
    yt = YouTube(url_input)
    video_stream = yt.streams.get_highest_resolution()
    video_stream.download(filename=name + '.mp4')
    print("다운로드 완료\n10초 후 자동종료됩니다.")
    time.sleep(10)
    sys.exit()
else:
    print('오류: 잘못된 URL입니다.')
    time.sleep(10)
    sys.exit()