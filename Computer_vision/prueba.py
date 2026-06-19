import cv2 as cv
from pathlib import Path

# Rutas
ruta1 = Path(__file__).parent / "imagen-ruido.jpg"
ruta2 = Path(__file__).parent / "imagen-ruido.jpg"

# Cargar en gris
img1 = cv.imread(str(ruta1), cv.IMREAD_GRAYSCALE)
img2 = cv.imread(str(ruta2), cv.IMREAD_GRAYSCALE)

if img1 is None:
    raise FileNotFoundError(f"No se pudo cargar: {ruta1}")

if img2 is None:
    raise FileNotFoundError(f"No se pudo cargar: {ruta2}")

# Crear detector/descriptor SIFT
sift = cv.SIFT_create()

# Detectar keypoints y calcular descriptores
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# Comparador de descriptores
bf = cv.BFMatcher(cv.NORM_L2, crossCheck=True)

# Comparar descriptores
matches = bf.match(des1, des2)

# Ordenar de mejor a peor match
matches = sorted(matches, key=lambda x: x.distance)

# Dibujar los 30 mejores matches
resultado = cv.drawMatches(
    img1, kp1,
    img2, kp2,
    matches[:30],
    None,
    flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
)

cv.imshow("Matches SIFT", resultado)
cv.waitKey(0)
cv.destroyAllWindows()