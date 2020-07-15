from pytube import YouTube

url = input("Please input the link: ")
yt = YouTube(url)
stream = yt.streams.filter(progressive = True)
print(*stream, sep='\n')
print('\n'"Above are the available itag(s) from which you can download the video.")
itag = int(input('\n'"Please enter the itag value from the above list: "))
folder = input('\n'"Please enter the folder name were you want to save video: ") # Skip this if you want to save it in current directory. 
dnld = yt.streams.get_by_itag(itag).download(folder) 
print(dnld)
print('\n'"Yep! Your Video is downloaded")
