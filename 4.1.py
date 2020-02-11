def and_gate(i1, i2):
    if (((int(i1) * 0.5) + (int(i2) * 0.5)) == 1):
        return True
    else:
        return False

def nor_gate(i1, i2, i3):
    print("NOR GATE Input : ", i1,i2,i3)
    if (i1 + i2 + i3) <= 0:
        print("Output : True")
        return True
    else:
        print("Output : False")
        return False
        
nor_gate(True, True, True)
nor_gate(True, False, False )
nor_gate(False, False, False)

