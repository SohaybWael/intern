#1- Representation of Rectangles: 
    #a) Each rectangle is represented by the coordinates of two opposing vertices, where [[x1, y1], [x2, y2]].
    #b) The first point [x1, y1] is the bottom-left corner of the rectangle.
    #c) The second point [x2, y2] is the top-right corner of the rectangle.
#2- Orientation of Rectangles:
    #a) The rectangles have two sides parallel to the X-axis and the other two sides parallel to the Y-axis. This means they are aligned with the coordinate axes.
#3- Intersection of Rectangles Conditions:
    #a) For two rectangles to intersect, there must be a common surface area between them that is greater than zero. In other words, they must overlap in both the X and Y dimensions.
    #b) However, if two rectangles are merely adjacent and touching side-to-side, with no overlapping area, they are NOT considered intersecting.
#4- Adjacent vs. Intersecting:
    #a) Being adjacent means the rectangles share a common boundary but do not overlap. This scenario is not considered as intersecting because the shared surface area is zero.


def intersectingRectangles(rect1, rect2):
    if rect1[0][0] >= rect2[1][0] or rect1[1][0] <= rect2[0][0] or rect1[0][1] >= rect2[1][1] or rect1[1][1] <= rect2[0][1]:
        return False
    else:
        return True
    
rect1 = [[2,2],[6,7]]
rect2 = [[1,10],[7,13]]

print(intersectingRectangles(rect1, rect2))



