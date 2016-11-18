import sys

def get_variables(variable_file,map_variables,in_file,out_file):
    variable_map={}
    f=open(map_variables,'r')
    line=f.readline()
    while line:
        line=line.replace('\n','')
        split=line.split('\t')
        index=int(split[0])
        reason=split[1].lower()
        variable_map[reason]=index
        line=f.readline()
    f.close()
    
    index_set=set()
    f=open(variable_file,'r')
    line=f.readline()
    while line:
        line=line.replace('\n','')
        reason=line
        index_set.add(variable_map[reason.lower()])
        line=f.readline()
    
    fw=open(out_file,'w')
    f=open(in_file,'r')
    line=f.readline()
    while line:
        line=line.replace('\n','')
        split=line.split(',')
        op_str=""
        for i in range(len(split)):
            if i in index_set:
                op_str=op_str+","+str(split[i])
        op_str=op_str[1:len(op_str)]
        fw.write(op_str+'\n')
        line=f.readline()
    f.close()
    fw.close()


variable_file=sys.argv[1]
map_variables='./MAP_Variables.txt'
in_file='./ALL_Years_data.csv'
out_file=sys.argv[2]
get_variables(variable_file,map_variables,in_file,out_file)