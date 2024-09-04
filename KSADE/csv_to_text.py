#-*-coding:utf-8-*-
import csv

def main(text_input):
    try:
        f = open(text_input, 'r')
    except IOError:
        return "Error"
    except TypeError:
        return "Error"
    
    else:
        pe2=open('PE2.txt','w')
        pe4=open('PE4.txt','w')
        pe6=open('PE6.txt','w')
        rdr = csv.reader(f)
        for line in rdr:
            try:
                s = line[0].split()[3]
            except IndexError:
                pass
            else:
                a=0
                pudata=''
                pudata+=(line[0].split()[0])+' '    
                try:
                    a=int(line[0].split()[2])
                except ValueError:
                    a=100
                if 0<a<8:
                    pudata+=(line[0].split()[2])+' '
                    for i in range(len(s)):
                        pudata+=(s[i])+' '
                    if line[0].split()[1]=='체육2':
                        pe2.write( pudata+'\n')
                    elif line[0].split()[1]=='체육4':
                        pe4.write( pudata+'\n')
                    elif line[0].split()[1]=='체육6':
                        pe6.write( pudata+'\n')
        f.close() 
        pe2.close()
        pe4.close()
        pe6.close()

        return ""
    
#main("abcd.txt")