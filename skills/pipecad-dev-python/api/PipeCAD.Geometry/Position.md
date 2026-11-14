---
title: PipeCAD.Geometry.Position Class
namespace: PipeCAD.Geometry
kind: Class
---

# PipeCAD.Geometry.Position Class

> Position in 3D space.

## Requirements

Namespace: PipeCAD.Geometry

Assembly: python/PipeCAD/Geometry.pyd

## Properties

### `X`

X coordinate of the position.

```py
pos = Position(1, 2, 3)
x = pos.X
```

### `Y`

Y coordinate of the position.

```py
pos = Position(1, 2, 3)
y = pos.Y
```

### `Z`

Z coordinate of the position.

```py
pos = Position(1, 2, 3)
Z = pos.Z
```

## Methods

### `Position()`

Construct (0, 0, 0) position.

```py
pos = Position()
```

### `Position(x, y, z)`

Construct (x, y, z) position.

```py
pos = Position(1, 2, 3)
```

### `Distance(pos)`

Calcuate distance between two position.

```py
pos1 = Position(1, 2, 3)
pos2 = Position(4, 5, 6)

dist = pos1.Distance(pos2)
```
