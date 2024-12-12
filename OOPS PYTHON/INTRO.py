class person:
    name="Shikher"
    work="Python developer"
    company="Inovation And You"
    def info(self):
        print(f"{self.name} is a {self.work} in {self.company}")

a=person()

# print(a)
# print(a.name)
a.name="Sonu"
# print(a.name)
# print(person)
# print(person)
# print(a.info())

b=person()

print(a.name)
print(b.name)
a.info()
b.info()