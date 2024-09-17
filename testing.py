import re
i = open('test.txt', 'r').readlines()#the program
op = open('test2.txt', 'r').readlines()#the instuctions 
output = open('output.txt', 'w')
# these ^ are reading the three files
opcodee={}
optab = {}#da lel opcode of the instructions
l = []# da lel symbol table
m = []# da lel instructions
n = []# wa da lele refernce
a = []#da lel location counter
objectcode=[]#for object code
last3=[]
opcode = []
object_code = []
format1 = {"FIX", "FLOAT", "HIO", "NORM", "SIO", "TIO"}
format2 = {"ADDR", "CLEAR", "COMPR", "DIVR", "MULR",
           "RMO", 'SHIFTL', "SHIFTR", "SUBR", "SVC", "TIXR"}
format3 = {"ADD", "ADDF", "AND", "COMP", "COMPF", "DIV", "DIVF", "J", "JEQ", "JGT", "JLT", "JSUB", "LDA", "LDB", "LDCH",
           'LDF', "LDL", "LDS", "LDT", "LDX",
           "LPS", "MUL", "SSK", "STA", "STB", "STCH", "STF", "STI", "STL", "STS", "STSW", "STT", "STX", "SUB", "SUBF",
           "MULF", "OR", 'RD', "RSUB", "TD", "TIX", "WD"}
format4 = {"+ADD", "+ADDF", "+AND", "+COMP", "+COMPF", "+DIV", "+DIVF", "+J", "+JEQ", "+JGT", "+JLT", "+JSUB", "+LDA",
           "+LDB", "+LDCH", "+LDF", "+LDL", "+LDS", "+LDT", "+LDX",
           "+LPS", "+MUL", "+SSK", "+STA", "+STB", "+STCH", "+STF", "+STI", "+STL", "+STS", "+STSW", "+STT", "+STX",
           "+SUB", "+SUBF", "+MULF", "+OR", "+RD", "+RSUB", "+TD", "+TIX", "+WD"}

# these are the arrays/dictionaries  that i will be using
#==========================================================================================================================================================================================================================
#case1 this is the location counter of the program 

# getting the opcode of each instruction from the instruction file  
for line in op:
    op = line.split()
    optab.update({op[0]: op[1]})#the op[o]is for the name of the opcode #wa el op[1] is for the number presented

#this is for dividing the file into  3 lists(symbols list,instructions list ,references list )
for line in i:
    line = line.split()
    if len(line) == 3:
        l.append(line[0])  # da lel symbol table
        m.append(line[1])  # da lel instructions
        n.append(line[2])

    elif len(line) == 2:
        l.append('xxxx')
        m.append(line[0])  # da lel instructions
        n.append(line[1])  # wa da lele size of el 7aga
    elif len(line) == 1:
        l.append('xxxx')
        m.append(line[0])  # da lel instructions
        n.append('xxxx')

#this is the location counter process
count=1
for line in i:
    if 'START' in line:
        start = line.split()[2]
        x = int(start,16)
        
for  number in m:
            a.append(str(hex(x)[2:].zfill(4)))
            if number in format1:
                    x=x+1
                    count= count+1
            elif number in format2:
                    x=x+2
                    count=count+1
            elif number in format3 or number == 'WORD':
                t=n[count]
                
                if t.startswith('X'):
                    de = len(t[2:])-1
                    x = x + int(de/2)
                    count=count+1
                else:
                    
                    x=x+3
                    count=count+1
                    

            elif number in format4:
                x=x+4
                count=count+1
            elif number == 'BYTE':
                t=n[count+1]
                if t.startswith('X'):
                    de = len(t[2:])-1
                    x = x + int(de/2)
                    count=count+1
                else:
                    count=count+1
                    x = x + len(number)-1 
            elif number == 'RESW':
                count=count+1
                g=(int(n[count]))*3
                
                x=x+g
            
            elif number == 'RESB':
                count=count+1
                h=n[count]
                f = int(h,10)
                y=hex(f)
                z=hex(x)
                a7=type(y)
                sumo =  hex(int(z, 16) + int(y, 16))
                shii=hex(int(z, 16) + int(y, 16))
                x=int(sumo[2:],16)
            elif number=='END':
                x=x
         
