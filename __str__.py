class a:
    def __init__(self,name,year):
        self.name = name
        self.year = year
    def __str__(self):
        return "name:%s year:%s"%(self.name,self.year)

def main():
    b = a("xiaoming",20);
    print(b);

main()
