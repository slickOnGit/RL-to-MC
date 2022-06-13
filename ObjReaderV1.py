from tokenize import String


class OBJ:
    # Reads obj file as text document and organizes the contents
    # into self.vertices, self.textures, and self.faces
    
    def __init__(self, path):
        file = open(path)
        data = []
        num = 0
        for line in file:
            data.append(line)
            num += 1


        self.vertices = []
        self.textures = []
        self.faces = []
        # Each line can start with one of these
        # or a '#' to mean comment, or other random stuff
        possible_starts = ['v', 'vp', 'vn', 'vt', 'f', 'l']
        for line in data:
            # remove new lines at end of lines
            if '\n' in line:
                line = line[:-1]
            # convert to list
            nums = line.split(" ")
            # some lines are empty just for formatting
            if len(nums) <= 1:
                continue
            # character(s) at the beginning of the line tell us 
            # what the line is
            data_type = nums[0]
            # vertex (v x y z)
            if data_type == 'v':
                coords = [float(i) for i in nums[1:]]
                self.vertices.append(coords)
            # texture (maps material to self.vertices, I think)
            # (vt u v w), v and w are optional
            elif data_type == 'vt':
                texture = [float(i) for i in nums[1:]]
                self.textures.append(texture)
            # face (f v1/vt1 v2/vt2 v3/vt3)
            # can have more than 3, vts are optional and can include
            # vn, which is a normal vector
            elif data_type == 'f':
                points = nums[1:]
                # this splits up each point in the face into the vertex
                # and the vertex texture
                for i in range(len(points)):
                    p = points[i]
                    info = p.split("/")
                    points[i] = [int(i) for i in info]
                self.faces.append(points)

        # Now we have the three lists. The material of the self.faces, 
        # which has color, transparency, shininess, secondary color, etc
        # is in the material.lib file which has a similar formatting
        # but I gtg so I don't have time to parse it.

        """
        xmax = max([v[0] for v in self.vertices])
        xmin = min([v[0] for v in self.vertices])
        ymax = max([v[1] for v in self.vertices])
        ymin = min([v[1] for v in self.vertices])
        zmax = max([v[2] for v in self.vertices])
        zmin = min([v[2] for v in self.vertices])



        print("self.vertices: ", len(self.vertices))
        print("self.textures: ", len(self.textures))
        print("self.faces: ", len(self.faces))
        print("X range: ", xmin, "-", xmax)
        print("Y range: ", ymin, "-", ymax)
        print("Z range: ", zmin, "-", zmax)
        """
        file.close()
        
    def getVertices(self):
        return self.vertices
    
    def getTextures(self):
        return self.textures
    
    def getFaces(self):
        return self.faces