import pytube
banner = ('''
$$\     $$\ $$$$$$$$\       $$$$$$$$\  $$$$$$\        $$\      $$\ $$$$$$$\  $$\   $$\ 
\$$\   $$  |\__$$  __|      \__$$  __|$$  __$$\       $$$\    $$$ |$$  __$$\ $$ |  $$ |
 \$$\ $$  /    $$ |            $$ |   $$ /  $$ |      $$$$\  $$$$ |$$ |  $$ |$$ |  $$ |
  \$$$$  /     $$ |            $$ |   $$ |  $$ |      $$\$$\$$ $$ |$$$$$$$  |$$$$$$$$ |
   \$$  /      $$ |            $$ |   $$ |  $$ |      $$ \$$$  $$ |$$  ____/ \_____$$ |
    $$ |       $$ |            $$ |   $$ |  $$ |      $$ |\$  /$$ |$$ |            $$ |
    $$ |       $$ |            $$ |    $$$$$$  |      $$ | \_/ $$ |$$ |            $$ |
    \__|       \__|            \__|    \______/       \__|     \__|\__|            \__|
                                    by die#9696/die-NA
 ''')
print(banner)
link = input("Enter the link you want to download : ")
direc = input("Enter the directory of where you want to download it : ")
youtube = pytube.YouTube(link)
video = youtube.streams.first()
video.download(direc)
