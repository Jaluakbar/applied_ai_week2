def nand_gate(i1, i2):
    #print("NAND Gate Input : ", i1,i2)
    if (i1 * 0.5 + i2 * 0.5) == 1:
        #print("Output : False")
        return False
    else:
        #print("Output : True")
        return True

def nand_adder(x1, x2):
    a = nand_gate(x1,x2)
    b = nand_gate(x1, a)
    c = nand_gate(a, x2)
    d = nand_gate(b, c)
    e = nand_gate(a,a)

    #return carry bit, sum
    return (int(e), int(d))


# nand_gate(True,True)
# nand_gate(True,False)
# nand_gate(False,True)
# nand_gate(False,False)

print(nand_adder(0, 0))
print(nand_adder(0, 1))
print(nand_adder(1, 0))
print(nand_adder(1, 1))