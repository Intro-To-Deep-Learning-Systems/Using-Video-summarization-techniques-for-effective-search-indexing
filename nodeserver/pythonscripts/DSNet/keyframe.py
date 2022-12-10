import cv2#importing cv2 library
import numpy as np#importing numpy library

filename = '/Users/suryakiran/Downloads/using-video-summarization-techniques-for-effective-search-indexing/nodeserver/uploaded/files/image1670653463040.mp4'
def extract_keyframes(filename):
    def framing(video):#defining a small function named"framing" with a parameter "i" that's supposed to be provided for reading the video
        fr = []#creating an empty list named fr
        fr_pre=[]#creating an empty list named fr_pre
        cap = cv2.VideoCapture(video)#reading the video file
        while (cap.isOpened()):#This command builds a loop to check if the data is still being read from the video
            ret,frame = cap.read()#reading the data tunnel,gives two output where one tells about presence of frames(here it's ret) & the other speaks frame data(here it's frame)
            if ret == True:#checking for presence of frames
                # cv2.imshow("fbyf",frame)#displaying the frames
                grayed = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#Converting the frames to Grayscale from BGR
                canned = cv2.Canny(grayed,320,320)#For extrating edges we use Canny Edge detection method
                fr.append(frame)#Appending the read frame
                fr_pre.append(canned)#Appending the edge extracted frames
                # cv2.imshow("Grayed",grayed)#Displaying the original frames
                # cv2.imshow("Canned",canned)#Displaying the edge detected frames
                k = cv2.waitKey(10) & 0XFF#this is an arrangement for displaying the video where the secs for which each frame needs to be displayed in given in the paranthesis
                if k == ord('q'):#pressing 'q' key will close the video
                    break
            else:
                break
        cap.release()#Here we release the resoures
        cv2.destroyAllWindows()#Here we delete all the windows that were created during the program       
        return fr_pre,fr     #returning the frames received after the execution of function

    frames,ogframes = framing(filename)#calling function framing & then extracting the images         
    # cv2.destroyAllWindows() 

    diff = []#creatin a list variable
    for i in range(0,len(frames)-1):#defining the range
        # print(frames[i],frames[i+1])#checking the frames presence
        diff.append(cv2.absdiff(frames[i],frames[i+1]))#appending the diff between frames to the list variable so we're supposed to get only the difference between frames

    mn = np.mean(diff)#This gives mean
    st_d = np.std(diff)#This gives standard deviation

    a = 12#Setting a random value we can modify it to any value 
    ts = mn + (a * st_d)#defining the standard threshold value for the project/global threshold value
    print('The threshold==>',ts)

    a_fr = []#Creating an empty list
    for i in range(len(diff)):#Defining the for loop to be looped over all the frames obtained after finding the frames resulted from subtracting
        mn = np.mean(diff[i])#Calculating the mean for each frame
        st_d = np.std(diff[i])#Calculating the standard deviation for each frame
        fr_ts = mn + (4*st_d)#Finding the threshold values for each frame/image
        # print(i,fr_ts)
        a_fr.append([i,fr_ts])#Appending the frame number & the threshold values


    imp_fr = []#Creating an empty list
    for i,ac_tr in(a_fr):#Defining the loop on the list obtained from above code
        if ac_tr >= ts:#Comapring the threshold values to the standard threshold/global threshold values
            # print(i,ac_tr)
            imp_fr.append([i,ac_tr])#Appending the list with the imp frames based on their index & the values

    key_fr = []#Creating an empty list
    for i,_ in imp_fr:#Defining the loop over the list obtained from above code
        key_fr.append(ogframes[i])#This extracts the frames based on the index of frames 
        print(diff[i],i)


    # for i in range(len(key_fr)):
    #     cv2.imshow('keys',key_fr[i])
    #     print("Frame no==>",i)
    #     k = cv2.waitKey(100) & 0xFF
    #     if k == ord('q'):
    #         break
    # cv2.destroyAllWindows()
    im_paths = []
    for i in range(len(key_fr)):
        # cv2.imshow('diff',frames[i])
        # cv2.imshow('keys',key_fr[i])
        path = "/Users/suryakiran/Downloads/using-video-summarization-techniques-for-effective-search-indexing/images/"+str(i)+".png"
        cv2.imwrite(path,key_fr[i])#Mention preferred path
        im_paths.append(path)
        # k = cv2.waitKey(100) & 0xFF
        # if k == ord('q'):
        #     break
    # cv2.destroyAllWindows()

    print(len(frames))
    print(len(key_fr))
    return im_paths

