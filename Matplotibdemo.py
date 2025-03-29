# import matplotlib.pyplot as plt
# import  numpy as np
from pickletools import markobject

# xpoints = np.array([0,6])
# ypoints = np.array([0,250])
# plt.plot(xpoints,ypoints)
# plt.show()

# ===================----------==============

# xpoints = np.array([1,8])
# ypoints = np.array([3,10])
#
# plt.plot(xpoints,ypoints)
# plt.show()

# ===================----------==============


# xpoints = np.array([1, 8])
# ypoints=  np.array([3, 10])
#
# plt.plot(xpoints,ypoints,'o')
# plt.show()

# ===================----------==============


# ypoints = np.array([3, 8, 1, 10])
#
# plt.plot(ypoints, marker = 'D')
# plt.show()

# ===================----------==============
# # xpoints = np.array([8,10,2])
# ypoints = np.array([2,10,5,10,2])
# plt.plot( ypoints, marker="*")
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# x=np.array([1,10])
# y=np.array([20,50])
#
# plt.plot(x,y)
# plt.show()


# import matplotlib.pyplot as af
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([8,5,8,5,8,5,8,5,8,5,8,5,8,5,8,5,8,5,8,5])
# # y=np.array([50,1])
# af.plot(x, marker="d")
# af.show()

# import matplotlib.pyplot as plt
# import numpy as np
#
# y = np.array([1, 2, 3, 4])
#
# plt.plot(y, linestyle="dotted")  # Correct parameter name
# plt.show()
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# y = np.array([1, 2, 3, 4])
#
# plt.plot(y, linestyle= "--")
# plt.show()


# import  matplotlib.pyplot as plt
# import numpy as np
#
# x=np.array([3,6,9])
# y=np.array([5,8,9])
# plt.plot(x,y)
# font1={'family':'serif','color':'blue','size':20}
# plt.title("Hey",fontdict=font1)
# plt.xlabel("Afsal",fontdict=font1)
# plt.ylabel("Ahamed")
# plt.show()
# ===========================-----------------===========================



# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.lines import lineStyles
#
# x=np.array([6,12,26,32])
# y=np.array([12,26,32,46])
# plt.title("Afsal")
# plt.xlabel("Ahamed")
# plt.ylabel("Hash")
#
# plt.plot(x,y)
# plt.grid(color="green",linestyle="--",linewidth=0.5)
# plt.show()

# ===============================------------------==================


import  matplotlib.pyplot as plt
import numpy as np

x=np.array([5,7,8,12])
y=np.array([12,18,28,12])
plt.scatter(x,y)

plt.scatter(x,y)
plt.show()