class Dog():
    hello = "hello! this is single dog!!!"
    def __init__(self, name, age):
        #self.hello = "hello! this is single dog!!!";
        self.name = name;
        self.age = age;
    def hello_name(self):
        print(Dog.hello);
class Person():
    name = "aaa";

p1 = Person();
p2 = Person();
p3 = Person();

print(p1.name, id(p1.name));
print(p2.name, id(p2.name));
print(p3.name, id(p3.name));
print(Person.name, id(Person.name));


p1.name = "bbb";

print(p1.name, id(p1.name));
print(p2.name, id(p2.name));
print(p3.name, id(p3.name));
print(Person.name, id(Person.name));


Person.name = "ccc";

print(p1.name, id(p1.name));
print(p2.name, id(p2.name));
print(p3.name, id(p3.name));
print(Person.name, id(Person.name));


        