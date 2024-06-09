from src.mybase64 import Base64

import base64


class TestEncode:
    def test_str_to_bit(self):
        plain = b"ABCDEFG"
        want = [
            "010000",
            "010100",
            "001001",
            "000011",
            "010001",
            "000100",
            "010101",
            "000110",
            "010001",
            "11",
        ]

        assert Base64.str_to_bit(plain) == "".join(want)

    def test_fill_padding_bit(self):
        testcases = [
            (["010000", "11"], ["010000", "110000"]),
            (["010000", "1100"], ["010000", "110000"]),
        ]

        for origin, want in testcases:
            origin[-1] = Base64.fill_padding(origin[-1], 6, "0")
            got = origin
            assert got == want

    def test_fill_padding_str(self):
        testcases = [
            (["A"], ["A==="]),
            (["AB"], ["AB=="]),
            (["ABC"], ["ABC="]),
            (["ABCD"], ["ABCD"]),
        ]

        for origin, want in testcases:
            origin[-1] = Base64.fill_padding(origin[-1], 4, "=")
            got = origin
            assert got == want

    def test_convert(self):
        testcases = [
            (
                [
                    "010000",
                    "010100",
                    "001001",
                    "000011",
                    "010001",
                    "000100",
                    "010101",
                    "000110",
                    "010001",
                    "110000",
                ],
                b"QUJDREVGRw==",
            )
        ]

        for bits, want in testcases:
            got = Base64.convert(bits)
            assert got == want

    def test_base64encode(self):
        testcases = [
            b"abcdefg",
            b"ABCDEFG",
            b"helloworld",
            b"hogehogemaster",
            b"base64",
        ]

        for plain in testcases:
            got = base64.b64encode(plain)
            want = Base64.base64encode(plain)
            assert got == want
