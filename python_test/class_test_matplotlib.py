import matplotlib.pyplot as plt
from random import choice
import pygal
import requests
import json


class Matplotlib_test():
    
    def __init__(self):
        self.list_x_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
        self.list_y_test = [1, 4, 9, 16, 25, 36, 49, 64, 81 ,100];
        print("this is a matplotlib test");
        print("this is also a random walk");
    
    def plot_self_list_y(self):#test matplotlib red
        plt.plot(self.list_y_test, linewidth = 3, c = "red");
        plt.title("test only_list_y");
        plt.xlabel("auto");
        plt.ylabel("list_y_value");
        plt.show();
    
    def plot_self_list_xy(self):#test matplotlib blue
        plt.plot(self.list_x_test, self.list_y_test, linewidth = 3, c = "Blue");
        plt.title("test list_x_y");
        plt.xlabel("list_x_value");
        plt.ylabel("list_y_value");
        plt.axis([0, 20, 0, 120]);
        plt.show();

    def plot_self_scatter(self):#test scatter
        plt.scatter(self.list_x_test, self.list_y_test, s=50, cmap = plt.cm.Blues, c = self.list_y_test, edgecolor = "none");
        plt.title("test scatter");
        plt.xlabel("x_list");
        plt.ylabel("y_list");
        plt.axis([0, 20, 0, 120]);
        plt.savefig("scatter_test.png", bbox_inches = "tight");
        plt.show();

    def random_walk_init(self, num_points = 100):
        self.num_points = num_points;

        #start position
        self.x_values = [0];
        self.y_values = [0];
        
    def fill_walk(self):
        
        while(len(self.x_values) < self.num_points):
            x_direction = choice([1, -1]);
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8]);
            xstep = x_direction * x_distance;

            y_direction = choice([1, -1]);
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8]);
            ystep = y_direction * y_distance;

            if(xstep == 0 and ystep == 0):
                continue;

            next_step_x = self.x_values[-1] + xstep;
            next_step_y = self.y_values[-1] + ystep;
            
            self.x_values.append(next_step_x);
            self.y_values.append(next_step_y);
            
            
        #show paint
        plt.scatter(next_step_x, next_step_y, s=15,  edgecolor = "none");#c = self.x_values, 
        plt.scatter(self.x_values, self.y_values, cmap = plt.cm.Reds, c = self.x_values, s=15);
        plt.savefig("random walk.png");
        plt.show();
    
    def test_pygal(self, count):
        list_roll = [];
        freq = [];
        die_list = [1, 2, 3, 4, 5, 6];
        
        #create data
        while(len(list_roll) <= count):
            value = choice(die_list);
            list_roll.append(value);
        print("list_roll:");
        
        #statistic fre
        for value in sorted(die_list):
            freq.append(list_roll.count(value));
            print("value = %d" %value);
        print("freq:");
        print(freq);

        pg = pygal.Bar();
        pg.title = "Die freq";
        pg.x_title = "die numbers";
        pg.y_title = "freq";
        pg.add("D6",freq);
        
        pg.render_to_file("die_freq_statistic.svg");
    def test_requests(self,url):
        r = requests.get(url);
        print("status code :", r.status_code);
        print("r.text:",r.content);
'''
        response_dict = r.json();
        
        print("response_dict:");
        print(response_dict);
'''

