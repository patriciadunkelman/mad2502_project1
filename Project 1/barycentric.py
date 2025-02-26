import numpy as np

#   calculates the barycentric coords of a point in a triangle
def get_barycentric_coordinates(triangle_coordinates: np.array, point_coordinates: np.array) -> np.array:
    """
    This function calculates the barycentric coordinates of a point in a triangle.
    
    They are calculated using the formula for the area of a triangle (1/2) * x1*(y1-y3) + x2(y3-y1 +x3*( y1-y2))).
    The formula for the area is known as the shoelace formula
    next the barycentric points are found by dividing by area of the point and two vertices with the total triangle area.
    
     Parameters
    ----------
    triangle_coordinates : np.array
    	The coordinates of the triangle. Its a 2x3 array where each column represents a vertex.
     point_coordinates : np.array 
    	The coordinates of the point.
    
    Returns
    --------
    np.array
        The barycentric coordinates of the point
    """
    
    # X1, X2, X3 are the x coordinates of the vertices of the triangle
    X1, X2, X3 = triangle_coordinates[0]
    
    # Y1, Y2, Y3 are the y coordinates of each of the vertices of the triangle
    Y1, Y2, Y3 = triangle_coordinates[1]
    
    # PX is the x-coordinate of the point
    PX, PY = point_coordinates
    
    # the previous lines unpacked the parameters into variables
    
    # calculating the area of the triangle using the shoelace formula
    # ithe formula adds up up the products of the x coordinates and the next y coordinates
    # then subtracting the products of the y coordinates and the next x coordinates
    area = (1/2)*((X1*(Y2-Y3))+(X2*(Y3-Y1))+(X3*(Y1-Y2)))
    
    # calculate the barycentric coordinates
    #the barycentric coordinates are found by dividing the area of the triangle with the 
    # point and two vertices of the triangle by the total area of the triangle
    bary_area_1 = (1/2)*((PX*(Y2-Y3))+(X2*(Y3-PY))+(X3*(PY-Y2)))
    bary1 = bary_area_1/area
    
    bary_area_2 = (1/2)*((X1*(PY-Y3))+(PX*(Y3-Y1))+(X3*(Y1-PY)))
    bary2 = bary_area_2/area
    
    bary_area_3 = (1/2)*((X1*(Y2-PY))+(X2*(PY-Y1))+(PX*(Y1-Y2)))
    bary3 = bary_area_3/area
    
    # returns the barycentric coordinates as a numpy array
    bary_coords = np.array([bary1, bary2, bary3])
    return bary_coords


# this function calculates the cartesian coords of a point from its barycentric coords
def get_cartesian_coordinates(triangle_coordinates: np.array, barycentric_coordinates: np.array) -> np.array:
    """
    This function calculates the cartesian coordinates of a point from its barycentric coordinates.
    
    They are calculated using the formula x = X1*B1 + X2*B2 + X3*B3 and y = Y1*B1 + Y2*B2 + Y3*B3
    
    Parameters
    ----------
    triangle_coordinates : np.array
    	The coordinates of the triangle. Its a 2x3 array where each column represents 
    	a vertex.
     barycentric_coordinates : np.array 
    	The barycentric coordinates of the point.
    
    Returns
    --------
    np.array
        The cartesian coordinates of the point
    """
    
    # X1, X2, X3 are the x coordinates of the vertices of the triangle
    X1, X2, X3 = triangle_coordinates[0]
    
    # Y1, Y2, Y3 are the y coordinates of each of the vertices of the triangle
    Y1, Y2, Y3 = triangle_coordinates[1]
    
    # B1, B2, B3 are the barycentric coordinates of the point
    B1, B2, B3 = barycentric_coordinates
    
    # calculating the cartesian coordinates using the formula
    x = (X1*B1) + (X2*B2) + (X3*B3)
    y = (Y1*B1) + (Y2*B2) + (Y3*B3)
    
    # returns the cartesian coordinates as a numpy array
    point_coords = np.array([x, y])
    return point_coords


# this function checks if a point is inside a triangle
def is_inside_triangle(triangle_coordinates: np.array, point_coordinates: np.array) -> bool:
    """
    This function checks if a point is inside a triangle.
    
    The point is inside the triangle if the barycentric coordinates are between 0 and 1
    
    Parameters
    ----------
    triangle_coordinates : np.array
    	The coordinates of the triangle. It is a 2x3 array where each column represents 
    	a vertex.
    point_coordinates : np.array 
    	The coordinates of the point.
    
    Returns
    --------
     bool
        True if the point is inside the triangle, False if not
    """
    
    # X1, X2, X3 are the x coordinates of the vertices of the triangle
    X1, X2, X3 = triangle_coordinates[0]
    
    # Y1, Y2, Y3 are the y coordinates of each of the vertices of the triangle
    Y1, Y2, Y3 = triangle_coordinates[1]
    
    # PX is the x-coordinate of the point
    PX, PY = point_coordinates
    
    # calculating the area of the triangle using the shoelace formula
    area = (1/2)*((X1*(Y2-Y3))+(X2*(Y3-Y1))+(X3*(Y1-Y2)))
    
    # calculate the barycentric coordinates
    bary_area_1 = (1/2)*((PX*(Y2-Y3))+(X2*(Y3-PY))+(X3*(PY-Y2)))
    bary1 = bary_area_1/area
    
    bary_area_2 = (1/2)*((X1*(PY-Y3))+(PX*(Y3-Y1))+(X3*(Y1-PY)))
    bary2 = bary_area_2/area
    
    bary_area_3 = (1/2)*((X1*(Y2-PY))+(X2*(PY-Y1))+(PX*(Y1-Y2)))
    bary3 = bary_area_3/area
    
    # the point is inside the triangle if the barycentric coordinates are between 0 and 1
    if (0 <= bary1 <= 1) and (0 <= bary2 <= 1) and (0 <= bary3 <= 1):
        return True
    return False
