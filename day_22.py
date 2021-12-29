class Cube:
    def __init__(self):
        self.x_int = [None, None]
        self.y_int = [None, None]
        self.z_int = [None, None]
        self.type = "on"

    def overlap(self, other: 'Cube'):
        """Determines the volume of the cross section.
        """
        # Initial checks of intervals
        if other.x_int[0] > self.x_int[1] or self.x_int[0] > other.x_int[1]:
            return None
        if other.y_int[0] > self.y_int[1] or self.y_int[0] > other.y_int[1]:
            return None
        if other.z_int[0] > self.z_int[1] or self.z_int[0] > other.z_int[1]:
            return None

        # Get the new intervals
        x_min = max(self.x_int[0], other.x_int[0])
        x_max = min(self.x_int[1], other.x_int[1])

        y_min = max(self.y_int[0], other.y_int[0])
        y_max = min(self.y_int[1], other.y_int[1])

        z_min = max(self.z_int[0], other.z_int[0])
        z_max = min(self.z_int[1], other.z_int[1])

        new_cube = Cube()
        new_cube.x_int = [x_min, x_max]
        new_cube.y_int = [y_min, y_max]
        new_cube.z_int = [z_min, z_max]
        return new_cube

    def volume(self):

        volume = (abs(self.x_int[1] - self.x_int[0]) + 1) * (abs(self.y_int[1] - self.y_int[0]) + 1) * (
                    abs(self.z_int[1] - self.z_int[0]) + 1)
        return volume


file = "input_22.txt"
volume_sum = 0
cubes = []
with open(file, 'r') as f:
    for line in f:
        sline = line.split()

        # Intervals
        ranges = sline[1].split(',')
        x_int = [int(_) for _ in ranges[0][2:].split("..")]
        y_int = [int(_) for _ in ranges[1][2:].split("..")]
        z_int = [int(_) for _ in ranges[2][2:].split("..")]

        el = Cube()
        el.x_int = x_int
        el.y_int = y_int
        el.z_int = z_int
        el.type = sline[0]
        cubes.append(el)

opposite = {"off": "on", "on": "off"}
cube = None
new_cube = None
other_cube = None


def part_one(part_one=True) -> int:
    processed = []
    for cube in cubes:
        # Filter out the -50 to 50 region
        if part_one:
            if cube.x_int[0] < -50:
                continue
            if cube.x_int[1] > 50:
                continue
            if cube.y_int[0] < -50:
                continue
            if cube.y_int[1] > 50:
                continue
            if cube.z_int[0] < -50:
                continue
            if cube.z_int[1] > 50:
                continue

        # Find all the cross sections
        new_cubes = []
        for other_cube in processed:
            new_cube = other_cube.overlap(cube)
            if new_cube:
                if other_cube.type == cube.type:
                    # Mark it as opposite cube
                    # Meaning if both cubes are on assign this as off and and
                    # vice verse if both cubes are off
                    new_cube.type = opposite[cube.type]
                else:
                    # Now assign the cube type depending on what what before
                    # and what is now
                    if other_cube.type == "on":
                        # Means that cube.type = off
                        new_cube.type = "off"
                    else:  # Means that we flip this region on
                        new_cube.type = "on"
                new_cubes.append(new_cube)

        # Append the cubes in order
        if cube.type == "on":
            processed.append(cube)
        processed += new_cubes

    # Now sum all the processed cubes
    c = 0
    for cube in processed:
        volume = cube.volume()
        if cube.type == "on":
            c += volume
        else:
            c -= volume

    return c


print("Part 1:", part_one())
print("Part 2:", part_one(part_one=False))