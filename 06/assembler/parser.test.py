import unittest
import parser


class TestParserFuncs(unittest.TestCase):

    def test_extractCommand(self):
        self.assertEqual(parser.extractCommand('  '), None)
        self.assertEqual(parser.extractCommand(''), None)
        self.assertEqual(parser.extractCommand(' @foo // comment'), '@foo')
        self.assertEqual(parser.extractCommand('// comment'), None)
        self.assertEqual(parser.extractCommand('M=A+1'), 'M=A+1')

    def test_commandType(self):
        self.assertEqual(parser.commandType('@Foo'), 'A_COMMAND')
        self.assertEqual(parser.commandType('@23'), 'A_COMMAND')
        self.assertEqual(parser.commandType('@a2:123'), 'A_COMMAND')
        self.assertEqual(parser.commandType('M=A+1;JGT'), 'C_COMMAND')
        self.assertEqual(parser.commandType('D;JLT'), 'C_COMMAND')
        self.assertEqual(parser.commandType('0;JMP'), 'C_COMMAND')
        self.assertEqual(parser.commandType('A=D'), 'C_COMMAND')
        self.assertEqual(parser.commandType('(Bar)'), 'L_COMMAND')
        self.assertEqual(parser.commandType('(Bar:foo)'), 'L_COMMAND')

        with self.assertRaises(ValueError):
            parser.commandType('@2Whif')

        with self.assertRaises(ValueError):
            parser.commandType('A+1;JGU')

    def test_symbol(self):
        self.assertEqual(parser.symbol("@foo"), 'foo')
        self.assertEqual(parser.symbol("@23"), '23')
        self.assertEqual(parser.symbol("(loop)"), 'loop')

        with self.assertRaises(ValueError):
            parser.symbol("D;JGT")


    def test_dest(self):
        self.assertEqual(parser.dest('MD=A+1'), 'MD')
        self.assertEqual(parser.dest('D;JGT'), None)
        with self.assertRaises(ValueError):
            parser.dest("@foo")


    def test_comp(self):
        self.assertEqual(parser.comp('MD=A+1'), 'A+1')
        self.assertEqual(parser.comp('D;JGT'), 'D')
        self.assertEqual(parser.comp('A+1'), 'A+1')
        with self.assertRaises(ValueError):
            parser.comp("@foo")


    def test_jump(self):
        self.assertEqual(parser.jump('D;JGT'), 'JGT')
        self.assertEqual(parser.jump('A+1'), None)
        with self.assertRaises(ValueError):
            parser.jump("@foo")

if __name__ == '__main__':
    unittest.main()
