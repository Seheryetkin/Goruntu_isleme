import cv2

image = cv2.imread("foto.png")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

print("orjinal resim: ", image)
print("gri ölçekli resim: ", gray)

(thresh, blackAndWhiteImage) = cv2.threshold(gri ölçekli resim, 20, 255, cv2.THRESH_BINARY)
(thresh, blackAndWhiteImage) = cv2.threshold(gri ölçekli resim, 80, 255, cv2.THRESH_BINARY)
(thresh, blackAndWhiteImage) = cv2.threshold(gri ölçekli resim, 160, 255, cv2.THRESH_BINARY)
(thresh, blackAndWhiteImage) = cv2.threshold(gri ölçekli resim, 200, 255, cv2.THRESH_BINARY)
plt.imshow(blackAndWhiteImage)
plt.show()



print(image.shape)
print(image.size)

cv2.imshow("foto",image)
cv2.imshow("foto gri ölçekli",gray )

cv2.waitKey(0)
cv2.destroyAllWindows()