"""
Vector Calculus Toolkit — Week 1
================================

First computational exercise for PHYS 2124 Mathematical Methods I.
Topics: Vector operations, dot product, cross product, gradient, divergence, curl.

Author: Saba Yip
Date: 2026-06-07
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

print("=" * 60)
print("Vector Calculus Toolkit — Week 1")
print("=" * 60)

# === 1. Basic Vector Operations ===
print("\n=== 1. Basic Vector Operations ===\n")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(f"a = {a}")
print(f"b = {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"3a = {3*a}")

# === 2. Dot Product ===
print("\n=== 2. Dot Product ===\n")
dot_ab = np.dot(a, b)
print(f"a · b = {dot_ab}")

# === 3. Cross Product ===
print("\n=== 3. Cross Product ===\n")
cross_ab = np.cross(a, b)
print(f"a × b = {cross_ab}")

# === 4. Vector Visualization ===
print("\n=== 4. Vector Visualization ===\n")

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

origin = [0, 0, 0]
ax.quiver(*origin, *a, color='r', label='a', arrow_length_ratio=0.1)
ax.quiver(*origin, *b, color='b', label='b', arrow_length_ratio=0.1)
ax.quiver(*origin, *cross_ab, color='g', label='a×b', arrow_length_ratio=0.1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([-1, 6])
ax.set_ylim([-1, 6])
ax.set_zlim([-1, 6])
ax.legend()
ax.set_title('Vectors a, b, and a×b')

plt.tight_layout()
plt.savefig('vector_visualization.png', dpi=100, bbox_inches='tight')
print("✅ Saved: vector_visualization.png")

# === 5. Practice Problems (MIT OCW 18.02) ===
print("\n=== 5. Practice Problems ===\n")
print("Problem 1: Find the angle between a and b.")
angle = np.arccos(dot_ab / (np.linalg.norm(a) * np.linalg.norm(b)))
print(f"  Answer: θ = {np.degrees(angle):.2f}°")

print("\nProblem 2: Find a unit vector perpendicular to both a and b.")
unit_cross = cross_ab / np.linalg.norm(cross_ab)
print(f"  Answer: {unit_cross}")

print("\nProblem 3: Area of parallelogram spanned by a and b.")
area = np.linalg.norm(cross_ab)
print(f"  Answer: {area:.4f}")

print("\n=== Week 1 Complete! ===")
print("Next: Gradient, divergence, curl")
