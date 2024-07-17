import math

def calculate_trigonometric_values(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    sine = math.sin(angle_radians)
    cosine = math.cos(angle_radians)
    tangent = math.tan(angle_radians)
    return sine, cosine, tangent

# Example usage
angle_degrees = 45
sine, cosine, tangent = calculate_trigonometric_values(angle_degrees)
print(f"For an angle of {angle_degrees} degrees:")
print(f"Sine: {sine}")
print(f"Cosine: {cosine}")
print(f"Tangent: {tangent}")
