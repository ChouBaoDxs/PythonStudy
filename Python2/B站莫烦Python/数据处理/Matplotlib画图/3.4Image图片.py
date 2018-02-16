# -*- coding:utf-8 -*-
__author__ = 'dxs'
__date__ = '2018/1/17 下午6:30'

import matplotlib.pyplot as plt
import numpy as np

a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)

#interpolation————https://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')

#压缩右边的颜色条，长度为原来的92%
plt.colorbar(shrink=.92)

plt.xticks(())
plt.yticks(())
plt.show()

