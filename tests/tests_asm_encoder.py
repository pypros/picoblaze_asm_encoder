from asm_encoder import PicoBlazeAsmEncoder

def test_encode_operation_ADD_sx_kk():
    line_of_code = "ADD s0, 127"
    #         "011000xxxxkkkkkkkk"
    binary_instruction_expected = "011000000001111111"  # ADD s0, kk
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin

def test_encode_operation_ADD_sx_sy():
    line_of_code = "ADD s0, sF"
    #         "011001xxxxyyyy0000"
    binary_instruction_expected = "011001000011110000"  # ADD s0, sF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin

def test_encode_operation_ADDCY_sx_kk():
    line_of_code = "ADDCY s0, 127"
    #         "011010xxxxkkkkkkkk"
    binary_instruction_expected = "011010000001111111"  # ADDCY s0, kk
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin

def test_encode_operation_ADDCY_sx_sy():
    line_of_code = "ADDCY s0, sF"
    #         "011011xxxxyyyy0000"
    binary_instruction_expected = "011011000011110000"  # ADDCY s0, sF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin

def test_encode_operation_AND_sx_kk():
    line_of_code = "AND s0, 127"
    #         "001010xxxxkkkkkkkk"
    binary_instruction_expected = "001010000001111111"  # AND s0, kk
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin

def test_encode_operation_AND_sx_sy():
    line_of_code = "AND s0, sF"
    #         "001011xxxxyyyy0000"
    binary_instruction_expected = "001011000011110000"  # AND s0, sF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_COMPARE_sx_kk():
    line_of_code = "COMPARE s0, 127"
    #         "010100xxxxkkkkkkkk"
    binary_instruction_expected = "010100000001111111"  # COMPARE s0, kk
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin

def test_encode_operation_COMPARE_sx_sy():
    line_of_code = "COMPARE s0, sF"
    #         "010101xxxxyyyy0000"
    binary_instruction_expected = "010101000011110000"  # COMPARE s0, sF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


# def test_encode_operation_COMPARE():
#     pass


def test_encode_operation_INTERRUPT():
    pass
def test_encode_operation_FETCH():
    pass
def test_encode_operation_INPUT():
    pass
def test_encode_operation_JUMP():
    pass
def test_encode_operation_LOAD():
    pass


def test_encode_operation_OR_sx_kk():
    line_of_code = "OR s0, 127"
    #         "001100xxxxkkkkkkkk"
    binary_instruction_expected = "001100000001111111"  # OR s0, kk
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_OR_sx_sy():
    line_of_code = "OR s0, sF"
    #         "001101xxxxyyyy0000"
    binary_instruction_expected = "001101000011110000"  # OR s0, sF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_OUTPUT():
    pass
def test_encode_operation_RETURN():
    pass
def test_encode_operation_RETURNI():
    pass
def test_encode_operation_SHIFT():
    pass


def test_encode_operation_STORE_sx_ss():
    line_of_code = "STORE s0, 63"
    #         "101110xxxxkkkkkkkk" 101110
    binary_instruction_expected = "101110000000111111"  # STORE s0, ss
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_STORE_sx_sy():
    line_of_code = "STORE s0, sF"
    #         "101111xxxxyyyy0000"
    binary_instruction_expected = "101111000011110000"  # STORE s0, sF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_SUB_sx_kk():
    line_of_code = "SUB s0, 127"
    #         "011100xxxxkkkkkkkk"
    binary_instruction_expected = "011100000001111111"  # SUB s0, kk
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_SUB_sx_sy():
    line_of_code = "SUB s0, sF"
    #         "011101xxxxyyyy0000"
    binary_instruction_expected = "011101000011110000"  # SUB s0, sF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_SUBCY_sx_kk():
    line_of_code = "SUBCY s0, 127"
    #         "011110xxxxkkkkkkkk"
    binary_instruction_expected = "011110000001111111"  # SUBCY s0, kk
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_SUBCY_sx_sy():
    line_of_code = "SUBCY s0, sF"
    #         "011111xxxxyyyy0000"
    binary_instruction_expected = "011111000011110000"  # SUBCY s0, sF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_TEST_sx_kk():
    line_of_code = "TEST s0, 127"
    #         "010010xxxxkkkkkkkk"
    binary_instruction_expected = "010010000001111111"  # TEST s0, kk
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_TEST_sx_sy():
    line_of_code = "TEST s0, sF"
    #         "010011xxxxyyyy0000"
    binary_instruction_expected = "010011000011110000"  # TEST s0, sF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_XOR_sx_kk():
    line_of_code = "XOR s0, 127"
    #         "001110xxxxkkkkkkkk"
    binary_instruction_expected = "001110000001111111"  # XOR s0, kk
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_XOR_sx_sy():
    line_of_code = "XOR s0, sF"
    #         "001111xxxxyyyy0000"
    binary_instruction_expected = "001111000011110000"  # XOR s0, sF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin