
""" This remains static - but allows us to change the code without restarting Abaqus"""

def main(): 
    import Inp_Seperator_kernel
    reload(Inp_Seperator_kernel)
    print("Run Script")
    Inp_Seperator_kernel.main()