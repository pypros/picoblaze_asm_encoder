
class PicoBlazeAsmEncoder():
    def __init__(self):
        self.operation = {
            "ADD": "01100",
            "ADDCY": "01101",
            "AND": "00101",
            "CALL": "11000",
            "COMPARE": "01010",
            "FETCH": "00011",
            "INPUT": "00010",
            "JUMP": "11010",
            "LOAD": "00000",
            "OR": "00110",
            "OUTPUT": "10110",
            "RETURN": "10101",
            "RETURNI": "11100",
            "SHIFT": "10000",
            'RL': '0010',
            'RR': '1100',
            'SL0': '0110',
            'SL1': '0111',
            'SLA': '0000',
            'SLX': '0100',
            'SR0': '1110',
            'SR1': '1111',
            'SRA': '1000',
            'SRX': '1010',
            "STORE": "10111",
            "SUB": "01110",
            "SUBCY": "01111",
            "TEST": "01001",
            "XOR": "00111"
        }

        self.flag = {
            'None': '000',
            'C': '110',
            'NC': '111',
            'NZ': '101',
            'Z': '100'
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

    def __CALL(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation['CALL']
        self.__encoded_instruction_to_bin += self.flag['None']
        self.__encoded_instruction_to_bin += ''.join(format(int(self.instruction[1], 16), 'b')).zfill(10)


    def __CALL_C(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation['CALL']
        self.__encoded_instruction_to_bin += self.flag[self.instruction[1][:-1]]
        self.__encoded_instruction_to_bin += ''.join(format(int(self.instruction[2], 16), 'b')).zfill(10)

    def __CALL_NC(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation['CALL']
        self.__encoded_instruction_to_bin += self.flag[self.instruction[1][:-1]]
        self.__encoded_instruction_to_bin += ''.join(format(int(self.instruction[2], 16), 'b')).zfill(10)

    def __CALL_Z(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation['CALL']
        self.__encoded_instruction_to_bin += self.flag[self.instruction[1][:-1]]
        self.__encoded_instruction_to_bin += ''.join(format(int(self.instruction[2], 16), 'b')).zfill(10)

    def __CALL_NZ(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation['CALL']
        self.__encoded_instruction_to_bin += self.flag[self.instruction[1][:-1]]
        self.__encoded_instruction_to_bin += ''.join(format(int(self.instruction[2], 16), 'b')).zfill(10)

    def __COMPARE(self):
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

    def __DISABLE_INTERRUPT(self):
        self.__encoded_instruction_to_bin = "111100000000000000"

    def __ENABLE_INTERRUPT(self):
        self.__encoded_instruction_to_bin = "111100000000000001"

    def __FETCH(self):
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

    def __INPUT(self):
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

    def __JUMP(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation['JUMP']
        self.__encoded_instruction_to_bin += self.flag['None']
        self.__encoded_instruction_to_bin += ''.join(format(int(self.instruction[1], 16), 'b')).zfill(10)


    def __JUMP_C(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation['JUMP']
        self.__encoded_instruction_to_bin += self.flag[self.instruction[1][:-1]]
        self.__encoded_instruction_to_bin += ''.join(format(int(self.instruction[2], 16), 'b')).zfill(10)

    def __JUMP_NC(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation['JUMP']
        self.__encoded_instruction_to_bin += self.flag[self.instruction[1][:-1]]
        self.__encoded_instruction_to_bin += ''.join(format(int(self.instruction[2], 16), 'b')).zfill(10)

    def __JUMP_Z(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation['JUMP']
        self.__encoded_instruction_to_bin += self.flag[self.instruction[1][:-1]]
        self.__encoded_instruction_to_bin += ''.join(format(int(self.instruction[2], 16), 'b')).zfill(10)

    def __JUMP_NZ(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation['JUMP']
        self.__encoded_instruction_to_bin += self.flag[self.instruction[1][:-1]]
        self.__encoded_instruction_to_bin += ''.join(format(int(self.instruction[2], 16), 'b')).zfill(10)

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
        self.__encoded_instruction_to_bin = "111000000000000000"

    def __RETURNI_ENABLE(self):
        self.__encoded_instruction_to_bin = "111000000000000001"

    def __RL(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation['SHIFT']
        self.__encoded_instruction_to_bin += '0'
        self.__encoded_instruction_to_bin += self.register[self.instruction[1]]
        self.__encoded_instruction_to_bin += '0000'
        self.__encoded_instruction_to_bin += self.operation[self.instruction[0]]

    def __RR(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation['SHIFT']
        self.__encoded_instruction_to_bin += '0'
        self.__encoded_instruction_to_bin += self.register[self.instruction[1]]
        self.__encoded_instruction_to_bin += '0000'
        self.__encoded_instruction_to_bin += self.operation[self.instruction[0]]

    def __SL0(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation['SHIFT']
        self.__encoded_instruction_to_bin += '0'
        self.__encoded_instruction_to_bin += self.register[self.instruction[1]]
        self.__encoded_instruction_to_bin += '0000'
        self.__encoded_instruction_to_bin += self.operation[self.instruction[0]]

    def __SL1(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation['SHIFT']
        self.__encoded_instruction_to_bin += '0'
        self.__encoded_instruction_to_bin += self.register[self.instruction[1]]
        self.__encoded_instruction_to_bin += '0000'
        self.__encoded_instruction_to_bin += self.operation[self.instruction[0]]

    def __SLA(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation['SHIFT']
        self.__encoded_instruction_to_bin += '0'
        self.__encoded_instruction_to_bin += self.register[self.instruction[1]]
        self.__encoded_instruction_to_bin += '0000'
        self.__encoded_instruction_to_bin += self.operation[self.instruction[0]]

    def __SLX(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation['SHIFT']
        self.__encoded_instruction_to_bin += '0'
        self.__encoded_instruction_to_bin += self.register[self.instruction[1]]
        self.__encoded_instruction_to_bin += '0000'
        self.__encoded_instruction_to_bin += self.operation[self.instruction[0]]

    def __SR0(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation['SHIFT']
        self.__encoded_instruction_to_bin += '0'
        self.__encoded_instruction_to_bin += self.register[self.instruction[1]]
        self.__encoded_instruction_to_bin += '0000'
        self.__encoded_instruction_to_bin += self.operation[self.instruction[0]]

    def __SR1(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation['SHIFT']
        self.__encoded_instruction_to_bin += '0'
        self.__encoded_instruction_to_bin += self.register[self.instruction[1]]
        self.__encoded_instruction_to_bin += '0000'
        self.__encoded_instruction_to_bin += self.operation[self.instruction[0]]

    def __SRA(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation['SHIFT']
        self.__encoded_instruction_to_bin += '0'
        self.__encoded_instruction_to_bin += self.register[self.instruction[1]]
        self.__encoded_instruction_to_bin += '0000'
        self.__encoded_instruction_to_bin += self.operation[self.instruction[0]]

    def __SRX(self):
        self.__encoded_instruction_to_bin = ""
        self.instruction = self.instruction.split()
        self.__encoded_instruction_to_bin += self.operation['SHIFT']
        self.__encoded_instruction_to_bin += '0'
        self.__encoded_instruction_to_bin += self.register[self.instruction[1]]
        self.__encoded_instruction_to_bin += '0000'
        self.__encoded_instruction_to_bin += self.operation[self.instruction[0]]

    def __STORE(self):
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

    def __TEST(self):
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

    def __XOR(self):
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

    def encode_instruction(self, instruction):
        self.instruction = instruction
        name_instruction = instruction.split()[0]
        second_name_instruction = instruction.split()[1]
        if name_instruction == "ADD":
            self.__ADD()
        elif name_instruction == "ADDCY":
            self.__ADDCY()
        elif name_instruction == "AND":
            self.__AND()
        elif name_instruction == "CALL":
            flag = instruction.split()[1][:-1]
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
            flag = instruction.split()[1][:-1]
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
            if second_name_instruction == "DISABLE":
                self.__RETURNI_DISABLE()
            elif second_name_instruction == "ENABLE":
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