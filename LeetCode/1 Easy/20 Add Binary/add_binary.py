class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_length: int = len(a)
        b_length: int = len(b)

        a_padded: str = a
        b_padded: str = b

        if a_length < b_length:
            a_padded = "0" * (b_length - a_length) + a_padded
        else:
            b_padded = "0" * (a_length - b_length) + b_padded

        final_str: str = ""
        carry = 0

        for i in range(max(a_length, b_length) - 1, -1, -1):
            a_val = int(a_padded[i])
            b_val = int(b_padded[i])

            if a_val == 0 and b_val == 0 and carry == 0:
                final_str = "0" + final_str
                carry = 0
            elif a_val == 1 and b_val == 0 and carry == 0:
                final_str = "1" + final_str
                carry = 0
            elif a_val == 0 and b_val == 1 and carry == 0:
                final_str = "1" + final_str
                carry = 0
            elif a_val == 1 and b_val == 1 and carry == 0:
                final_str = "0" + final_str
                carry = 1
            elif a_val == 0 and b_val == 0 and carry == 1:
                final_str = "1" + final_str
                carry = 0
            elif a_val == 1 and b_val == 0 and carry == 1:
                final_str = "0" + final_str
                carry = 1
            elif a_val == 0 and b_val == 1 and carry == 1:
                final_str = "0" + final_str
                carry = 1
            elif a_val == 1 and b_val == 1 and carry == 1:
                final_str = "1" + final_str
                carry = 1

        if carry == 1:
            final_str = "1" + final_str

        return final_str
