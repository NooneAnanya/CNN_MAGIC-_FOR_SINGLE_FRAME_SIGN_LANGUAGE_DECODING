import cv2
import os

directory= 'SignImg48x48/'
print(os.getcwd())

if not os.path.exists(directory):
    os.mkdir(directory) 
if not os.path.exists(f'{directory}/blank'):
    os.mkdir(f'{directory}/blank')

# Create directories for the signs
signs = ['BLESS', 'HELLO', 'I_LOVE_YOU', 'NO', 'OKAY', 'YES', 'blank']
for sign in signs:
    if not os.path.exists(f'{directory}/{sign}'):
        os.mkdir(f'{directory}/{sign}')

cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    count = {sign: len(os.listdir(directory+sign)) for sign in signs}

    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,300),(255,255,255),2)
    cv2.imshow("data",frame)
    frame=frame[40:300,0:300]
    cv2.imshow("ROI",frame)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame,(48,48))
    interrupt = cv2.waitKey(10)
    
    # Save the frame when the corresponding key is pressed
    if interrupt & 0xFF == ord('h'):  # 'h' for 'HELLO'
        cv2.imwrite(os.path.join(directory, 'HELLO', str(count['HELLO'])+'.jpg'), frame)
    if interrupt & 0xFF == ord('i'):  # 'i' for 'I_LOVE_YOU'
        cv2.imwrite(os.path.join(directory, 'I_LOVE_YOU', str(count['I_LOVE_YOU'])+'.jpg'), frame)
    if interrupt & 0xFF == ord('o'):  # 'o' for 'OKAY'
        cv2.imwrite(os.path.join(directory, 'OKAY', str(count['OKAY'])+'.jpg'), frame)
    if interrupt & 0xFF == ord('y'):  # 'y' for 'YES'
        cv2.imwrite(os.path.join(directory, 'YES', str(count['YES'])+'.jpg'), frame)
    if interrupt & 0xFF == ord('n'):  # 'n' for 'NO'
        cv2.imwrite(os.path.join(directory, 'NO', str(count['NO'])+'.jpg'), frame)
    if interrupt & 0xFF == ord('b'):  # '.' for 'bless'
        cv2.imwrite(os.path.join(directory, 'BLESS', str(count['BLESS'])+'.jpg'), frame)
    if interrupt & 0xFF == ord('.'):  # '.' for 'blank'
        cv2.imwrite(os.path.join(directory, 'blank', str(count['blank'])+'.jpg'), frame)    
    
    # Close the camera when the space key is pressed
    if interrupt & 0xFF == 32:  # ASCII value of the space key
        break

cap.release()
cv2.destroyAllWindows()