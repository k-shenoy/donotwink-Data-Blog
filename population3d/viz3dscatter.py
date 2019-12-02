from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
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
ax.patch.set_facecolor('#ebfff7')
#fig.patch.set_facecolor((0,250/255,154/255, .15))

ax.set_title('1000 Most Populated US Cities')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_zlabel('Population (In Thousands)')
txt = "IG: do_not_wink | Reddit: donotwink"
fig.text(.98, .02, txt, ha='right', fontsize = 7)

ydata = data['long']
xdata = data['lat']
zdata = data['Population']

ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='spring', edgecolors='black')

def init():
    ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='spring', edgecolors='black');
    return fig,

def animate(i):
    ax.view_init(elev = 30, azim=i)
    return fig,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=360, interval=20, blit=True)

anim.save('scatter.mp4', fps = 30, savefig_kwargs={'facecolor': '#ebfff7'}, dpi = 150)
