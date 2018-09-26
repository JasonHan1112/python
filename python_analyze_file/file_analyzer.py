#file name
in_file_name = "file.rdl";
out_file_name = "";
conf_file_name= "";
line_list = [];


#get words after key_word
def get_words_after(line, key_word):
    
    key_word_len = len(key_word);

    if(line.find(key_word) == -1):#can't find key_word
        return -1;

    start_pos = line.find(key_word) + key_word_len;
    val = line[start_pos : -1];

    #print(val);
    

    return val;





#get words between key_words (key1 xxx key2)
def get_words_between(line, key1, key2):
    key1_word_len = len(key1);
    
    if(line.find(key1) == -1):#can't find key_word
        return -1;

    start_pos = line.find(key1) + key1_word_len;#get pos after key1

    if(line[start_pos : -1].find(key2) == -1):#can't find key_word
        return -1;
    
    #get pos after key2(need plus offset)
    end_pos = line[start_pos : -1].find(key2) + start_pos;

    val = line[start_pos : end_pos];


    '''debug
    tmplist = [];
    tmplist.append(val);
    print(tmplist);
    '''
    return val
    



    
#analyzer words
def analyzer_words(words):
    nop();


'''
#analyzer rdl reg region
#reg_info_cur keep the current reg info (only one reg)
def analyzer_lines_reg_region(line, reg_keylist, reg_info_cur):

    #get reg_name
    val0 = get_words_between(line, reg_keylist[0], reg_keylist[1]);
    if(val0 != -1):
        reg_info_cur.append(val0);
    
    #get reg_offset
    val1 = get_words_after(line, reg_keylist[2]);
    if(val1 != -1):
        reg_info_cur.append(val1);
    
    #get reg_width
    val2 = get_words_after(line, reg_keylist[3]);
    if(val2 != -1):
        reg_info_cur.append(val2);
    

    return 0;
'''

#analyzer rdl get field attr in the same line with "field: "
#need refine
def analyzer_lines_get_field_attr(line, field_keylist, list_out):
    
    val0 = get_words_between(line, field_keylist[2], field_keylist[3])
    if(val0 != -1):
        if(val0.find("R") != -1):
            list_out.append("RO");
        else:
            list_out.append("RW");
    else:
        print("field attr error!!!");
        return -1;

    return 0;


#change field attr for "fixed at: "
def analyzer_lines_change_field_attr(line, field_keylist, list_out):

    val0 = get_words_after(line, "fixed at: ");
    if(val0 != -1):
        list_out.pop();
        list_out.append("RO")



#analyzer rdl get field size in the same line with "field: "
def analyzer_lines_get_field_size(line, field_keylist, list_out):
        
    val0 = line.find("[");
    val1 = line.find("]");
    if((val0 ==-1) or (val1 == -1)):
        print("field size error!!!");
        return -1;

    if(line.find("..") != -1):
        val_s = line[line.find("[")+1];
        val_e = line[line.find("]")-1];
        field_size = int(val_s) - int(val_e) + 1;
        #print(line);
    else:
        field_size = 1;

    list_out.append(field_size);
        
    return 0;


#analyzer rdl get field offset in the same line with "field: "
def analyzer_lines_get_filed_offset(line, field_keylist, list_out):
        
    val0 = line.find("[");
    val1 = line.find("]");
    if((val0 ==-1) or (val1 == -1)):
        print("field offset error!!!");
        return -1;

    val_offset = int(line[line.find("]") - 1]);
      
    list_out.append(val_offset);
      
#analyzer rdl get field data
def analyzer_lines_get_field_data(line, field_keylist, list_out):
    
    val0 = get_words_after(line, "fixed at: ");
    val1 = get_words_after(line, "reset ");

    if(val0 != -1):
        list_out.append(val0);
    if(val1 != -1):
        list_out.append(val1);
    if((val1 == -1) and (val0 == -1)):
        return -1;

    return 0;  


