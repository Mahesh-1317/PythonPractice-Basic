class Star:
    def __init__(self,name, galaxy):
        self.name = name
        self.galaxy = galaxy

    # def __str__(self):
    #     return f"Name: {self.name}, Galaxy: {self.galaxy}"

obj = Star("Sun","Milky Way")
print(obj)