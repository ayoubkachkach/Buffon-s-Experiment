import numpy as np
import math

MATCH_LEN = 1 #in pixels
LINE_SPACING = 2*MATCH_LEN #spacing between consecutive lines
DIM_SPACE = 240

class Point:
    '''Represents a 2D point'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates():
        return (x, y)

class Match:
    '''Represents a match with its center and angle (rad) of tilt'''
    def __init__(self, center, angle):
        self.center = center
        self.angle = angle
        
        #projection of center to side of the match w.r.t. x and y axes resp.
        self.hor_projection = (MATCH_LEN/2)*math.cos(angle)
        self.ver_projection = (MATCH_LEN/2)*math.sin(angle)
        
        #upper_point --> point with higher x-coordinate
        self.upper_point = Point(self.center + self.hor_projection,self.center + self.ver_projection)
        self.lower_point = Point(self.center - self.hor_projection, self.center - self.ver_projection) 
    
        self.touches = self.touches_line()

    def get_points(self):
        return (self.lower_point, self.upper_point)

    def touches_line(self):
        center_dist = self.center % LINE_SPACING
        
        return center_dist - self.ver_projection < 0 \
            or center_dist + self.ver_projection >= LINE_SPACING

    # @classmethod
    # def throw_match(self):


class Experiment:
    '''Represents an experiment with num_matches of matches each of which
    are of size match_len'''
    def __init__(self, num_matches):
        self.num_matches = num_matches
        self.matches = []
        self.touching_matches = 0 #no matches touching line initially

        self.throw_matches(num_matches)

    def throw_matches(self, num_matches):
        centers = np.random.uniform(0, DIM_SPACE - MATCH_LEN/2, num_matches)
        angles = np.random.uniform(0, math.pi, num_matches)
        self.matches = [Match(center, angle) for center, angle in zip(centers, angles)]
        self.touching_matches = sum(1 for match in self.matches if match.touches)
    

if(__name__ == "__main__"):
    num_matches = 90000
    print(sum([num_matches/Experiment(num_matches).touching_matches for i in range(10)])/10)

