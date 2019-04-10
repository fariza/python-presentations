import PSU, Radiometer, Camera
import numpy as np

psu = PSU()
rad = Radiometer()
cam = Camera()

x = []
y1 = []
y2 = []
for current in np.linspace(0, 0.35, 100):
    psu.current = current
    x.append(rad.radiance)
    img = camera.grab()
    y1.append(img.mean())
    y2.append(img.std())


# save into database
# process data
#....
