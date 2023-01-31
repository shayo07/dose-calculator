from dataclasses import fields
from mysqlx import Row
from prettytable import from_csv
import array as arr



with open("alltogather1.csv", "r") as fp:
    x = from_csv(fp)
print(x)
with open("TSF.csv", "r") as fp:
    k = from_csv(fp)
print(k)
with open("combined TAR1.csv", "r") as fp:
    y = from_csv(fp)
print(y)
with open("CSF.csv", "r") as fp:
    z = from_csv(fp)
print(z)
mydic = {
    3:0,
    4:1,
    5:2,
    6:3,
    8:4,
    9:5,
    10:6,
    12:7,
    15:8,
    20:9,
    25:10,
    30:11,
    35:12,
    40:13,

}

mydic1 = {
    0.5:0, 1:1, 1.5:2 ,2:3, 2.5:4, 3:5, 3.5:6, 4:7, 4.5:8, 5:9, 5.5:10, 6:11, 6.5:12, 7:13,
    7.5:14, 8:15, 8.5:16 ,9:17, 9.5:18, 10:19, 10.5:20, 11:21, 11.5:22, 12:23, 12.5:24, 13:25, 13.5:26, 14:27,
    14.5:28, 15:29, 15.5:30 ,16:31, 16.5:32, 17:33, 17.5:34, 18:35, 18.5:36, 19:37, 19.5:38, 20:39, 20.5:40, 21:41,
    21.5:42, 22:43,22.5:44 ,23:45, 23.5:46, 24:47, 24.5:48, 25:49, 25.5:50, 26:51, 26.5:52, 27:53, 27.5:54, 28:55,
    28.5:56, 29:57, 29.5:58 ,30:59,
}

pname= input("Enter the patient's name: ")
ddose= float(input("Enter Daily Dose in cGy: "))
depth= input("Enter Depth in Cm: ")
dim1= input("Enter first dimension of field size in Cm: ")
dim2= input("Enter second dimension of field size in Cm: ")


sum_of_dims = float(dim1)+float(dim2)
product = 2 * float(dim1) * float(dim2)
equivalentfs= product / float(sum_of_dims)
efs = float(equivalentfs)
efs0 = int(efs)
efs1 =str(efs0)

def printTT(tt1, tt):
                if technique == 2:
                    
                        print("treatment time for patient: ", pname, " is: ", tt," minutes")
                        print("AP-0 degree: ", round(tt1/2,2)," minutes")
                        print("PA-180 degree: ", round(tt1/2,2)," minutes")
                elif technique == 4:
                    
                        print("treatment time for patient: ", pname, " is: ", tt," minutes")
                        print("AP-0 degree: ", round(tt1/4,2)," minutes")
                        print("PA-180 degree: ", round(tt1/4,2)," minutes")
                        print("LT-LAT-90 degree: ", round(tt1/4,2)," minutes")
                        print("RT-LAT-270 degree: ", round(tt1/4,2)," minutes")
                else:
                        print("You have entered wrong technique")
                        print("Please re-run the program and choose wisely")



print("Equivalent field size is: ",efs)

choice= input("write 1 for SSD or 2 for SAD Mode: ")
if choice=="1":
  
  print("You are working in SSD mode")
  doserate = float(input("Enter Dose Rate in cGy/min: "))
  depth1 = float(depth)
  


  def mychoice1():
      print("nimefika")
      esfarr = arr.array('i', [4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 25, 30, 35, 40])
      for p in esfarr:
         if (p == efs):
                row = k[mydic[efs]]
                row.header = False
                row.border = False
                tsf = row.get_string(fields= ["TOTAL SCATTER"]).strip("\"")
                tsf = float(tsf)
                print(tsf)


                row = x[mydic1[depth1]]
                row.header= False
                row.border = False
                pdd = row.get_string(fields= [efs1]).strip("\"")
                pdd = float(pdd)/100
                print(pdd)
                tt = (ddose)/(pdd*tsf*doserate)
                tt1 = round(tt,2)
                print("treatment time for patient: ", pname, " is: ", tt1, "minutes")
                break   
         
  esfarr = arr.array('i', [4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 25, 30, 35, 40])

  for i in esfarr: 
            if (i == efs):
                mychoice1()
                break
            elif (i== esfarr[13] and efs0 != esfarr[13] ):
                print("nipo ndani")
                for d in esfarr:
                    if esfarr[d] > efs0 :
                       print("chochote")
                        

                       a =str(esfarr[d])
                       b =str(esfarr[d-1])
                       b1=float(b)
                       a1= float(a)


                       row = x[mydic1[depth1]]
                       row.header= False
                       row.border = False
                       pdd1 = row.get_string(fields= [a]).strip("\"")
                       pdd1 = float(pdd1)
                       print("pdd1", pdd1)

                       row = x[mydic1[depth1]]
                       row.header= False
                       row.border = False
                       pdd2 = row.get_string(fields= [b]).strip("\"")
                       pdd2 = float(pdd2)
                       print("pdd2",pdd2)

                       y = (pdd2 + (efs - b1)*(pdd1-pdd2)/(a1-b1))/100 
                       print("this is my resultant pdd: ",y)
                       break
                tsfarr1 = arr.array('i', [3, 4, 5, 6, 8, 9, 10, 12, 15, 20, 25, 30, 35, 40])
                
                for x in tsfarr1:
                    
                    if x > efs0 :
                
                        

                       s =str(x)
                       o = tsfarr1.index(x)

                       t =str(tsfarr1[o-1])
                       t1=float(t)
                       s1= float(s)
                       print(s)
                       print(t)


                       row = k[mydic[s1]]
                       row.header = False
                       row.border = False
                       tsf1 = row.get_string(fields= ["TOTAL SCATTER"]).strip("\"")
                       tsf1 = float(tsf1)
                       print(tsf1)

                       row = k[mydic[t1]]
                       row.header = False
                       row.border = False
                       tsf2 = row.get_string(fields= ["TOTAL SCATTER"]).strip("\"")
                       tsf2 = float(tsf2)
                       print(tsf2)

                       u = (tsf2 + (efs - s1)*(tsf1-tsf2)/(t1-s1)) 
                       print("this is my resultant tsf: ",u)  
                       break  
                tt = (ddose)/(y*u*doserate)
                tt1 = round(tt,2)
                print("treatment time for patient: ", pname, " is: ", tt1, "minutes")
                
              
            

           






