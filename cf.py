from PIL import Image

direction_map = ["north", "west", "south", "east"]

def read_pattern(file_path):
    pattern = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            pattern.append(list(line))
    return pattern

def rotate90_matrix(m):
    return [[m[i][j] for i in reversed(range(len(m)))] for j in range(len(m[0]))]

def mirror_matrix(m):
    return [list(reversed(row)) for row in m]

def determine_direction(input_matrix, output_matrix):
    current_matrix = input_matrix
    for i in range(4):
        if current_matrix == output_matrix:
            return direction_map[i], i
        current_matrix = rotate90_matrix(current_matrix)
    return None

def find_cloud_pattern(image_path, pattern, alpha_threshold=128):
    image = Image.open(image_path).convert("RGBA")
    width, height = image.size

    print(f"[INFO] Image size: {width}x{height}")
    patterns = []
    matches = [[], [], [], []]

    for o in range(4):
        if o != 0:
            pattern = rotate90_matrix(pattern)
        patterns.append(pattern)

        for y in range(height):
            for x in range(width):
                match = True
                for i in range(len(pattern)):
                    for j in range(len(pattern[i])):
                        pixel_x = (x + j) % width
                        pixel_y = (y + i) % height
                        _, _, _, a = image.getpixel((pixel_x, pixel_y))

                        is_cloud = a >= alpha_threshold
                        expected = pattern[i][j]

                        if expected != "?" and is_cloud != (expected == "1"):
                            match = False
                            break
                    if not match:
                        break
                if match:
                    matches[o].append((x, y))

    return patterns, matches

def get_valid_coords(spawn_range, pixel_z, fast):
    coords = []
    blocks = 8 if fast else 12
    grid_size = blocks * 256

    int_quotient = spawn_range // grid_size
    z_offset = (pixel_z * blocks)

    min_i = -int_quotient - 1
    if (grid_size * min_i) - 4 + z_offset < -spawn_range:
        min_i += 1

    max_i = int_quotient
    if (grid_size * max_i) - 4 + z_offset > spawn_range:
        max_i -= 1

    for i in range(min_i, max_i + 1):
        coords.append(grid_size * i - 4 + z_offset)
    return coords

def main():
    image_path = "clouds.png"  # Use your new converted image here
    pattern_path = "pattern.txt"
    from_bottom = False
    fast = False
    spawn_range = 10000

    print("[INFO] Looking for the pattern from the " + ("BOTTOM" if from_bottom else "TOP"))

    input_pattern = read_pattern(pattern_path)

    if from_bottom:
        input_pattern = mirror_matrix(input_pattern)

    output_patterns, matches = find_cloud_pattern(image_path, input_pattern)

    total_matches = sum(len(m) for m in matches)
    if total_matches == 0:
        print("[WARN] Pattern not found")
        return

    print(f"[INFO] Found {total_matches} match{'es' if total_matches > 1 else ''}\n")

    for orientation, matched_coords in enumerate(matches):
        for match in matched_coords:
            direction_info = determine_direction(input_pattern, output_patterns[orientation])
            if direction_info:
                input_direction, _ = direction_info
                print(f"[MATCH] Input was oriented towards {input_direction}, inserted from the {'BOTTOM' if from_bottom else 'TOP'}")
                print("         (Output is always oriented NORTH from the TOP)\n")
                print("Pattern:\n" + "\n".join("".join(row) for row in output_patterns[orientation]))
                print(f"Match at pixel: {match}")
                valid_z_coords = get_valid_coords(spawn_range, match[1], fast)
                print("Valid Z coords (spawn range ±{}):".format(spawn_range))
                for coord in valid_z_coords:
                    print(coord)
                print("\n")

if __name__ == "__main__":
    main()
