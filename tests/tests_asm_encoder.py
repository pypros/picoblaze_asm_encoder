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


def test_encode_operation_CALL():
    line_of_code = "CALL 3FF"
    #         "11000fffaaaaaaaaaa"
    binary_instruction_expected = "110000001111111111"  # CALL 3FF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_CALL_C():
    line_of_code = "CALL C, 3FF"
    #         "11000fffaaaaaaaaaa"
    binary_instruction_expected = "110001101111111111"  # CALL C, 3FF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_CALL_NC():
    line_of_code = "CALL NC, 3FF"
    #         "11000fffaaaaaaaaaa"
    binary_instruction_expected = "110001111111111111"  # CALL NC, 3FF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_CALL_NZ():
    line_of_code = "CALL NZ, 3FF"
    #         "11000fffaaaaaaaaaa"
    binary_instruction_expected = "110001011111111111"  # CALL NZ, 3FF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_CALL_Z():
    line_of_code = "CALL Z, 3FF"
    #         "11000fffaaaaaaaaaa"
    binary_instruction_expected = "110001001111111111"  # CALL Z, 3FF
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


def test_encode_operation_DISABLE_INTERRUPT():
    line_of_code = "DISABLE INTERRUPT"
    #         "111100000000000000"
    binary_instruction_expected = "111100000000000000"  # DISABLE INTERRUPT
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_ENABLE_INTERRUPT():
    line_of_code = "ENABLE INTERRUPT"
    #         "111100000000000001"
    binary_instruction_expected = "111100000000000001"  # ENABLE_INTERRUPT
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_FETCH_sx_kk():
    line_of_code = "FETCH s0, 63"
    #         "000110xxxx00kkkkkk" 000110
    binary_instruction_expected = "000110000000111111"  # FETCH s0, kk
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_FETCH_sx_sy():
    line_of_code = "FETCH s0, sF"
    #         "000111xxxxyyyy0000"
    binary_instruction_expected = "000111000011110000"  # FETCH s0, sF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_INPUT_sx_kk():
    line_of_code = "INPUT s0, 127"
    #         "000100xxxxkkkkkkkk"
    binary_instruction_expected = "000100000001111111"  # INPUT s0, kk
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_INPUT_sx_sy():
    line_of_code = "INPUT s0, sF"
    #         "000101xxxxyyyy0000"
    binary_instruction_expected = "000101000011110000"  # INPUT s0, sF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_JUMP():
    line_of_code = "JUMP 3FF"
    #         "11010fffaaaaaaaaaa"
    binary_instruction_expected = "110100001111111111"  # JUMP 3FF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_JUMP_C():
    line_of_code = "JUMP C, 3FF"
    #         "11010fffaaaaaaaaaa"
    binary_instruction_expected = "110101101111111111"  # JUMP 3FF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_JUMP_NC():
    line_of_code = "JUMP NC, 3FF"
    #         "11010fffaaaaaaaaaa"
    binary_instruction_expected = "110101111111111111"  # JUMP 3FF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_JUMP_NZ():
    line_of_code = "JUMP NZ, 3FF"
    #         "11010fffaaaaaaaaaa"
    binary_instruction_expected = "110101011111111111"  # JUMP 3FF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_JUMP_Z():
    line_of_code = "JUMP Z, 3FF"
    #         "11010fffaaaaaaaaaa"
    binary_instruction_expected = "110101001111111111"  # JUMP 3FF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_LOAD_sx_kk():
    line_of_code = "LOAD s0, 127"
    #         "000000xxxxkkkkkkkk"
    binary_instruction_expected = "000000000001111111"  # LOAD s0, kk
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_LOAD_sx_sy():
    line_of_code = "LOAD s0, sF"
    #         "000000xxxxyyyy0000" 000000
    binary_instruction_expected = "000001000011110000"  # LOAD s0, sF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin

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


def test_encode_operation_OUTPUT_sx_kk():
    line_of_code = "OUTPUT s0, 127"
    #         "101100xxxxkkkkkkkk" 101101
    binary_instruction_expected = "101100000001111111"  # OUTPUT s0, kk
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_OUTPUT_sx_sy():
    line_of_code = "OUTPUT s0, sF"
    #         "101101xxxxyyyy0000"
    binary_instruction_expected = "101101000011110000"  # OUTPUT s0, sF
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_RETURN():
    pass


def test_encode_operation_RETURNI_DISABLE():
    line_of_code = "RETURNI DISABLE"
    #         "111000000000000000"
    binary_instruction_expected = "111000000000000000"  # RETURNI DISABLE
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_RETURNI_ENABLE():
    line_of_code = "RETURNI ENABLE"
    #         "111000000000000001"
    binary_instruction_expected = "111000000000000001"  # RETURNI ENABLE
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_RL_sx():
    line_of_code = "RL s0"
    #         "100000xxxx00000010"
    binary_instruction_expected = "100000000000000010"  # RL s0
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_RR_sx():
    line_of_code = "RR s0"
    #         "100000xxxx00001100"
    binary_instruction_expected = "100000000000001100"  # RR s0
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_SL0_sx():
    line_of_code = "SL0 s0"
    #         "100000xxxx00000110"
    binary_instruction_expected = "100000000000000110"  # SL0 s0
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_SL1_sx():
    line_of_code = "SL1 s0"
    #         "100000xxxx00000111"
    binary_instruction_expected = "100000000000000111"  # SL1 s0
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_SLA_sx():
    line_of_code = "SLA s0"
    #         "100000xxxx00000000"
    binary_instruction_expected = "100000000000000000"  # SLA s0
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_SLX_sx():
    line_of_code = "SLX s0"
    #         "100000xxxx00000100"
    binary_instruction_expected = "100000000000000100"  # SLX s0
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_SR0_sx():
    line_of_code = "SR0 s0"
    #         "100000xxxx00001110"
    binary_instruction_expected = "100000000000001110"  # SR0 s0
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_SR1_sx():
    line_of_code = "SR1 s0"
    #         "100000xxxx00001111"
    binary_instruction_expected = "100000000000001111"  # SR1 s0
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_SRA_sx():
    line_of_code = "SRA s0"
    #         "100000xxxx00001000"
    binary_instruction_expected = "100000000000001000"  # SRA s0
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


def test_encode_operation_SRX_sx():
    line_of_code = "SRX s0"
    #         "100000xxxx00001010"
    binary_instruction_expected = "100000000000001010"  # SRX s0
    asm_encoder = PicoBlazeAsmEncoder()
    asm_encoder.encode_instruction(line_of_code)
    assert binary_instruction_expected == asm_encoder._PicoBlazeAsmEncoder__encoded_instruction_to_bin


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