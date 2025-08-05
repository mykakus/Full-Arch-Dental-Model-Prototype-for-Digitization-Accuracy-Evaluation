import trimesh 
import igl
import numpy as np

def SDF_individual_sphere(A):
    Sphere_OG_d=trimesh.primitives.Sphere(A[0],A[1],subdivisions =4) # buvo su subdivision =4
    SDF, _, _ = igl.signed_distance(A[2], Sphere_OG_d.vertices,Sphere_OG_d.faces, return_normals=False)
    RMSE_val=np.sqrt(np.mean(SDF**2))
    SD_val=SDF.std()
    return RMSE_val,SD_val,SDF