#for x in range(len(a)):
        #output.write(str(a[x])+"\n")          

#output.write(str(a)+"\n")
         
#======================================================================================================================================================================
def address_form4(name,index,x):
    g=n[index]
    if x!=0:
        ra=hex(x)
        final=ra[2:].zfill(5)
        
        last3.append(final)
    for i in range(len(m)):
        if g != l[i] :
            i=i+1
        else:
            f=a[i].zfill(5) 
            #output.write(str(f)+"\n")
           
            last3.append(f)
#this is for flag bits of format 4
def n_i_X_b_p_e4(name,index):
    name1=n[index]
    if name.startswith('+'):
         match = re.search(r'\d+$', name1)
         if name1.startswith('#'):
            if match is not None:
                g=0
                i=1
                x=0
                a=0
                c=0
                b=1
                y=int(name1[1:])
                address_form4(name,index,y)
                
                nixbpe=str(g) + str(i) + str(x)+str(a) + str(c) + str(b)
                return nixbpe
         else:
            g=1
            i=1
            x=0
            a=0
            c=0
            b=1
            y=0
            address_form4(name,index,y)
            nixbpe=str(g) + str(i) + str(x)+str(a) + str(c) + str(b)
            #output.write("the format 4  "+str(nixbpe)+" "+name+" "+str(index+1)+" the el index"+"\n")
            return nixbpe
#to bring the target address and the  next pc counter
def find_loc(name,index):
    i=l[index]
    d=m[index]
    g=n[index]
   
    
   # output.write(str(name)+"\n")
    
    k=g[1:]
    ra=g[:1]
    re=g[:6]
    for i in range(len(m)):
        if g != l[i] and k!=l[i] and re!=l[i]:
            i=i+1
        elif d =='RSUB':
            return 0,0
            i=i+1    
        else:
            if ra=='#'and ra=='='and ra=='@':
                i=i+1
                return 0,0  
                
            #output.write("name "+str(l[i])+" location "+str(a[i])+ "\n")
            
            return a[i] ,a[index+1]
    #output.write(str(i)+" "+str(d)+str(g)+"\n")
   
        

    
def tohex(val, nbits):
      return hex((val + (1 << nbits)) % (1 << nbits))

def base_pc_relative(B,b,c,d):
    ta,f=find_loc(c,d)
    #output.write(str(ta)+"\n")
    if ta==0and f==0:
        last3.append('000')
        return B,b
    else:
        mon=hex(int(ta, 16) - int(f, 16))
        final=mon[2:].zfill(3)
        if '-' in mon:
            y=int(mon,16)
            if -2048 <= y <= 2047:
                
                v=tohex(y,32)
                final=v[7:]
                last3.append(final)
                B=0
                b=1
                return B,b
            else:
                 
                for i in range(len(m)):
                     if m[i]=='BASE':
                        base=n[i]
                        for i in range(len(m)):
                            if base==l[i]:
                                er=a[i]
                       
                        ta,f=find_loc(c,d)
                        f=er
                        mon=hex(int(ta, 16) - int(f, 16))
                        final=mon[2:].zfill(3)
                        last3.append(final)
                        B=1
                        b=0
                        return B,b
        else:
            last3.append(final)
            return B,b
            
            
        
            
            
            
     
   
    
    
