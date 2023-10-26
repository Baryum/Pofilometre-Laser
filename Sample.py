class  Sample():
    nextId = 0

    def __init__(self, name, ogPxValues):
        self.id = Sample.nextId
        Sample.nextId += 1
        self.name = name
        self.ogPxValues = ogPxValues
        self.filteredPxValues = []

    def __str__(self) -> str:
        return f"Sample {self.id} : \nname={self.name}\nogPxValues={self.ogPxValues is not None}\nfilteredPxValues={self.filteredPxValues is not None}"
    
    def __repr__(self) -> str:
        pass
