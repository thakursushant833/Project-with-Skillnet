class school:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        return sum / 3

d=school("Sushant",[60,80,77])
average=round(d.avg(),2)
print(f"name {d.name}, Average is {average}")