import unittest
import code

class TestCodeFuncs(unittest.TestCase):

    def test_dest(self):
        self.assertEqual(code.dest(None),  '000')
        self.assertEqual(code.dest('M'),   '001')
        self.assertEqual(code.dest('D'),   '010')
        self.assertEqual(code.dest('MD'),  '011')
        self.assertEqual(code.dest('A'),   '100')
        self.assertEqual(code.dest('AM'),  '101')
        self.assertEqual(code.dest('AD'),  '110')
        self.assertEqual(code.dest('AMD'), '111')

    def test_comp(self):
        self.assertEqual(code.comp('0'),   '0101010')
        self.assertEqual(code.comp('1'),   '0111111')
        self.assertEqual(code.comp('-1'),  '0111010')
        self.assertEqual(code.comp('D'),   '0001100')
        self.assertEqual(code.comp('A'),   '0110000')
        self.assertEqual(code.comp('!D'),  '0001101')
        self.assertEqual(code.comp('!A'),  '0110011')
        self.assertEqual(code.comp('-D'),  '0001111')
        self.assertEqual(code.comp('-A'),  '0110011')
        self.assertEqual(code.comp('D+1'), '0011111')
        self.assertEqual(code.comp('A+1'), '0110111')
        self.assertEqual(code.comp('D-1'), '0001110')
        self.assertEqual(code.comp('A-1'), '0110010')
        self.assertEqual(code.comp('D+A'), '0000010')
        self.assertEqual(code.comp('D-A'), '0010011')
        self.assertEqual(code.comp('A-D'), '0000111')
        self.assertEqual(code.comp('D&A'), '0000000')
        self.assertEqual(code.comp('D|A'), '0010101')
        self.assertEqual(code.comp('M'),   '1110000')
        self.assertEqual(code.comp('!M'),  '1110001')
        self.assertEqual(code.comp('-M'),  '1110011')
        self.assertEqual(code.comp('M+1'), '1110111')
        self.assertEqual(code.comp('M-1'), '1110010')
        self.assertEqual(code.comp('D+M'), '1000010')
        self.assertEqual(code.comp('D-M'), '1010011')
        self.assertEqual(code.comp('M-D'), '1000111')
        self.assertEqual(code.comp('D&M'), '1000000')
        self.assertEqual(code.comp('D|M'), '1010101')

    def test_jump(self):
        self.assertEqual(code.jump(None),  '000')
        self.assertEqual(code.jump('JGT'), '001')
        self.assertEqual(code.jump('JEQ'), '010')
        self.assertEqual(code.jump('JGE'), '011')
        self.assertEqual(code.jump('JLT'), '100')
        self.assertEqual(code.jump('JNE'), '101')
        self.assertEqual(code.jump('JLE'), '110')
        self.assertEqual(code.jump('JMP'), '111')

if __name__ == '__main__':
    unittest.main()
