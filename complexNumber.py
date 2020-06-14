R1=int(input("Real Part 1:"))
I1=int(input("Imaginary Part 1:"))
R2=int(input("Real Part 2:"))
I2=int(input("Imaginary Part 2:"))
choice=int(input("1.Addition\n2.Subraction\n3.Multiplication\n4.Division\n5.Inverse\nENTER YOUR CHOICE:"))
def add_sub(r1,r2,i1,i2):
    real=r1+r2
    img=i1+i2
    print("{}+{}j".format(real,img))
def mul(r1,r2,i1,i2):
    real=r1*r2
    img=i1*i2
    print("{}+{}j".format(real, img))
def div(r1,r2,i1,i2):
    real=( (r1*r2)+(i1*i2) ) / ( (r2**2)+(i2**2) )
    img=( (r2*i1)-(r1*i2) ) / ( (r2**2)+(i2**2) )
    if(img<0):
        print("{}{}j".format(real, img))
    else:
        print("{}+{}j".format(real, img))

if(choice==1):
    add_sub(R1,R2,I1,I2)
elif(choice==2):
    add_sub(R1,-R2,I1,-I2)
elif(choice==3):
    mul(R1,R2,I1,I2)
elif(choice==4):
    div(R1,R2,I1,I2)
elif(choice==5):
    inv=int(input("you want to find the inverse of which complex number , 1 or 2 :"))
    if(inv==1):
        div(1,R1,0,I1)
    elif(inv==2):
        div(1,R2,0,I2)
    else:
        print("Invalid choice")
else:
    print("Invalid choice")

