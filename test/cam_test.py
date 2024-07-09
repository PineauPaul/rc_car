import cv2
import numpy as np

# Ouvrir la capture vidéo avec l'ID de la caméra (0 pour la première caméra, 1 pour la deuxième, etc.)
cap = cv2.VideoCapture(0)

# Vérifier si la caméra est correctement ouverte
if not cap.isOpened():
    print("Erreur: Impossible d'ouvrir la caméra.")
    exit()

while True:
    # Capturer une seule image du flux vidéo
    ret, frame = cap.read()

    # Vérifier si la capture est réussie
    if not ret:
        print("Erreur: Échec de la capture de l'image.")
        break

    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Appliquer un flou pour réduire le bruit
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Appliquer la détection de contours avec le filtre de Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Appliquer la transformation de Hough pour détecter les lignes
    lines = cv2.HoughLines(edges, 1, np.pi/180, threshold=100)

    # Dessiner les lignes détectées sur l'image originale
    if lines is not None:
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Afficher l'image avec les lignes détectées
    cv2.imshow('Line Detection', frame)

    # Attendre la touche 'q' pour quitter
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources de la caméra
cap.release()
cv2.destroyAllWindows() 
