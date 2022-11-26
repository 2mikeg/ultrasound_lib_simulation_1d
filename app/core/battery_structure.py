from typing import List


def battery_structure(geometric_unit: List[int], layers_number: int):

    """
    Battery structure method allow to create the battery geometric.

    Params:
    geometric_unit: list of the composition wrappred
    layers_number: number of layers to create the geometry
    """

    _geometric_unit = int(geometric_unit / 2)

    battery_map = []

    unit_count = 0
    geometry_count = 0

    for _ in range(layers_number):

        battery_map.append(geometric_unit[unit_count])
        unit_count = unit_count + 1
        geometry_count = geometry_count + 1

        if unit_count == len(geometric_unit):
            unit_count = 0

        if geometry_count == (layers_number / 2) + 1:
            unit_count = len(geometric_unit) - 1
            for _ in range(_geometric_unit):
                battery_map.append(geometric_unit[unit_count])
                unit_count = unit_count - 1

                if unit_count < 0:
                    unit_count = len(geometric_unit) - 1

            break

    return battery_map
