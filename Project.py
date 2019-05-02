#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cmath


# In[28]:


r = int(input("r?"))
h = int(input("h?"))
π = (3.142)


# In[29]:


def sarea():
    SA = (π*r)*(r+(h**2+r**2)**(1/2))
    sarea = SA
    return sarea
print(type(sarea))


# In[30]:


sarea()


# In[31]:


def lsarea():
    LSA = (π*r)*((h**2+r**2)**(1/2))
    lsarea = LSA
    return lsarea
print(type(lsarea))


# In[32]:


lsarea()


# In[33]:


def barea():
    BA = (π*(r**2))
    barea = BA
    return barea
print(type(barea))


# In[34]:


barea()


# In[35]:


def volume():
    V = (π*(r**2))*(h/3)
    volume = V
    return volume
print(type(volume))


# In[36]:


volume()


# In[37]:


def Graph():
    from matplotlib import pyplot as p
    from mpl_toolkits.mplot3d import Axes3D    # @UnusedImport

    import numpy as np
    from math import pi, cos, sin

    z = np.arange(0, h, 0.06)
    theta = np.arange(0, 2 * np.pi, pi / 50)

    fig = p.figure()
    axes1 = fig.add_subplot(111, projection='3d')
    for zval in z:
        x = (2*r) * zval * np.array([cos(q) for q in theta])
        y = (2*r) * zval * np.array([sin(q) for q in theta])
        axes1.plot(x, y, zval, 'b-')
    axes1.set_xlabel("x label")
    axes1.set_ylabel("y label")
    axes1.set_zlabel("z label")


# In[38]:


Graph()

