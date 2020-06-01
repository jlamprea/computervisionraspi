# programa para calcular frame fps en varios escenarios
# 1) basico sin sin ninguna programacion especial.
    # prom 48 fps, min 34, max 68.
import cv2

captura = cv2.VideoCapture(0)
while (captura.isOpened()):
  timer= cv2.getTickCount() # inicia el tiempo de fps
  ret, imagen = captura.read()
  if ret == True:
    fps= cv2.getTickFrequency()/(cv2.getTickCount()-timer) # calcula el tiempo fps
    # voltea la imagen
    imagen = cv2.flip(imagen,0)
    cv2.putText(imagen, str(int(fps)),(75,50),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)
    cv2.imshow('video', imagen)
    #print("Frames por segundos: ", str(int(fps)))
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else: break
captura.release()
cv2.destroyAllWindows()