#this is for the flag bits of format 3      
def n_i_X_b_p_e3(name,ondex):
    name1=n[ondex]
    if name1.startswith('T'):
        #output.write("format2"+"\n")
        no_objectcode()
    if name =='RSUB':
        g=1
        i=1
        x=0
        a=0
        c=0
        b=0
        a,c=base_pc_relative(a,c,name,ondex)
        nixbpe=str(g) + str(i) + str(x)+str(a) + str(c) + str(b)
                #output.write(str(nixbpe)+" "+name+" "+str(ondex+1)+" the el index"+"\n")
        return nixbpe
        
    if name1.startswith('#'):
        match = re.search(r'\d+$', name1)
        if match is not None:
                g=0
                i=1
                x=0
                a=0
                c=0
                b=0
                #output.write(str(name1)+"\n")
                y=name1[1:].zfill(3)
                
                last3.append(y)
                nixbpe=str(g) + str(i) + str(x)+str(a) + str(c) + str(b)
                return nixbpe
        else:
                g=0
                i=1
                x=0
                a=0
                c=1
                b=0
                #output.write(str(name1)+"\n")
                a,c=base_pc_relative(a,c,name,ondex)
                nixbpe=str(g) + str(i) + str(x)+str(a) + str(c) + str(b)
                #output.write(str(nixbpe)+" "+name+" "+str(ondex+1)+" the el index"+"\n")
                return nixbpe
    elif name1.startswith('@'):
                g=1
                i=0
                x=0
                a=0
                c=1
                b=0
                #output.write(str(name1)+"\n")
                a,c=base_pc_relative(a,c,name,ondex)
                nixbpe=str(g) + str(i) + str(x)+str(a) + str(c) + str(b)
                #output.write(str(nixbpe)+" "+name+" "+str(ondex+1)+" the el index"+"\n")
                return nixbpe
    elif name1.endswith(',X'):
                g=1
                i=1
                x=1
                a=1
                c=0
                b=0
                #output.write(str(name1)+"\n")
                a,c=base_pc_relative(a,c,name,ondex)
                nixbpe=str(g)  + str(i)  + str(x)+str(a) + str(c) + str(b)
                #output.write(str(nixbpe)+" "+name+" "+str(ondex+1)+" the el index"+"\n")
                return nixbpe
    
        
        
    else:
                g=1
                i=1
                x=0
                a=0
                c=1
                b=0
                #output.write(str(name1)+"\n")
                a,c=base_pc_relative(a,c,name,ondex)
                nixbpe=str(g) + str(i) + str(x)+str(a) + str(c) + str(b)
                #output.write(str(nixbpe)+" "+name+" "+str(ondex+1)+" the el index"+"\n")
                return nixbpe
    
        
    
    #output.write(str(nixbpe)+" "+name+"\n") 
#output.write(str(a)+str(b)+str(c)+str(name)+"\n")  




        



    
    


                           
def the_fist_number(i):
    
    x = [a for a in str(i)]
    a=x[0]
    
    return a       
def opcode_to_binary(opcodenumber):
    x = [a for a in str(opcodenumber)]
    a=x[0]
    b=x[1]
    
    
    for i in range(len(b)):
        if b >='0' and b < '9':
            z=bin(int(b))
            t=z[2:].zfill(4)
            final=t[:2]
            #output.write(" da el awl"+str(x)+"\n")
            #output.write(str(final)) 
            return final
            
        else:
            z=int(b,16)
            #output.write(str(x)+"\n")
            t=bin(z)
            final=t[2:4]
            #output.write(str(final))
            return final

def last_2_in_opcode(i):
            opcode_to_binary(i)
            first=opcode_to_binary(i)
            #output.write(str(first)+" ")
            return first
             
def objectcode_without_ta(h,l,m):
    p=l[:2]
    g=int(l[2:],2)
    if g>9:
        k=hex(g)
        g=k[2:]
    f=int(h+p,2)
    if f>9:
        t=hex(f)
        f=t[2:]
    a5ern=str(m)+str(f)+str(g)
    
    objectcode.append(a5ern)
    #output.write(str(a5ern) +"\n")
    
def byte_handle(inst,ref):
    if ref.startswith('X'):
        z=ref[2:-1]
        objectcode.append(' ')
        last3.append(z)
        
    elif ref.startswith('C'):
        z=ref[2:-1]
        k=ord(z[0])
        le=ord(z[1])
        m=ord(z[2])
        final =str(k)+str(le)+str(m)
        objectcode.append(' ')
        last3.append(final)
    #output.write(str(inst)+" "+str(ref) +"\n")
    
          
def no_objectcode():
    z=0
    #output.write("no object code" +"\n")   

