# empty file 
def largeFileCreator(fileSize, filename = "file.useless"):
    onegb = 1024 * 1024 * 1024
    with open(filename, 'wb') as file:
        for i in range(fileSize):
            file.seek(onegb, 1)
        
        file.write(" ".encode())
    
# file fill with 0
def largeFileCreator2(fileSize, filename = "file.useless"):
    halfgb = "0"*1024*1024*512
    
    with open(filename, 'w') as file:
        for i in range(fileSize):
            file.write(halfgb)
            file.write(halfgb)
            
