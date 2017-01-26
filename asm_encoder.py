
class PicoBlazeAsmEncoder():
    operation = {
        "ADD": "01100",
        "ADDCY": "01101",
        "AND": "00101",
        "CALL": "11000",
        "COMPARE": "01010",
        "INTERRUPT": "11110",
        "FETCH": "00011",
        "INPUT": "00010",
        "JUMP": "11010",
        "LOAD": "00000",
        "OR": "00110",
        "OUTPUT": "10110",
        "RETURN": "10101",
        "RETURNI": "11100",
        "SHIFT": "10000",
        "STORE": "10111",
        "SUB": "01110",
        "SUBCY": "01111",
        "TEST": "01001",
        "XOR": "00111"
    }

    register = {
        "s0": "0000",
        "s1": "0001",
        "s2": "0010",
        "s3": "0011",
        "s4": "0100",
        "s5": "0101",
        "s6": "0110",
        "s7": "0111",
        "s8": "1000",
        "s9": "1001",
        "sA": "1010",
        "sB": "1011",
        "sC": "1100",
        "sD": "1101",
        "sE": "1110",
        "sF": "1111"
    }

    def __ADD(self):
        pass

    def __ADDCY(self):
        pass

    def __AND(self):
        pass

    def __CALL(self):
        pass

    def __CALL_C(self):
        pass

    def __CALL_NC(self):
        pass

    def __CALL_Z(self):
        pass

    def __CALL_NZ(self):
        pass

    def __COMPARE(self):
        pass

    def __DISABLE_INTERRUPT(self):
        pass

    def __ENABLE_INTERRUPT(self):
        pass

    def __FETCH(self):
        pass

    def __INPUT(self):
        pass

    def __JUMP(self):
        pass

    def __JUMP_C(self):
        pass

    def __JUMP_NC(self):
        pass

    def __JUMP_Z(self):
        pass

    def __JUMP_NZ(self):
        pass

    def __LOAD(self):
        pass

    def __OR(self):
        pass

    def __OUTPUT(self):
        pass

    def __RESET(self):
        pass

    def __RETURN(self):
        pass

    def __RETURN_C(self):
        pass

    def __RETURN_NC(self):
        pass

    def __RETURN_Z(self):
        pass

    def __RETURN_NZ(self):
        pass

    def __RETURNI_DISABLE(self):
        pass

    def __RETURNI_ENABLE(self):
        pass

    def __RL(self):
        pass

    def __RR(self):
        pass

    def __SL0(self):
        pass

    def __SL1(self):
        pass

    def __SLA(self):
        pass

    def __SLX(self):
        pass

    def __SR0(self):
        pass

    def __SR1(self):
        pass

    def __SRA(self):
        pass

    def __SRX(self):
        pass

    def __STORE(self):
        pass

    def __SUB(self):
        pass

    def __SUBCY(self):
        pass

    def __TEST(self):
        pass

    def __XOR(self):
        pass

