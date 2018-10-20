class Udacian:

    def __init__(self, name, city, enrollment, nanodegree, status):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nanodegree = nanodegree
        self.status = status

    def print_udacian(self):
        return  self.name + "is in " + self.city + "and he/she is " + self.enrollment[0]

u = Udacian('Ibrahim', 'Riyadh', ('Saturday', 'am', 'Lujain'), 'FSDND','on track')

print(u.print_udacian())
