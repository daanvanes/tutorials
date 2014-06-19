### The dot product can geometrically be thought of as the length of the projection of one vector onto the other multiplied by the length of the vector that it is projected upon. However, because the eigenvalues are unit vectors (with length one), the dot product of a data point onto an eigenvector is defined only by the length (norm) of the projectied vector. If one wants to find the coordinates of a datapoint after rotation among the eigenvectors, we can simply compute it by taking the dot product of the point with the first eigenvector to get the x coordinate, and the dot product of the point and the second eigenvector to get the y coordinate. This is illustrated by:

## show data point with two 

data_point = np.array([3,5])
dot_product = dot(inv(v),data_point.T)
plt.figure(figsize=(5,5))
# plt.plot(xd,yd,'bo',markersize=4,zorder=1,alpha = 0.1)
plt.plot(data_point[0], data_point[1], 'bo',markersize=5, color='k')
# plt.plot(dot_product[0], dot_product[1], 'bo',markersize=5, color='g')
# plt.plot([-100,100],[0,0],'k')
# plt.plot([0,0],[-100,100],'k')
plt.axis('equal')
plt.xlim([-5, 10])
plt.ylim([-5,10])
plt.grid()
plt.title('Principal Components (eigenvectors) of random data', fontsize=12)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
scaled_eigenvec1 = [v[0,0]*sqrt(w[0]),v[1,0]*sqrt(w[0])]
scaled_eigenvec2 = [v[0,1]*sqrt(w[1]),v[1,1]*sqrt(w[1])]

plt.arrow(0,0,scaled_eigenvec1[0],scaled_eigenvec1[1],color='r',linewidth=2,head_width=.2,head_length=.2)
plt.arrow(0,0,scaled_eigenvec2[0],scaled_eigenvec2[1],color='r',linewidth=2,head_width=.2,head_length=.2)

shared_variance1 = dot_product[0]/np.linalg.norm(scaled_eigenvec1)*np.array(scaled_eigenvec1)

plt.arrow(0,0,shared_variance1[0],shared_variance1[1])
plt.arrow(data_point[0],data_point[1],(shared_variance1-data_point)[0],(shared_variance1-data_point)[1], linestyle = '-')
plt.text(2,0,str(np.linalg.norm(shared_variance1)))
plt.show()