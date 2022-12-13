def courant(dx: float, dt: float, materials_summary):

    coeficient = lambda c, dx, dt: (c.square_velocity) ** (1 / 2) * (dt / dx)

    courant_material = [coeficient(m, dx, dt) for m in materials_summary]

    return courant_material
