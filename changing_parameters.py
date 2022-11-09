import astropy.units as u
from einsteinpy.rays import Shadow
from einsteinpy.plotting import ShadowPlotter
import matplotlib.pyplot as plt
import numpy as np

# set mass and fov arrays
mass_array = [1*u.kg, 3*u.kg, 5*u.kg]
fov_array = [30*u.km, 40*u.km, 50*u.km]

# plot intensity graphs
fig = plt.figure(figsize=(15,10))
index = 1
for mass in mass_array:
  for fov in fov_array:
    shadow = Shadow(mass=mass, fov=fov, n_rays=1000)
    intensity = ShadowPlotter(shadow=shadow, is_line_plot=True)    
    plt.subplot(3,3,index)
    intensity.plot()
    plt.title(f'm={mass} and fov={fov}')
    index += 1

fig.tight_layout(pad=5.0)
plt.show()

#plot black holes graphs
index = 1
for mass in mass_array:
  for fov in fov_array:
    shadow = Shadow(mass=mass, fov=fov, n_rays=1000)
    bh = ShadowPlotter(shadow=shadow, is_line_plot=False)
    plt.subplot(3,3,index)
    bh.plot()
    xx = bh.r1 * np.cos(bh.theta1)
    yy = bh.r1 * np.sin(bh.theta1)
    #plt.pcolormesh(bh.r1, bh.theta1, bh.values1, cmap=plt.cm.afmhot, shading="gouraud")
    plt.pcolormesh(xx, yy, bh.values1, cmap=plt.cm.afmhot, shading="gouraud")
    #plt.contourf(xx, yy, bh.values1, cmap = plt.cm.afmhot, shading="gouraud")
    plt.title(f'm={mass} and fov={fov}')
    plt.gca().set_aspect("equal", adjustable="box")
    index += 1

fig.tight_layout(pad=0.5)
plt.show()