class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

priyankasApplication = RailwayForm()
priyankasApplication.name = "Priyanka"
priyankasApplication.train = "Rajdhani Express"
priyankasApplication.printData()