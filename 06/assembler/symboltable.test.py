import unittest
import symboltable

class TestSymbolTableFuncs(unittest.TestCase):

    def setUp(self):
        self.lines = [
            "A=D+1",
            "(Loop)",
            "D=A+1",
            "M=D+1",
            "(End)",
            "@end",
            "0;JMP"
        ]
        self.table = { 'End': 3, 'Loop': 1 }

    def test_buildTable(self):
        table = symboltable.buildTable(self.lines)
        self.assertEqual(table["Loop"], 1)
        self.assertEqual(table["End"], 3)

    def test_convertSymbol(self):
        self.assertEqual(symboltable.convertSymbol('AM=D'), 'AM=D')
        self.assertEqual(symboltable.convertSymbol('@R3'), 3)
        self.assertEqual(symboltable.convertSymbol('@End', self.table), 3)



if __name__ == '__main__':
    unittest.main()
