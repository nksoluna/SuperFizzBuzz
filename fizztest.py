import superfizzbuzzclass
import unittest


class TestFizzBuzz(unittest.TestCase):

    # ----- Test Case For all Case in Some Scenario -------------- #

    #case 1 -  Fizz and Buzz
    def test_give_5_shoud_be_Buzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(5), 'Buzz', 'Should be Buzz')
    def test_give_3_shoud_be_Fizz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(3), 'Fizz', 'Should be Fizz')
    def test_give_237_shoud_be_Fizz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(237), 'Fizz', 'Should be Fizz')
    def test_give_786_shoud_be_Fizz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(786), 'Fizz', 'Should be Fizz')
    def test_give_5065_shoud_be_Buzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(5065), 'Buzz', 'Should be Buzz')
    def test_give_4655_shoud_be_Buzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(4655), 'Buzz', 'Should be Buzz')
    def test_give_6573_shoud_be_Fizz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(6573), 'Fizz', 'Should be Fizz')
    def test_give_9516_shoud_be_Fizz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(9516), 'Fizz', 'Should be Fizz')
    def test_give_8485_shoud_be_Buzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(8485), 'Buzz', 'Should be Buzz')
    def test_give_5585_shoud_be_Buzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(5585), 'Buzz', 'Should be Buzz')



    # case 2 - FizzFizz and BuzzBuzz
    def test_give_27_shoud_be_FizzFizz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(27), 'FizzFizz', 'Should be FizzFizz')
    def test_give_657_shoud_be_FizzFizz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(657), 'FizzFizz', 'Should be FizzFizz')
    def test_give_7677_shoud_be_FizzFizz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(7677), 'FizzFizz', 'Should be FizzFizz')
    def test_give_6381_shoud_be_FizzFizz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(6381), 'FizzFizz', 'Should be FizzFizz')
    def test_give_5139_shoud_be_FizzFizz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(5139), 'FizzFizz', 'Should be FizzFizz')
    def test_give_1775_shoud_be_BuzzBuzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(1775), 'BuzzBuzz', 'Should be BuzzBuzz')
    def test_give_7075_shoud_be_BuzzBuzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(7075), 'BuzzBuzz', 'Should be BuzzBuzz')
    def test_give_6275_shoud_be_BuzzBuzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(6275), 'BuzzBuzz', 'Should be BuzzBuzz')
    def test_give_2825_shoud_be_BuzzBuzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(2825), 'BuzzBuzz', 'Should be BuzzBuzz')
    def test_give_7775_shoud_be_BuzzBuzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(7775), 'BuzzBuzz', 'Should be BuzzBuzz')
    
   
   
   
   
   
   # case 3 - FizzFizzBuzzBuzz and FizzBuzz
    def test_give_1395_shoud_be_FizzBuzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(1395), 'FizzBuzz', 'Should be FizzBuzz')
    def test_give_5235_shoud_be_FizzBuzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(5235), 'FizzBuzz', 'Should be FizzBuzz')
    def test_give_30_shoud_be_FizzBuzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(30), 'FizzBuzz', 'Should be FizzBuzz')
    def test_give_9645_shoud_be_FizzBuzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(9645), 'FizzBuzz', 'Should be FizzBuzz')
    def test_give_6915_shoud_be_FizzBuzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(6915), 'FizzBuzz', 'Should be FizzBuzz')
    def test_give_5175_shoud_be_FizzFizzBuzzBuzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(5175), 'FizzFizzBuzzBuzz', 'Should be FizzFizzBuzzBuzz')
    def test_give_1575_shoud_be_FizzFizzBuzzBuzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(1575), 'FizzFizzBuzzBuzz', 'Should be FizzFizzBuzzBuzz')
    def test_give_4275_shoud_be_FizzFizzBuzzBuzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(4275), 'FizzFizzBuzzBuzz', 'Should be FizzFizzBuzzBuzz')
    def test_give_3825_shoud_be_FizzFizzBuzzBuzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(3825), 'FizzFizzBuzzBuzz', 'Should be FizzFizzBuzzBuzz')
    def test_give_2475_shoud_be_FizzFizzBuzzBuzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(2475), 'FizzFizzBuzzBuzz', 'Should be FizzFizzBuzzBuzz')






     # case 4 - NoFizzBuzz
    def test_give_17_shoud_be_NoFizzBuzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(17), 'NoFizzBuzz', 'Should be NoFizzBuzz')
    def test_give_964_shoud_be_NoFizzBuzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(964), 'NoFizzBuzz', 'Should be NoFizzBuzz')
    def test_give_127_shoud_be_NoFizzBuzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(127), 'NoFizzBuzz', 'Should be NoFizzBuzz')
    def test_give_1151_shoud_be_NoFizzBuzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(1151), 'NoFizzBuzz', 'Should be NoFizzBuzz')
    def test_give_3527_shoud_be_NoFizzBuzz(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(3527), 'NoFizzBuzz', 'Should be NoFizzBuzz')

    # case  - More Than 10,000
    def test_give_10001_shoud_be_moretenthousand(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(10001), 'More Than 10,000 please insert new number', 'Should be More Than 10,000 please insert new number')
    def test_give_103101_shoud_be_moretenthousand(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(103101), 'More Than 10,000 please insert new number', 'Should be More Than 10,000 please insert new number')
    def test_give_762001_shoud_be_moretenthousand(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(762001), 'More Than 10,000 please insert new number', 'Should be More Than 10,000 please insert new number')
    def test_give_65642_shoud_be_moretenthousand(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(65642), 'More Than 10,000 please insert new number', 'Should be More Than 10,000 please insert new number')
    def test_give_8655456654_shoud_be_moretenthousand(self):
        self.assertEqual(superfizzbuzzclass.callClassFunction().callSuperFizzbuzz().returnresult(8655456654), 'More Than 10,000 please insert new number', 'Should be More Than 10,000 please insert new number')