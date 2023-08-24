# %%
import numpy as np
# 1) Input and Output with Numpy
# We already saw how to read file in Python 
# However, the creators of numpy have made it even easier

# Fill in 
Data = np.loadtxt("Data/Image2.txt",delimiter=",",dtype=int)

# Write the file using numpy
np.savetxt("Data/ImageWrite.txt",Data)

# %%
# If we have a more complex array, we can use another  
# type of file format, called pickle file format
# It is a binary file format, so it is not human    
# readable but it is very fast to read and write
# numpy has it's own version of pickle, called .npy    
# and .npz
np.save('Data/WriteFile.npy', Data)
X = np.load('Data/WriteFile.npy')
# npy is for single array, npz is for multiple arrays
Y = np.vstack((Data,Data))
np.savez('Data/WriteFile.npz', X, Y)
X,Y = np.load('Data/WriteFile.npz')
# %%
# 2) Plotting with Matplotlib
# Matplotlib is the most popular plotting library in Python
# Basic Plotting 
# PLot a cos function and a sin function from 0 to 2pi
import matplotlib.pyplot as plt

# Plot a cos function and a sin function from 0 to 2pi
X=np.linspace(0, 2*np.pi,1000)
y=np.cos(X)
y2=np.sin(X)
plt.plot(X,y,'*',label="Sin",color="green")
plt.plot(X,y2,label="Cos",color="blue")
plt.title("Cos and Sin")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()


# Change the color of the lines
# Fill in #done above



# change the line style
# Fill in #done above




# %%

# Histogram
# Let's plot a histogram of random numbers
# For a uniform distribution
# Fill in
x = np.random.uniform(0,100,10000)
plt.hist(x, bins=50)

# For a normal distribution
x = np.random.normal(0,100,10000)
# Fill in 
plt.hist(x, bins=50)
plt.savefig("Data/ImageHist")
# For an exponential distribution
x = np.random.exponential(10,10000)
# Fill in
plt.hist(x, bins=50)


# %%
# 3-D Plotting
# We can also plot 3-D plots

zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
# Plot a 3-D line
# Fill in
fig=plt.figure()
ax=plt.axes(projection="3d")
ax.plot3D(xline,yline,zline)
ax.scatter3D(xdata,ydata,zdata,c=zdata)

plt.show()


# Data for three-dimensional scattered points
# Fill in #done above




# Animation
from matplotlib.animation import FuncAnimation
# Make an animation of a particle moving in a circle

# Fill in 
fig=plt.figure()
def animate(i):
    i=i/5
    x=np.cos(i)
    y=np.sin(i)
    plt.clf()
    plt.scatter(x,y,color='r',s=100)
    plt.axis('square')
    plt.xlim(-1.5,1.5)
    plt.ylim(-1.5,1.5)
    plt.grid()
anim=FuncAnimation(fig,animate,frames=int(np.ceil(2*np.pi*5)),interval=50)
anim.save("Data/Animation.gif")



# %%
# Read Images in Python
# Let's read 'Image1.png' in Python
# We will use the PIL library
# to install PIL, use the following command pip install pillow
from PIL import Image, ImageOps
# Fill in 
im=Image.open("Data/Image1.png")
plt.axis('off')
plt.imshow(im)
plt.show()

# PIL also has also image processing functions
# Let's convert the image to grayscale
# Fill 
im2=ImageOps.grayscale(im)
plt.imshow(im2,cmap="Greys_r")
plt.show()


# There are many other functions, such as resize, rotate, crop, etc.
# You can convert the image to numpy array using np.array
# Fill in

array=np.array(im2)

# %%
# The opposite is also possible
# You can convert a numpy array to an image
# First load the Image2.txt file that I provided
# Then convert it to an image
# plot the image using plt.imshow 
# NOTE: The image is a grayscale image so
# you need to use cmap = 'Grays_r' option
# Then save it as a png file
# Fill in
im3=np.loadtxt("Data/Image2.txt",delimiter=",",dtype=int)
plt.imshow(im3)

# %%