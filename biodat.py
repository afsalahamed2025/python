class  BioData:

    def bio(self,Name,Age,DOB,District,Qulification,SchoolName,CollegeName,Intersted,Skills,Shorttimegoal,Longtimegoal):
        print("Name",Name)
        print("Age",Age)
        print("DOB",DOB)
        print("District",District)
        print("Qulification",Qulification)
        print("SchoolName",SchoolName)
        print("CollegeName",CollegeName)
        print("Intersted",Intersted)
        print("Skills",Skills)
        print("Shorttimegoal",Shorttimegoal)
        print("Longtimegoal",Longtimegoal)

Name =input("Enter The Name:")
Age =input("Enter The Age:")
DOB =input("Enter The DOB:")
Qulification =input("Enter The Qulification:")
District =input("Enter The District:")
SchoolName =input("Enter The SchoolName:")
CollegeName =input("Enter The CollegeName:")
Intersted =input("Enter The Intersted:")
Skills =input("Enter The Skills:")
Shorttimegoal =input("Enter The Shorttimegoal:")
Longtimegoal =input("Enter The Longtimegoal:")

o = BioData()
o.bio(Name,Age,DOB,District,Qulification,SchoolName,CollegeName,Intersted,Skills,Shorttimegoal,Longtimegoal)