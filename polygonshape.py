import pygame

# Base class for game objects
class PolygonShape(pygame.sprite.Sprite):
    def __init__(self, x, y, number_sides):
        # grabs container init
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.number_sides = randint(6, 13)
    
    def polygon_angle_calc(self, n):
        INTERIOR_ANGLE_SUM = 180 * (n-2)
        angles = []
        for i in range(1, n):
            angle = randrange(90, 180)
            angles.append(angle)
        last_angle = INTERIOR_ANGLE_SUM - sum(angles)
        angles.append(last_angle)
        while angles[n-1] > 180:
            angles = self.recalculate_angles(angles, n)
        return angles

        
    def recalculate_angles(self, angles, n):
        INTERIOR_ANGLE_SUM = 180 * (n-2)
        for i in range(1, n):
            angle = randrange(90, 180)
            angles[i-1] = angle
        angles[n-1] = INTERIOR_ANGLE_SUM - sum(angles)
        return angles

    def polygon(self, n):
        if n < 3:
            raise ValueError("polygons must have at least 3 sides")
# calculate angle ratio with points on line method (find n-1 points from 0 to 1 and take the difference between them)
        ratio_points = []
        ratios = []
        for i in range(1, n):
            point = randrange(0, 1)
            ratio_points.add(point)
        previous_point = 0
        for point in ratio_points:
            ratio = point - previous_point
            ratios.add(ratio)
            previous_point = point
        ratio = 1 - previous_point
        ratios.add(ratio)
# alternate
        INTERIOR_ANGLE_SUM = (n-2) * 180
        points = []
        angles = []
        starting_angle = 0
        for i in range(1, n):
            angle = randrange(90, 180)
# see errors if they exist
        if sum(ratios) != 1:
            print("ratios are wrong")
            for ratio in ratios:
                print(ratio)
        if len(ratios) != n:
            print("number of sides is wrong")
            print(f"there are {len(ratios)} sides listed instead of {n} sides")
# convert angle ratio to interior_angles
        INTERIOR_ANGLE_SUM = (n-2) * 180
        interior_angles = [ratio * INTERIOR_ANGLE_SUM for ratio in ratios]
# get points around position
        if self.velocity == pygame.Vector2(0,0):
            starting_vector = pygame.Vector2(1, 0)
        else:
            starting_vector = self.velocity
        for angle in angles:
            starting_vector.rotate(180 - angle)


    def polygon(self):

#    def collides_with(self, other):
#        if pygame.Vector2.distance_to(self.position, other.position) < self.radius + other.radius:
#            return True
#        else:
#            return False
        
    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass
