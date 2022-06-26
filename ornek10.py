equ = int(input("Gir: "))
SS = 0
MM = 0
HH = 0

if equ < 60:
    SS = equ
    if SS < 10:
        print("00:00:0{}".format(SS))
    else:
        print("00:00:{}".format(SS))
elif equ < 3600:
    SS = equ % 60
    MM = equ // 60
    if SS < 10:
        if MM < 10:
            print("00:0{}:0{}".format(MM,SS))
        else:
            print("00:{}:0{}".format(MM,SS))
    else:
        if MM < 10:
            print("00:0{}:{}".format(MM,SS))
        else:
            print("00:{}:{}".format(MM,SS))
else:
    SS = equ % 60
    HH = equ // 3600
    MM = (equ // 60) - (HH*60)
    if SS < 10:
        if MM < 10:
            if HH < 10:
                print("0{}:0{}:0{}".format(HH,MM,SS))
            else:
                print("{}:0{}:0{}".format(HH,MM,SS))
        else:
            if HH < 10:
                print("0{}:{}:0{}".format(HH,MM,SS))
            else:
                print("{}:{}:0{}".format(HH,MM,SS)) 
    else:
        if MM < 10:
            if HH < 10:
                print("0{}:0{}:{}".format(HH,MM,SS))
            else:
                print("{}:0{}:{}".format(HH,MM,SS))
        else:
            if HH < 10:
                print("0{}:{}:{}".format(HH,MM,SS))
            else:
                print("{}:{}:{}".format(HH,MM,SS))
        

    
