#AVAILABLE EXTENSIONS
extensions= {"py": "Python" , "mp3": "Audio File" , "mp4": "Video File" , "java": "Java" , "html": "HTML" , "css": "CSS"}

print("Available Extenstions: \n py\n mp3\n mp4\n java\n html\n css")
filename= input("Enter the file name: ")
check= filename.split(".")

#SAVING THE EXTENSION IN A VARIABLE
saved_ext= check[-1]

if saved_ext in extensions:
    print("The extension of the file is: ", extensions.get(saved_ext))
else:
    print("This extension does not exist in our database")