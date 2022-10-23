# Failed implementation
import math, numpy

class MD5Calc:

    @staticmethod
    def f(b, c, d):
        # (b & c) | (~b & d)
        return numpy.bitwise_or(
            numpy.bitwise_and(b, c),
            numpy.bitwise_and(
                numpy.bitwise_not(b),
                d
            )
        )

    @staticmethod
    def g(b, c, d):
        # (b & d) | (c & ~d)
        return numpy.bitwise_or(
            numpy.bitwise_and(b, d),
            numpy.bitwise_and(
                c, numpy.bitwise_not(d)
            )
        )

    @staticmethod
    def h(b, c, d):
        # b ^ c ^ d
        return numpy.bitwise_xor(
            numpy.bitwise_xor(b, c), d
        )

    @staticmethod
    def i(b, c, d):
        # c ^ (b | ~d)
        return numpy.bitwise_xor(
            c, numpy.bitwise_or(b, numpy.bitwise_not(d))
        )


def generate_hash(msg):
    shift = [
        7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
        5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
        4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
        6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21
    ]
    K = [numpy.uint32(math.floor(2 ** 32 * abs(math.sin(i + 1)))) for i in range(64)]

    # Using big-endian to eval
    a0 = numpy.uint32(0x01234567)
    b0 = numpy.uint32(0x89abcdef)
    c0 = numpy.uint32(0xfedcba98)
    d0 = numpy.uint32(0x76543210)

    byte_arr = to_byte_array(msg)
    og_len = len(byte_arr)

    # Pre-processing
    byte_arr += ["1"]
    byte_arr += ["0"] * ((448 - len(byte_arr)) % 512)
    byte_arr += to_bin_arr(og_len, 64)[::-1]
    print(byte_arr)

    for i in range(0, len(byte_arr) // 512):
        chunk = byte_arr[i * 512:(i + 1) * 512]
        M = [chunk[i * 32:(i + 1) * 32] for i in range(16)]
        A = a0
        B = b0
        C = c0
        D = d0

        for i in range(64):
            if i < 16:
                F, g = MD5Calc.f(B, C, D), i
            elif i < 32:
                F, g = MD5Calc.g(B, C, D), (5 * i + 1) % 16
            elif i < 48:
                F, g = MD5Calc.h(B, C, D), (3 * i + 5) % 16
            else:
                F, g = MD5Calc.i(B, C, D), (7 * i) % 16
            F = numpy.sum([F, A, K[i], bin_arr_to_uint32(M[g])])
            A = D
            D = C
            C = B
            B = numpy.add(B, l_rot(F, shift[i]))
            # print(hex(A), hex(B), hex(C), hex(D))
        a0 = numpy.add(a0, A)
        b0 = numpy.add(b0, B)
        c0 = numpy.add(c0, C)
        d0 = numpy.add(d0, D)

    digest = []
    for i in [a0, b0, c0, d0]:
        digest += to_bin_arr(i, 32)
    # Little endian
    print([a0, b0, c0, d0])
    return "".join(bit_arr_to_hex_byte_arr(digest)[::-1])


def l_rot(num, times):
    arr = to_bin_arr(num, 32)
    shifted_arr = l_rot_arr(arr, times)
    return bin_arr_to_uint32(shifted_arr)


def l_rot_arr(arr, times):
    return arr[times:] + arr[:times]


def bin_arr_to_uint32(arr):
    num = int("".join(arr), 2)
    return numpy.uint32(num)


def to_bin_arr(num, padding=0):
    return list(format(num, f"0{padding}b"))


def to_byte_array(msg):
    arr = []
    for val in bytearray(msg, "ASCII"):
        arr.extend(to_bin_arr(val, 8))
    return arr


def bit_arr_to_hex_byte_arr(arr):
    hx = []
    for i in range(len(arr) // 8):
        val = arr[i*8:(i+1)*8]
        hx += ['{:02x}'.format(int("".join(val), 2))]
    return hx


# Should give 8 zeroes at the beginning
print(generate_hash(""))
