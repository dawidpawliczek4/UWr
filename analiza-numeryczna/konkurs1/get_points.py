import matplotlib.pyplot as plt

clicked_points = []

def onclick(event):
    # event.xdata i event.ydata to współrzędne w układzie wykresu
    if event.xdata is not None and event.ydata is not None:
        clicked_points.append((event.xdata, event.ydata))
        print(f"Kliknięto w: ({event.xdata}, {event.ydata})")

fig, ax = plt.subplots()
# jeżeli chcesz w tle mieć obrazek odręcznego napisu:
img = plt.imread('original.png')
ax.imshow(img, extent=[0, img.shape[1], img.shape[0], 0])  # dopasuj extent i odwróć oś y, jeśli trzeba

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

# Po zamknięciu okienka 'clicked_points' zawiera listę (x, y).
# Możesz to teraz np. zapisać do pliku:
with open('punkty.txt', 'w') as f:
    for (x, y) in clicked_points:
        f.write(f"({x}, {y})\n")
