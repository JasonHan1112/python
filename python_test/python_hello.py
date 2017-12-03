#print test
test = "\"hello\"world"
hello_world = "hello world, this is my hello world";
print(hello_world);
print(test);

#title upper lower
print(hello_world.title());
print(hello_world.upper());
print(hello_world.lower());
print(hello_world);

#combine strings + 
hello_python = "hello python, this is my hello world";
print(hello_world+"*\n*"+hello_python);

#rstrip lstrip strip
test_rstrip = "    hello, how are you   ";
print(test_rstrip.rstrip());

test_lstrip = "    hello, how are you    ";
print(test_lstrip.lstrip());

test_strip = "   hello, how are you   ";
print(test_strip.strip());

#test int float
a = 1 + 2;
b = 2 + 3;
print(a + b);
a = 0.1 * 4;
b = 0.2 * 5;
print("a = %f" %(a));
print(a + b);

#test str
a = 3 * 2;
print(a);
print("hello"+str(a)+"?");

#test list
bicycles = ["trek", "cannondale", "redline", "specialized"];
print(bicycles);
print(bicycles[0]);

print("str" + bicycles[1].upper());

#change list
print(bicycles);
bicycles[1] = "giant";
print(bicycles);

#append insert
bicycles.append("merida");
print(bicycles);
bicycles.insert(3, "phonix");
print(bicycles);

#del pop remove
del(bicycles[0]);
print(bicycles);
test = bicycles.pop(3);
print("pop element" + "\"" + test + "\"");
print("pop element \"%s\"" %(test));
print(bicycles);

bicycles.remove("redline");
print (bicycles);

#sort sorted
bicycles.sort(reverse = True);#change the original element
print(bicycles);
print(sorted(bicycles));
print(bicycles);

bicycles.reverse();
print(bicycles);

print("len of bicycles = %d" %len(bicycles));

#iterate the list
for bicycle in bicycles:
    print(bicycle);
    print("this is my favorite");
print("end");

sum = 0;
digit = [];
for i in range(0, 10, 1):
    sum += i;
    digit.insert(i,i);
    print("i = %d" %i);
print("sum = %d" %sum);
print(digit);

print("min = %d" %min(digit));
print("max = %d" %max(digit));

#abbreviation of for assignment
abb_assignment = [value**2 for value in digit];
print("abb_assignment:");
print(abb_assignment);

#section
print("section:");
print(abb_assignment[0:3]);
print(abb_assignment[-3:]);

#iterate section
section = abb_assignment[0:3];
for sec in section:
    print(sec);

#it's not copy section
copy = abb_assignment;'''like pointer operate copy is like operate abb_assigment'''
for c in copy:
    print(c);
copy.pop(0);
print(abb_assignment);

#copy section must with section
copy = abb_assignment[:];
for c in copy:
    print(c);
copy.pop(0);
print(copy);
print(abb_assignment);

#tuple
dimensions = (0, 100, 200);
for dimension in dimensions:
    print(dimension);

#try to change tuple: error
#dimensions[0] = 300;

#change tuple
dimensions = (0, 1, 2);
print(dimensions);

#if statement
cars = ["audi", "bmw", "subaru", "toyota"];
for car in cars:
    if(car == "toyota"):
        print("fuck japan!!!"+" toyota");
    else:
        print(car.title());
car = "Audi";
print(car == "AUDI");

a = 32;
print(a < 33);

b = 35;
c = 43;
print(c > b and b > a);

if("audi" in cars):
    print("audi in cars");

if("BMW" not in cars):
    print("BMW is not in cars");

'''
tmp = input("input a number:");
if(int(tmp) < 10):
    print("the number %d < 10" %int(tmp));
elif(int(tmp) > 10):
    print("the number %d > 10" %int(tmp));
else:
    print("the number %d == 10" %int(tmp));
'''

#if in list
test_l = [];

if test_l:#judge the list is empty or not
    print("test_l list is not empty");
    for i in range(0, 100):
        test_l.insert(i, i);
        print(test_l[i]);
else:
    print("test_l list is empty");

for i in test_l:
    if("30" in test_l):
        print("30 in test_l");

#dictionary
alien_0 = {"color": "green", "point": 5};
print(alien_0["color"]);
print(alien_0["point"]);

#add items
alien_0["age"] = 30;
alien_0["time"] = "11:25";
print(alien_0);

del alien_0["time"];
print(alien_0);

for alien in alien_0.items():
    print(alien);
alien_0["color"] = "yellow";
for key, value in alien_0.items():
    print("key: " + key + " ; value: "+ str(value));

for key in alien_0.keys():
    print(key);
for value in sorted(alien_0.keys()):
    print(value);

#dictionary nest (dictionay in list)
alien_1 = {"color": "green", "point": 10};
alien_p = [alien_0, alien_1];
print(alien_p);

alien_2 = {"color": "black", "point": 20};
alien_p.append(alien_2);
print(alien_p);


alien_0["alien_list"] = bicycles;
print(alien_0);

'''
#while & input
while_count = 0;
print("input 3 times, then continue");
while while_count < 3:
    tmp = input("count = ");
    print("you input a number: %d" %int(tmp));
    while_count += 1;

dic_alien_input = {};
print("input a dictionary 3 elements");
count = 0;
while count < 3:
    key = input("input a key: ");
    value = input("input a value:");
    dic_alien_input[key] = value;
    count += 1;

print("you input the dictionary is :");
print(dic_alien_input);
'''

#function
import python_module_test
python_module_test.hello_world("xueqing");
python_module_test.make_pizza("mushrooms", "green peppers", "extra cheese");

from python_module_test import make_pizza
make_pizza("this is a test for import function only");

#class
from class_test import Dog

dog = Dog("xueqing", 28);
print(dog.name.title());
print(dog.age);
dog.hello_name();
print(dog.hello);
print(Dog.hello);
print(dog.name);
dog2 = Dog("2", 30);
dog.hello = "how are you";
Dog.hello = "fuck"
print(Dog.hello);
print(dog.hello);
print(dog2.hello);

#matplotlib
from class_test_matplotlib import Matplotlib_test

test_matplotlib = Matplotlib_test();

'''#test easy plot and scatter
test_matplotlib.plot_self_list_y();

test_matplotlib.plot_self_list_xy();

test_matplotlib.plot_self_scatter();
'''
#test random walk
'''
test_matplotlib.random_walk_init(10000);
test_matplotlib.fill_walk();
'''

#test die
#test_matplotlib.test_pygal(1000);

#test requests
test_matplotlib.test_requests("https://www.baidu.com/");
print("after test requests");
    
    













