def switch_endian(n, size_bit):
  
    if (n > 0) and (size_bit >= 8) and (size_bit & (size_bit - 1) == 0) and n <2**size_bit:
        conv_hex = hex(n)
        conv_hex = conv_hex[2:].zfill((len(conv_hex[2:]) +1) // 2 * 2)
        return conv_hex        
    return None

print(switch_endian(123, 16))



