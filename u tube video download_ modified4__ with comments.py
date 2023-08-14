import os
from pytube import YouTube

# select folder to save downloaded files
selectPath = input("Enter the path of the folder to save downloads: ")

selectPath = repr(selectPath)   # will make raw string
l=list(selectPath)
while "'" in l:
    l.remove("'")   # will remove quotation in the path
selectPath = ''.join(l)

# if selected folder is not found
while os.path.isdir(selectPath)==False:     # will check if the directory exists or not 
    selectPath = input("No such directory! Enter again: ")  # will take input untill the input directory is found
    selectPath = repr(selectPath)   # will make raw string
    l=list(selectPath)
    while "'" in l:
        l.remove("'")   # will remove quotation in the path
    selectPath = ''.join(l)

no_of_downloads=0

while True:
    
    link = input("\nEnter the URL of the video: ")
    
    # if video is found
    try:
        mainVideo = YouTube(link)   # all details of the video will be assigned to mainVideo
        print("Fetching data...")
        print("\nTitle: ",mainVideo.title)  # will print the title of the video
        download = input("Enter 'D' to download and 'N' to skip: ")  # will keep track if we want to download or not
        
        # if wrong choice download or quit
        while download!='D' and download!='N':
            download = input("Wrong choice! enter either 'D' or 'N': ")  # will input choice until choice is correct
         
        # if we choose to download
        if download=='D':
            choice = input("Enter 1 to download audio only and 2 to download video: ")
            
            # if wrong choice audio or video
            while choice!='1' and choice!='2':
                choice = input("Wrong choice! enter either 1 or 2: ")   # will input choice until choice is correct
                    
            # if audio download
            if choice=='1':
                print("Loading all audio streams...")
                streams = mainVideo.streams.filter(only_audio=True)   # will assign all the streams which contains only audio to the 'streams' from the 'mainVideo'
                list_of_streams = list(streams)     # convert 'streams' to list and assign to 'list_of_streams', so that we can easily see the streams available in the video
                print("\nAll audio streams in the video:")
                for i in range(len(list_of_streams)):
                    print("index:",i+1,"  ",list_of_streams[i])     # will print all the audio streams 
                choice_stream = input("Enter the stream index according to which stream you want to download: ")    # the stream index we will choose  will be assigned to choice stream
                
                # if choice of stream is wrong
                # choice_stream should be only integers starting from 1 and upto the length of 'list_of_stream', if not it is wrong
                while choice_stream.isnumeric()==False or int(choice_stream)<1 or int(choice_stream)>len(list_of_streams):
                    choice_stream = input("stream index is out of range! choose the correct stream: ")    # will take input of choice stream until choice is correct
                
                # if correct choice then download
                name_of_file = input("Enter the filename or press Enter to set filename default: ")   # if we press enter while taking the input in 'name_of_file' then an empty string will be assigned to 'name_of_file'
                
                # if we select the file name default
                if name_of_file=='':    # empty string
                    l=list(mainVideo.title)     # will make list of the string 'mainVideo.title' (title of the video, which will be used to name the donloaded file)
                    while '|' in l:
                        l.remove('|')   # will remove all the '|' characters which is uatomatically added to the 'mainVideo.title'
                    s = ''.join(l)      # we are joining all the characters of list after deleting all '|' and assign to s
                    name_of_file = s+'.mp3'   # finally we are updating the 'name_of_file' variable with s(name of the file) adding '.mp3' exdtension as it will be a audio file
                    markFilename='*'    # will keep track that filename is set default
                
                # if we select a name of the file
                else:
                    markFilename = name_of_file     # 'markFilename' will be updated with a copy of the name_of_file as the 'name_of_file' is being changed in the next line
                    name_of_file = name_of_file+'.mp3'    # will update name_of_file adding '.mp3' extension
                checkFile = selectPath +"\\"+ name_of_file    # selectPath is the path we have selected to save downloads
                # 'checkfile' contains the filename along with the path we have selected to save downloads
                
                # now we need to check if the file we want to sownload already exists or not
                
                # file already exists, do not proceed further for that file
                if os.path.isfile(checkFile)==True:    
                    print("File already exists")
                    
                # file does not exists previously, proceed to download
                else:  
                    print("Downloading...")
                    os.chdir(selectPath)    # will change the current working directory to the folder we want to save downloads
                    downloaded_file = streams[int(choice_stream)-1].download()   # the file according to (the index we have choosen - 1)  will be downloaded and downloaded_file will point to that downloaded file
                    
                    # if default file name is selected
                    if markFilename=='*':
                        base, ext = os.path.splitext(downloaded_file)   # file name will be assigned to 'base' and extension will be assigned to 'ext'
                        new_file = base+'.mp3'    # new_file will be assigned the filename('base') with '.mp3' extension. it is used to change the extension
                        os.rename(downloaded_file, new_file)    # downloaded_file will be renamed with new_file. here just the extension will be changed
                    
                    # if file name is given
                    else:
                        new_file = markFilename+'.mp3'    # name of the file with '.mp3' extension will be assigned to new_file
                        os.rename(downloaded_file, new_file)    # the downloaded file will be renamed with new_file with '.mp3' extension
                    no_of_downloads+=1      # no_of_downloads will be incremented after each download
                    print("\n\nSuccessfully downloaded!")   
                    print("File is stored at:",os.getcwd())     # will show where file is saved
                    print(no_of_downloads,"files downloaded")
                  
            # if video download
            if choice=='2':
                print("Loading all video streams...")
                streams = mainVideo.streams.all()    # all of the streams present in the video will be assigned to 'streams'
                list_of_streams = list(streams)     # 'streams' will be converetd to list and assigned to 'list_of_streams'
                print("\nAll video streams in the video:")
                for i in range(len(list_of_streams)):
                    print("index:",i+1,"  ",list_of_streams[i])     # will print all the streams present in the video
                choice_stream = input("Enter the stream index according to which stream you want to download: ")    # choose according to which stream index we want to download
                
                # if choice of stream is wrong
                # choice_stream should be only integers starting from 1 and upto the length of 'list_of_stream', if not it is wrong
                while choice_stream.isnumeric()==False or int(choice_stream)<1 or int(choice_stream)>len(list_of_streams):
                    choice_stream = input("stream index is out of range! choose the correct stream: ")    # will take input of choice stream until choice is correct
                
                # if correct choice then download
                name_of_file = input("Enter the filename or press Enter to set filename default: ")     # if we press enter while taking the input in 'name_of_file' then an empty string will be assigned to 'name_of_file'
                
                # if we select the file name default
                if name_of_file=='':    # empty string
                    l=list(mainVideo.title)     # will make list of the string 'mainVideo.title' (title of the video, which will be used to name the donloaded file)
                    while '|' in l:
                        l.remove('|')       # will remove all the '|' characters which is uatomatically added to the 'mainVideo.title'
                    s = ''.join(l)          # we are joining all the characters of list after deleting all '|' and assign to s
                    name_of_file = s+'.mp4'     # finally we are updating the 'name_of_file' variable with s(name of the file) adding '.mp4' exdtension as it will be a video file
                    markFilename='*'    # will keep track that filename is set default
                    
                # if we select a name of the file
                else:
                    markFilename = name_of_file     # 'markFilename' will be updated with a copy of the name_of_file as the 'name_of_file' is being changed in the next line
                    name_of_file = name_of_file+'.mp4'      # will update name_of_file adding '.mp4' extension
                checkFile = selectPath +"\\"+ name_of_file    # selectPath is the path we have selected to save downloads
                # 'checkfile' contains the filename along with the path we have selected to save downloads
                
                # now we need to check if the file we want to sownload already exists or not
                
                # file already exists, do not proceed further for that file
                if os.path.isfile(checkFile)==True:
                    print("File already exists")
                    
                # file does not exists previously, proceed to download
                else:
                    print("Downloading...")
                    os.chdir(selectPath)    # will change the current working directory to the folder we want to save downloads
                    downloaded_file = streams[int(choice_stream)-1].download()   # the file according to (the index we have choosen - 1)  will be downloaded and downloaded_file will point to that downloaded file
                    
                    # if we have given name to that file, ie markFilename is not '*', we have to rename the downloaded file with 'name_of_file'
                    if markFilename!='*':
                        new_file = name_of_file
                        os.rename(downloaded_file, new_file)    # rename the downloaded file with new_file
                    
                    # if file name is set default we do not need to do anything more
                    
                    no_of_downloads+=1      # no_of_downloads will be incremented after each download
                    print("\nSuccessfully downloaded!")
                    print("File is stored at:",os.getcwd())    # will show where file is saved
                    print(no_of_downloads,"files downloaded")
        
    # if video is not found or any error has been occured
    except Exception as e:
        print(e)    # will show what error has been occured
        print("cannot find video")
            
    q = input("press Enter to continue or enter 'Q' to quit: ")
    if q=='Q':
        break     # if 'Q' is entered program execution will be stpped here
    
    # if user does not want to quit it will again ask for the URL of the next video to download, and the new videos will also be downloaded in the same folder