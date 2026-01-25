import math
import sys

# default Coordinates

dest = (10, 20, 5)
point = (0, 0, 0)
pars_point = None


def calc_distance(point1, point2):
    """Calculate the 3D distance between two points (x, y, z)."""
    des = math.sqrt(((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2 +
                     (point2[2]-point1[2])**2))
    return des


def Unpacking(pars_point):
    """Show how to unpack 'x,y,z' into x, y, z variables."""
    print("\nUnpacking demonstration:")
    x, y, z = pars_point.split(',')
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: x={x}, y={y}, z={z}")


if __name__ == "__main__":
    """Run a small demo: parse coordinates,
    compute distance, and unpack them."""

    print("=== Game Coordinate System ===\n")
    print(f"Position created: {dest}")
    print(f"Distance between {point} and {dest}: "
          f"{calc_distance(point, dest):.2f}\n")

    if (len(sys.argv) > 1):
        pars_point = sys.argv[1]
    else:
        pars_point = "3, 4, 0"

    print(f'Parsing coordinates: "{pars_point}"')
    splited_pos = pars_point.split(',')
    dest_list = []
    try:
        for s in splited_pos:
            dest_list.append(int(s))
        dest = tuple(dest_list)
        print(f"Parsed position: {dest}")
        print(f"Distance between {point} and {dest}: "
              f"{calc_distance(point, dest):.2f}\n")
    except ValueError:
        print(f"oops!, you entered invalide value => {s}\n")
    dest = "abc,def,ghi"
    print(f"Parsing invalid coordinates: {dest}")
    splited_pos = dest.split(',')
    dest_list = []
    try:
        for s in splited_pos:
            dest_list.append(int(s))
    except ValueError:
        print(f"Error parsing coordinates: invalid literal for int() "
              f"with base 10: {splited_pos[0]}")
        print(f'Error details - Type: ValueError, Args: ("invalid literal '
              f'for int() with base 10: \'{splited_pos[0]}\'",)')

    Unpacking(pars_point)
