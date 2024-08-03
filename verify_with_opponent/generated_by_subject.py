def max_points_on_a_line(points):
    n = len(points)
    if n <= 2:
        return n

    def count_slope(i):
        same_point = 1
        slope_map = {}
        for j in range(n):
            if i == j:
                continue
            x_diff, y_diff = points[j][0] - points[i][0], points[j][1] - points[i][1]
            if x_diff == 0:
                slope = float('inf')
            else:
                slope = y_diff / x_diff
            slope_map[slope] = slope_map.get(slope, 0) + 1
        return max(slope_map.values(), default=0) + same_point

    max_count = 0
    for i in range(n):
        max_count = max(max_count, count_slope(i))
    return max_count