
class PicoBlazeAsmEncoder():
    def __init__(self):
        self.operation = {
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

        self.register = {
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

        self.__encoded_instruction_to_bin = ''

    def __ADD(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation[self.instruction[0]]
        if self.instruction[2].find('s') != -1:
            self.__encoded_instruction_to_bin += '1'
            self.__encoded_instruction_to_bin += self.register[self.instruction[1][:-1]]
            self.__encoded_instruction_to_bin += self.register[self.instruction[2]]
            self.__encoded_instruction_to_bin += '0000'
        else:
            self.__encoded_instruction_to_bin += '0'
            self.__encoded_instruction_to_bin += self.register[self.instruction[1][:-1]]
            self.__encoded_instruction_to_bin += ''.join(format(int(self.instruction[2]), 'b')).zfill(8)

    def __ADDCY(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation[self.instruction[0]]
        if self.instruction[2].find('s') != -1:
            self.__encoded_instruction_to_bin += '1'
            self.__encoded_instruction_to_bin += self.register[self.instruction[1][:-1]]
            self.__encoded_instruction_to_bin += self.register[self.instruction[2]]
            self.__encoded_instruction_to_bin += '0000'
        else:
            self.__encoded_instruction_to_bin += '0'
            self.__encoded_instruction_to_bin += self.register[self.instruction[1][:-1]]
            self.__encoded_instruction_to_bin += ''.join(format(int(self.instruction[2]), 'b')).zfill(8)

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
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation[self.instruction[0]]
        if self.instruction[2].find('s') != -1:
            self.__encoded_instruction_to_bin += '1'
            self.__encoded_instruction_to_bin += self.register[self.instruction[1][:-1]]
            self.__encoded_instruction_to_bin += self.register[self.instruction[2]]
            self.__encoded_instruction_to_bin += '0000'
        else:
            self.__encoded_instruction_to_bin += '0'
            self.__encoded_instruction_to_bin += self.register[self.instruction[1][:-1]]
            self.__encoded_instruction_to_bin += ''.join(format(int(self.instruction[2]), 'b')).zfill(8)

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
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation[self.instruction[0]]
        if self.instruction[2].find('s') != -1:
            self.__encoded_instruction_to_bin += '1'
            self.__encoded_instruction_to_bin += self.register[self.instruction[1][:-1]]
            self.__encoded_instruction_to_bin += self.register[self.instruction[2]]
            self.__encoded_instruction_to_bin += '0000'
        else:
            self.__encoded_instruction_to_bin += '0'
            self.__encoded_instruction_to_bin += self.register[self.instruction[1][:-1]]
            self.__encoded_instruction_to_bin += ''.join(format(int(self.instruction[2]), 'b')).zfill(8)

    def __SUBCY(self):
        pass

    def __TEST(self):
        pass

    def __XOR(self):
        pass

    def encode_instruction(self, instruction):
        self.instruction = instruction
        name_instruction = instruction.split()[0]
        if name_instruction == "ADD":
            self.__ADD()
        elif name_instruction == "ADDCY":
            self.__ADDCY()
        elif name_instruction == "AND":
            self.__AND()
        elif name_instruction == "CALL":
            flag = self.instruction[1]
            if flag == "C":
                self.__CALL_C()
            elif flag == "NC":
                self.__CALL_NC()
            elif flag == "Z":
                self.__CALL_Z()
            elif flag == "NZ":
                self.__CALL_NZ()
            else:
                self.__CALL()
        elif name_instruction == "COMPARE":
            self.__COMPARE()
        elif name_instruction == "DISABLE":
            self.__DISABLE_INTERRUPT()
        elif name_instruction == "ENABLE":
            self.__ENABLE_INTERRUPT()
        elif name_instruction == "FETCH":
            self.__FETCH()
        elif name_instruction == "INPUT":
            self.__INPUT()
        elif name_instruction == "JUMP":
            flag = self.instruction[1]
            if flag == "C":
                self.__JUMP_C()
            elif flag == "NC":
                self.__JUMP_NC()
            elif flag == "Z":
                self.__JUMP_Z()
            elif flag == "NZ":
                self.__JUMP_NZ()
            else:
                self.__JUMP()
        elif name_instruction == "LOAD":
            self.__LOAD()
        elif name_instruction == "OR":
            self.__OR()
        elif name_instruction == "OUTPUT":
            self.__OUTPUT()
        elif name_instruction == "RETURN":
            flag = self.instruction[1]
            if flag == "C":
                self.__RETURN_C()
            elif flag == "NC":
                self.__RETURN_NC()
            elif flag == "Z":
                self.__RETURN_Z()
            elif flag == "NZ":
                self.__RETURN_NZ()
            else:
                self.__RETURN()
        elif name_instruction == "RETURNI":
            if name_instruction == "DISABLE":
                self.__RETURNI_DISABLE()
            elif name_instruction == "ENABLE":
                self.__RETURNI_ENABLE()
        elif name_instruction == "RL":
            self.__RL()
        elif name_instruction == "RR":
            self.__RR()
        elif name_instruction == "SL0":
            self.__SL0()
        elif name_instruction == "SL1":
            self.__SL1()
        elif name_instruction == "SLA":
            self.__SLA()
        elif name_instruction == "SLX":
            self.__SLX()
        elif name_instruction == "SR0":
            self.__SR0()
        elif name_instruction == "SR1":
            self.__SR1()
        elif name_instruction == "SRA":
            self.__SRA()
        elif name_instruction == "SRX":
            self.__SRX()
        elif name_instruction == "STORE":
            self.__STORE()
        elif name_instruction == "SUB":
            self.__SUB()
        elif name_instruction == "SUBCY":
            self.__SUBCY()
        elif name_instruction == "TEST":
            self.__TEST()
        elif name_instruction == "XOR":
            self.__XOR()
        else:
            print "instruction unsupported"