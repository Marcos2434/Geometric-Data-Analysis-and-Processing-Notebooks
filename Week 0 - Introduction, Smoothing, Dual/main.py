from pygel3d import hmesh, gl_display as gl
from pygel3d import graph

m = hmesh.load("bunny.obj")

print("Number of vertices: " + str(len(m.vertices())))

v = gl.Viewer()

v.display(m)

# go back to viewer
# v.envent_loop()

# delete the viewer object
# del v

# simplify mesh (to 10% it's original size)
hmesh.quadric_simplify(m, 0.1)

hmesh.close_holes(m)
hmesh.triangulate(m)

# Maximizes the minimum angle of triangles by flipping edges of m. Makes the mesh more Delaunay.
hmesh.maximize_min_angle(m, 0.95)

g = graph.from_mesh(m)

v.display(m, g, mode='x') # mode x-ray

s = graph.LS_skeleton(g)

v.display(m, s, mode='x')