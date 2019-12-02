from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import cm
import pandas as pd
import ffmpeg as ffmpeg

url = 'popcoord.xlsx'
data = pd.read_excel(url)

print(data)

fig = plt.figure()

ax = plt.axes(projection='3d')
ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.grid(False)
ax.patch.set_facecolor('#f0fff9')
#fig.patch.set_facecolor((0,250/255,154/255, .15))

ax.set_title('1000 Most Populated US Cities')
ax.set_xlabel('Latitude')
ax.set_ylabel('Longitude')
ax.set_zlabel('Population (In Millions)')
txt = "IG: do_not_wink | Reddit: donotwink"
fig.text(.75, .02, txt, ha='right', fontsize = 7)

num_points = 998
zdata = np.zeros(num_points)
ydata = data['long']
xdata = data['lat']

z_size = data['Population']
x_size = np.ones(num_points)
y_size = np.full(num_points, 1/2)

cmap = cm.get_cmap('spring')
max_height = np.max(z_size)
min_height = np.min(z_size)
rgba = [cmap((k-min_height)/max_height) for k in z_size]

#ax.bar3d(xdata, ydata, zdata, x_size, y_size, z_size, cmap='viridis')
#plt.show()

def init():
    ax.bar3d(xdata, ydata, zdata, x_size, y_size, z_size, color=rgba);
    return fig,

def animate(i):
    ax.view_init(elev = 30, azim=i/2-100)
    return fig,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=720, interval=20, blit=True)

anim.save('barco.mp4', fps = 30, savefig_kwargs={'facecolor': '#f0fff9'}, dpi = 150)