base=0
for i in range(len(m)):
    if m[i] =='BASE':
        base=a[i]
        objectcode.append('no object')
        last3.append(' code')
    elif m[i] in format3:
        j=optab.get(m[i]) 
        kk=the_fist_number(j)#for the opcode
        az=last_2_in_opcode(j)#for the opcode
        ze=n_i_X_b_p_e3(m[i],i)#for flag bits
        
        objectcode_without_ta(az,ze,kk)
    elif m[i]in format4:
        j=optab.get(m[i]) 
        kk=the_fist_number(j)#for the opcode
        az=last_2_in_opcode(j)#for the opcode
        ze=n_i_X_b_p_e4(m[i],i)
        objectcode_without_ta(az,ze,kk)
    elif m[i]in format2:
        j=optab.get(m[i]) 
        if ','in n[i]:
            k=n[i]
            p=optab.get(k[2:3])
            c=optab.get(k[:1])
            g=str(c)+str(p)
            #output.write(str(g)+"\n")
            
            last3.append(g)
        k=optab.get(n[i])
        le=str(k).ljust(2,'0')
        
        if le == 'None':
            g=g
        else:
            last3.append(le)
        #output.write(str(le)+"\n")
        objectcode.append(j)
    elif m[i]=='START':
        objectcode.append('no object')
        last3.append(' code')
    elif m[i]=='BASE':
        objectcode.append('no object')
        last3.append(' code')
    elif m[i]=='RESW':
        objectcode.append('no object')
        last3.append(' code')
    elif m[i]=='RESB':
        objectcode.append('no object')
        last3.append(' code')
        
    elif m[i] =='BYTE':
       byte_handle(m[i],n[i])
           
the_final=[]    
for i in range(len(objectcode)):
    the_final.append((str(objectcode[i])+str(last3[i])))
    #output.write(str(objectcode[i])+str(last3[i])+"\n")
#output.write(str(the_final)+"\n")
#======================================================================================================================================================================
#======================================================================================================================================================================

for i in range (len(objectcode)):
    output.write(" "+str(a[i])+" "+str(l[i])+" "+str(m[i])+" "+str(n[i])+" "+str(the_final[i])+"\n")
#======================================================================================================================================================================

#hte
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  
no_ob=[]
output.write('H^' + l[0] + '^' + a[1] + '^' + a[len(a) - 1][2:]+'\n')    
cout=0
no_ob=the_final
no_ob.remove('no object code')
no_ob.remove('no object code')
no_ob.remove('no object code')
no_ob.remove('no object code')
no_ob.remove('no object code')




u=0
if 'BASE'in m:
    u=u+1
if 'START'in m:
    u=u+1
if 'END'in m:
    u=u+1
k=len(m)-u
if m[1:11] !='RESW':
        f=hex(30)
        j=len(m[1:11])
        for i in range(j):
            T = 't^' + a[0]+'^'+str(f[2:])+'^' +'^'.join(no_ob[0:i])
        output.write(str(T)+"\n")
while m[j+1] not in 'RESW':
    f=hex(12)
    T2 = 't^' + a[13]+'^'+str(f[2:])+'^' +'^'.join(no_ob[11:j])
    j=j+1
output.write(str(T2)+"\n")
while m[j]=='RESW':
    j=j+1
while m[j]=='RESB':
    j=j+1
while m[j] != 'RESW':
    f=hex(30)
    T3 = 't^' + a[20]+'^'+str(f[2:])+'^' +'^'.join(no_ob[j-1:j+9])
    j=j+1
output.write(str(T3)+"\n")
if m[25:35] !='RESW':
        f=hex(30)
        T4 = 't^' + a[30]+'^'+str(f[2:])+'^' +'^'.join(no_ob[25:35])
output.write(str(T4)+"\n")
if m[35:40] !='RESW':
        f=hex(15)
        T4 = 't^' + a[41]+'^'+str(f[2:])+'^' +'^'.join(no_ob[35:40])
output.write(str(T4)+"\n")
output.write('E^' + '00' + a[1]+'\n')

#======================================================================================================================================================