elif choice=="2":
  print("You are working in SAD mode")
  doserate = float(input("Enter Dose Rate in cGy/min: "))
  technique= int(input("enter 2 for two sides or 4 for 4 box technique: "))
  depth1 = float(depth)
  


  def mychoice2():
      print("nimefika")
      esfarr1 = arr.array('i', [4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 25, 30, 35, 40])
      for p in esfarr1:
         if (p == efs):
                row = z[mydic[efs]]
                row.header = False
                row.border = False
                csf = row.get_string(fields= ["COLLIMATOR SCATTER"]).strip("\"")
                csf = float(csf)
                print(csf)


                row = y[mydic1[depth1]]
                row.header= False
                row.border = False
                tar = row.get_string(fields= [efs1]).strip("\"")
                tar = float(tar)
                print(tar)
                tt1 = (ddose)/(tar*csf*doserate)
                tt = round(tt1,2)
                printTT(tt1,tt)
                break   
         
  esfarr1 = arr.array('i', [4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 25, 30, 35, 40])

  
  for i in esfarr1: 
            if (i == efs):
                mychoice2()
                break
            elif (i== esfarr1[13] and efs0 != esfarr1[13] ):
                print("nipo ndani")
                for d in esfarr1:
                    if esfarr1[d] > efs0 :
                       print("chochote")
                        

                       a0 =str(esfarr1[d])
                       b0 =str(esfarr1[d-1])
                       b2=float(b0)
                       a2= float(a0)


                       row = y[mydic1[depth1]]
                       row.header= False
                       row.border = False
                       tar1 = row.get_string(fields= [a0]).strip("\"")
                       tar1 = float(tar1)
                       print("tar1", tar1)

                       row = y[mydic1[depth1]]
                       row.header= False
                       row.border = False
                       tar2 = row.get_string(fields= [b0]).strip("\"")
                       tar2 = float(tar2)
                       print("tar2",tar2)

                       ry = (tar2 + (efs - b2)*(tar1-tar2)/(a2-b2)) 
                       print("this is my resultant tar: ",ry)
                       break
                tsfarr1 = arr.array('i', [3, 4, 5, 6, 8, 9, 10, 12, 15, 20, 25, 30, 35, 40])
                
                for x in tsfarr1:
                    
                    if x > efs0 :
                
                        

                       s =str(x)
                       o = tsfarr1.index(x)

                       t =str(tsfarr1[o-1])
                       t1=float(t)
                       s1= float(s)
                       print(s)
                       print(t)


                       row = z[mydic[s1]]
                       row.header = False
                       row.border = False
                       csf1 = row.get_string(fields= ["COLLIMATOR SCATTER"]).strip("\"")
                       csf1 = float(csf1)
                       print(csf1)

                       row = z[mydic[t1]]
                       row.header = False
                       row.border = False
                       csf2 = row.get_string(fields= ["COLLIMATOR SCATTER"]).strip("\"")
                       csf2 = float(csf2)
                       print(csf2)

                       ru = (csf2 + (efs - s1)*(csf1-csf2)/(t1-s1)) 
                       print("this is my resultant csf: ",ru)  
                       tt1 = (ddose)/(ry*ru*doserate)
                       tt= round(tt1,2)
                       printTT(tt1,tt)
                       break  
                


else:
    print("You have entered wrong choice")
    print("Please re-run the program and choose wisely")
