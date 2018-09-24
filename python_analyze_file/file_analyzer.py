#file name
in_file_name = "file.rdl";
out_file_name = "";
conf_file_name= "";
line_list = [];


#get words after key_word
def get_words_after(line, key_word):
    
    key_word_len = len(key_word);

    if(line.find(key_word) == -1):#can't find key_word
        return 1;

    start_pos = line.find(key_word) + key_word_len;
    val = line[start_pos : -1];

    print(val);
    

    return val;





#get words between key_words (key1 xxx key2)
def get_words_between(line, key1, key2):
    key1_word_len = len(key1);
    
    if(line.find(key1) == -1):#can't find key_word
        return 1;

    start_pos = line.find(key1) + key1_word_len;#get pos after key1

    if(line[start_pos : -1].find(key2) == -1):#can't find key_word
        return 1;
    
    #get pos after key2(need plus offset)
    end_pos = line[start_pos : -1].find(key2) + start_pos;

    val = line[start_pos : end_pos];
    
    tmplist = [];
    tmplist.append(val);
    print(tmplist);

    return val
    



    
#analyzer words
def analyzer_words(words):
    nop();


#analyzer line
def analyzer_lines(line):
    nop();


#analyzer lines 
def analyzer_lines(lines):
    nop();



#read file
def read_file(file_name, tmpline_list):
    
    try:
        in_file = open(file_name, "r");
    except:
        print ("open file error");
        return 1;
    
    #if file right read file lines
    for line in in_file.readlines():
       tmpline_list.append(line);
    
    
    return 0;


#main flow
def analyzer():
    line_list = [];
    print("analyzer...\n")
    
    if (read_file(in_file_name, line_list)):
        return 1;
    for line in line_list:
        #get_words_after(line, "width ");
        get_words_between(line, "register :", " ");
    print(line_list);
    
    return 0;
    



#execute...
analyzer();
