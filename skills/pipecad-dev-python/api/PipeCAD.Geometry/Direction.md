---
title: PipeCAD.Geometry.Direction Class
namespace: PipeCAD.Geometry
kind: Class
---

# PipeCAD.Geometry.Direction Class

> Unit vector in 3D space.

## Requirements

Namespace: PipeCAD.Geometry

Assembly: python/PipeCAD/Geometry.pyd

## Properties

### `X`

X component of the direction.

```py
dir = Direction(1, 0, 0)
x = dir.X
```

### `Y`

Y component of the direction.

```py
dir = Direction(1, 0, 0)
y = dir.Y
```

### `Z`

Z component of the direction.

```py
dir = Direction(1, 0, 0)
z = dir.Z
```

## Methods

### `Direction()`

Construct (0, 0, 1) direction.

```py
dir = Direction()
```

### `Direction(x, y, z)`

Construct (x, y, z) direction.

```py
dir = Direction(1, 2, 3)
```

### `IsParallel(dir)`

Return Ture if two direction is parallel.

```py
dir1 = Direction(1, 2, 3)
dir2 = Direction(4, 5, 6)

dir1.IsParallel(dir2)
```
