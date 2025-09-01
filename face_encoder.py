# Script to add/register new student faces
import cv2

student_name = input("Enter student name: ")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("Register Face - Press 's' to save", frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite(f"images/{student_name}.jpg", frame)
        print(f"Saved {student_name}.jpg")
        break

cap.release()
cv2.destroyAllWindows()
