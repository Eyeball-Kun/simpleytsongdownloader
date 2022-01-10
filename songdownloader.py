import youtube_dl

def download(song):
    ydl_opts = {'format': 'bestaudio/best',  # choice of quality
                'postprocessors': [{'key': 'FFmpegExtractAudio',  
                                    'preferredcodec': "mp3",}],}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading...")  # print to show that the program is working
        ydl.download([song])  # download song

    return "Downloaded"


def main():
    print("""
        _      _                                   _                         _                    _             
       | |    (_)                                 | |                       | |                  | |            
   ___ | |__   _  _ __    __ _   __ _  _   _    __| |  ___ __      __ _ __  | |  ___    __ _   __| |  ___  _ __ 
  / __|| '_ \ | || '_ \  / _` | / _` || | | |  / _` | / _ \\ \ /\ / /| '_ \ | | / _ \  / _` | / _` | / _ \| '__|
 | (__ | | | || || | | || (_| || (_| || |_| | | (_| || (_) |\ V  V / | | | || || (_) || (_| || (_| ||  __/| |   
  \___||_| |_||_||_| |_| \__, | \__, | \__, |  \__,_| \___/  \_/\_/  |_| |_||_| \___/  \__,_| \__,_| \___||_|   
                          __/ |  __/ |  __/ |                                                                   
                         |___/  |___/  |___/                                                                    
""")
    song = input("Enter a youtube link:") 
    download(song)


if __name__ == '__main__':  
    main()