# Failed implementation
import math
import struct
from bitarray import bitarray


class MD5:

    @staticmethod
    def hash(key):
        pre_processed = MD5._preprocess(key)
        calculated = MD5._calculate(pre_processed)
        return MD5._to_hash(*calculated)

    @staticmethod
    def _preprocess(key):
        bit_array = bitarray(endian="big")
        bit_array.frombytes(key.encode("utf-8"))
        bit_array.append(1)
        for i in range((448 - len(bit_array)) % 512):
            bit_array.append(0)

        # Convert to little endian
        bit_array = bitarray(bit_array, endian="little")

        length = (len(key) * 8) % pow(2, 64)
        length_bit_array = bitarray(endian="little")
        # < = little endian, Q = unsigned long
        length_bit_array.frombytes(struct.pack("<Q", length))

        bit_array.extend(length_bit_array)
        return bit_array

    @staticmethod
    def _calculate(bit_array):
        # a0 = 0x67452301
        # b0 = 0xEFCDAB89
        # c0 = 0x98BADCFE
        # d0 = 0x10325476
        # a0 = 0x01234567
        # b0 = 0x89ABCDEF
        # c0 = 0xFEDCBA98
        # d0 = 0x76543210

        F = lambda b, c, d: (b & c) | (~b & d)
        G = lambda b, c, d: (b & d) | (c & ~d)
        H = lambda b, c, d: b ^ c ^ d
        I = lambda b, c, d: c ^ (b | ~d)

        shifts = (
            7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
            5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,
            4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
            6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21
        )

        K = [math.floor(2 ** 32 * abs(math.sin(i + 1))) for i in range(64)]

        for i in range(0, len(bit_array) // 512):
            chunk = bit_array[i * 512:(i + 1) * 512]

            M = [chunk[i * 32:(i + 1) * 32] for i in range(16)]
            M = [int.from_bytes(word.tobytes(), byteorder="little") for word in M]

            A = a0
            B = b0
            C = c0
            D = d0

            l_rot = lambda x, n: (x << n) | (x >> (32 - n))
            mod_add = lambda a, b: (a + b) % pow(2, 32)

            for i in range(64):
                if i < 16:
                    f, g = F(B, C, D), i
                elif i < 32:
                    f, g = G(B, C, D), (5 * i + 1) % 16
                elif i < 48:
                    f, g = H(B, C, D), (3 * i + 5) % 16
                else:
                    f, g = I(B, C, D), (7 * i) % 16

                tmp = mod_add(f, A)
                tmp = mod_add(tmp, K[i])
                tmp = mod_add(tmp, M[g])

                A = D
                D = C
                C = B
                B = mod_add(B, l_rot(tmp, shifts[i]))

            a0 = mod_add(a0, A)
            b0 = mod_add(b0, B)
            c0 = mod_add(c0, C)
            d0 = mod_add(d0, D)

        return a0, b0, c0, d0

    @staticmethod
    def _to_hash(a0, b0, c0, d0):
        # Convert the buffers to little-endian.
        A = struct.unpack("<I", struct.pack(">I", a0))[0]
        B = struct.unpack("<I", struct.pack(">I", b0))[0]
        C = struct.unpack("<I", struct.pack(">I", c0))[0]
        D = struct.unpack("<I", struct.pack(">I", d0))[0]

        # Output the buffers in lower-case hexadecimal format.
        return f"{format(A, '08x')}{format(B, '08x')}{format(C, '08x')}{format(D, '08x')}"


print(MD5.hash(""))
