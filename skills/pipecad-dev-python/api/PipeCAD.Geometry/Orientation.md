---
title: PipeCAD.Geometry.Orientation Class
namespace: PipeCAD.Geometry
kind: Class
---

# PipeCAD.Geometry.Orientation Class

> Coordinate System.

## Requirements

Namespace: PipeCAD.Geometry

Assembly: python/PipeCAD/Geometry.pyd

## Properties


## Methods

### `Orientation(Direction dx, Direction dy)`

Construct coordinate system by two direction.

```py
dir1 = Direction(1, 0, 0)
dir2 = Direction(0, 1, 0)

ori = Orientation(dx, dy)
```

### `XDirection()`

Return X direction.

```py
dir1 = Direction(1, 0, 0)
dir2 = Direction(0, 1, 0)

ori = Orientation(dx, dy)
dx = ori.XDirection()
```

### `YDirection()`

Return Y direction.

```py
dir1 = Direction(1, 0, 0)
dir2 = Direction(0, 1, 0)

ori = Orientation(dx, dy)
dy = ori.YDirection()
```
