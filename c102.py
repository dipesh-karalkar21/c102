import cv2
import time
import random
import dropbox

startTime = time.time()


def captureImage() :
    image = cv2.VideoCapture(0)
    result = True
    while (result) :
        ret,frame = image.read()
        imageName = "Image" + str(random.randint(0 , 100)) + ".jpg"
        cv2.imwrite(imageName , frame)
        result = False
    print("Snapshot taken")
    image.release()
    cv2.destroyAllWindows()
    return imageName

def storeInDropbox(imageName) :
    accessToken = "sl.BNTeg8Bs8r4Vm87h-B3w5lIJXeXpM45j9ukQI0_F6YXyuKe9h0jSuCvbNmc431_DTWh9Dwyctlr4gQIZI9D-SGOLx3DFWNe0ADURaBh4A-XZWJAOdzuYm1Q6fDrDdBrVhJLo_UA"
    fileFrom = imageName 
    fileTo = "/image1/" + imageName

    dbx = dropbox.Dropbox(accessToken)

    with open(fileFrom , "rb" ) as f:
        dbx.files_upload(f.read() , fileTo , mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded Successfully")

def main() :
    while True :
        if ( (time.time() - startTime) >= 10 ):
            name = captureImage()
            storeInDropbox(name)

main()


