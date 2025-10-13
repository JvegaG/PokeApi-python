class pokemon:
    def __init__(
        self,
        id: int,
        name: str,
        base_experience: int,
        locationarea_encounters: str,
        weight: int,
        height: int,
    ):
        self.id = id
        self.name = name
        self.base_experience = base_experience
        self.locationarea_encounters = locationarea_encounters
        self.weight = weight
        self.height = height
