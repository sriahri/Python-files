mygraph = graph(width=420, height=240,xtitle='v (m/s)', ytitle='dN/dv (s/m)',title='Particle velocity distribution', fast=False)

mycurve = gcurve(color=color.red, width=4) # a graphics curve; it won't actually plot anything until line 10


# define variables

T = 298 # temperature in K

M = 4 # molar mass in g/mol

m = M*1.67e-27 # mass of one gas particle in kg

k = 1.38e-23 # Boltzmann constant in J/K


# create all v-values for plot from 0 to 2500 m/s in steps of 1 m/s

for v in arange(0, 2500., 1):

    F=4*pi*v**2*exp(-m*v**2/(2*k*T))*(m/(2*pi*k*T))**(3./2.) # calculate probability

    mycurve.plot(pos=(v,F)) # plot probability
