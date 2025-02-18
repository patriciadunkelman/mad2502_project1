import numpy as np

def get_barycentric_coordinates(triangle_coordinates: np.array, point_coordinates: np.array) -> np.array:
     X1, X2, X3 = triangle_coordinates[0]
     Y1, Y2, Y3 = triangle_coordinates[1]
     PX, PY = point_coordinates
     area = (1/2)*((X1*(Y2-Y3))+(X2*(Y3-Y1))+(X3*(Y1-Y2)))
     bary_area_1 = (1/2)*((PX*(Y2-Y3))+(X2*(Y3-PY))+(X3*(PY-Y2)))
     bary1 =bary_area_1/area
     bary_area_2 = (1/2)*((X1*(PY-Y3))+(PX*(Y3-Y1))+(X3*(Y1-PY)))
     bary2 =bary_area_2/area
     bary_area_3 = (1/2)*((X1*(Y2-PY))+(X2*(PY-Y1))+(PX*(Y1-Y2)))
     bary3 =bary_area_3/area
     bary_coords = np.array([bary1, bary2, bary3])

     return bary_coords
    

def get_cartesian_coordinates(triangle_coordinates: np.array, barycentric_coordinates: np.array) -> np.array:
     X1, X2, X3 = triangle_coordinates[0]
     Y1, Y2, Y3 = triangle_coordinates[1]
     B1, B2, B3 = barycentric_coordinates
     x = (X1*B1) + (X2*B2) + (X3*B3) 
     y = (Y1*B1) + (Y2*B2) + (Y3*B3) 
     point_coords = np.array([x,y])
     return point_coords


def is_inside_triangle(triangle_coordinates: np.array, point_coordinates: np.array) -> bool:
     X1, X2, X3 = triangle_coordinates[0]
     Y1, Y2, Y3 = triangle_coordinates[1]
     PX, PY = point_coordinates
     area = (1/2)*((X1*(Y2-Y3))+(X2*(Y3-Y1))+(X3*(Y1-Y2)))
     bary_area_1 = (1/2)*((PX*(Y2-Y3))+(X2*(Y3-PY))+(X3*(PY-Y2)))
     bary1 =bary_area_1/area
     bary_area_2 = (1/2)*((X1*(PY-Y3))+(PX*(Y3-Y1))+(X3*(Y1-PY)))
     bary2 =bary_area_2/area
     bary_area_3 = (1/2)*((X1*(Y2-PY))+(X2*(PY-Y1))+(PX*(Y1-Y2)))
     bary3 =bary_area_3/area
     if (0 <= bary1 <= 1) and (0 <= bary2 <= 1) and (0 <= bary3 <= 1):
          return True
     return False