'''
#analyzer rdl field region
#need refine
def analyzer_lines_field_region(line, field_keylist, reg_cur_list, list_out):
    
    filed_line_num = 0;
    while (1):
        #get field_name
        val0 = get_words_between(line, field_keylist[0], field_keylist[1]);
        if(val0 != -1):
            list_out.append(reg_cur_list);#add a reg head
            list_out.append(val0);

            #get field_attr in the same line with "field :"
            #print(line);
            analyzer_lines_get_field_attr(line, field_keylist, list_out);
   
            #get field_size in the same line with "field :"
            analyzer_lines_get_field_size(line, field_keylist, list_out);

            #get field_offset in the same line with "field :"
            analyzer_lines_get_filed_offset(line, field_keylist, list_out);

            #get filed_data

    return;

'''
#analyzer rdl file lines 
def analyzer_lines_rdl(lines, list_out):

    field_flag = 0;
    reg_flag = 0;
    line_num = 0;
    sub_reg_info = [];
    reg_keylist = ["register :", " ", "map to:  :cfgdecp, at: ", "width "];
    field_keylist = ["field :", ",", "]", "do", "[", "]", "fixed at: "];
    
    for line in lines:
        
        if(reg_flag == 0):
            #get reg_name
            val0 = get_words_between(line, reg_keylist[0], reg_keylist[1]);
            if(val0 != -1):
                sub_reg_info.append(val0);
                reg_flag = 1;#get reg offset
                continue;
    
        if(reg_flag == 1):
            #get reg_offset
            val1 = get_words_after(line, reg_keylist[2]);
            if(val1 != -1):
                sub_reg_info.append(val1);
                reg_flag = 2;#get reg width
                continue;
        
        if(reg_flag == 2):
            #get reg_width
            val2 = get_words_after(line, reg_keylist[3]);
            if(val2 != -1):
                sub_reg_info.append(val2);
                reg_flag = 3;#get field name
                continue;
        
        if(reg_flag == 3):
            #get field_name
            val3 = get_words_between(line, field_keylist[0], field_keylist[1]);
            if(val3 != -1):
                list_out.append(sub_reg_info);
                list_out.append(val3);
                reg_flag = 4;#get field size ,filed_name in the same line
        
        if(reg_flag == 4):
            #get field size
            analyzer_lines_get_field_size(line, field_keylist, list_out);
            reg_flag = 5;#get field off in the same line

        if(reg_flag == 5):
            #get field offset
            analyzer_lines_get_filed_offset(line, field_keylist, list_out);
            reg_flag = 6;#get field attr on two lines


        if(reg_flag == 6):
            #get attr
            analyzer_lines_get_field_attr(line, field_keylist, list_out);
            reg_flag = 7;#change attr in the next

        if(reg_flag == 7):
            #change attr in the next lines
            analyzer_lines_change_field_attr(line, field_keylist, list_out);
            reg_flag = 8;#get field data
            continue;

        if(reg_flag == 8):
            #get data
            ret = analyzer_lines_get_field_data(line, field_keylist, list_out);
            if(ret != -1):#current line find field data

                reg_flag = 9;#find "end"
                continue;
            else:#find field data
                reg_flag = 8;#find field data
                continue;

        if(reg_flag == 9):
            if(line.find("end") != -1):
                reg_flag = 3;
                continue;
    return;



#read file
def read_file(file_name, tmpline_list):
    
    try:
        in_file = open(file_name, "r");
    except:
        print ("open file error");
        return -1;
    
    #if file right read file lines
    for line in in_file.readlines():
       tmpline_list.append(line);
    
    
    return 0;


#main flow
def analyzer():
    #initial analyzer
    line_list = [];
    list_out = [];
    print("analyzer...\n")
    
    if (read_file(in_file_name, line_list)):
        return -1;

    analyzer_lines_rdl(line_list, list_out);     
    
    #print(line_list);
    print(list_out);
    
    return 0;
    



#execute...
analyzer();
