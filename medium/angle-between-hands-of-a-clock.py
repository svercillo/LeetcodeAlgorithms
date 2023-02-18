class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        hour = hour % 12
        hour_angle = hour * 360 / 12 + minutes / 60 *  360 / 12
        min_angle = minutes * 360 / 60
        print(hour_angle, min_angle)

        if min_angle >= hour_angle:
            return min(min_angle - hour_angle, 360 - min_angle  + hour_angle)
        else:
            return min(hour_angle - min_angle, 360 - hour_angle + min_angle)
