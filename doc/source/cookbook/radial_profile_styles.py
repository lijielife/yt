### THIS RECIPE IS CURRENTLY BROKEN IN YT-3.0
### DO NOT TRUST THIS RECIPE UNTIL THIS LINE IS REMOVED

import yt
import matplotlib.pyplot as plt

ds = yt.load("GasSloshing/sloshing_nomag2_hdf5_plt_cnt_0150")

# Get a sphere object

sp = ds.sphere(ds.domain_center, (500., "kpc"))

# Bin up the data from the sphere into a radial profile

#rp = BinnedProfile1D(sphere, 100, "Radiuskpc", 0.0, 500., log_space=False)
#rp.add_fields("density","temperature")
rp = yt.ProfilePlot(sp, 'radius', ['density', 'temperature'])
rp = yt.create_profile(sp, 'radius', ['density', 'temperature'],
                       units = {'radius': 'kpc'},
                       logs = {'radius': False})

# Make plots using matplotlib

fig = plt.figure()
ax = fig.add_subplot(111)

# Plot the density as a log-log plot using the default settings
dens_plot = ax.loglog(rp.x, rp["density"])

# Here we set the labels of the plot axes

ax.set_xlabel(r"$\mathrm{r\ (kpc)}$")
ax.set_ylabel(r"$\mathrm{\rho\ (g\ cm^{-3})}$")

# Save the default plot

fig.savefig("density_profile_default.png" % ds)

# The "dens_plot" object is a list of plot objects. In our case we only have one,
# so we index the list by '0' to get it. 

# Plot using dashed red lines

dens_plot[0].set_linestyle("--")
dens_plot[0].set_color("red")

fig.savefig("density_profile_dashed_red.png")

# Increase the line width and add points in the shape of x's

dens_plot[0].set_linewidth(5)
dens_plot[0].set_marker("x")
dens_plot[0].set_markersize(10)

fig.savefig("density_profile_thick_with_xs.png")
