class callClassFunction():
    def callSuperFizzbuzz(self):
        fizzfizzBuzzbuzz = [
            FizzFizzBuzzBuzz(),  
            FizzBuzz(), 
            FizzFizz(),
            BuzzBuzz(), 
            Fizz(), 
            Buzz(), 
            NoFizzBuzz(), 
            Morethantenthousand() ,
        ]
        return fizzfizzbuzzbuzz(fizzfizzBuzzbuzz)

class fizzfizzbuzzbuzz():
    def __init__(self,fizzfizzBuzzbuzz):
        self.fizzfizzBuzzbuzz = fizzfizzBuzzbuzz
    def returnresult(self,num):
        for numberInclass in self.fizzfizzBuzzbuzz:
            if numberInclass.result(num):
                return numberInclass.result(num)

class numberInclass():
    def result(self,num):
        pass

class FizzBuzz(numberInclass):
    def result(self,n):
        if n % 3 == 0 and n % 5 == 0 and n <= 10000 :

            return "FizzBuzz"

class Fizz(numberInclass):
    def result(self,n):
        if n % 3 == 0 and n <= 10000 :

            return "Fizz"

class Buzz(numberInclass):
   def result(self,n):
        if n % 5 == 0 and n <= 10000 :
            return "Buzz"
class FizzFizz(numberInclass):
    def result(self,n):
        if n % 9 == 0  and n <= 10000:
            return "FizzFizz"

class BuzzBuzz(numberInclass):
    def result(self,n):
        if n % 25 == 0 and n <= 10000 :
            return "BuzzBuzz"

class FizzFizzBuzzBuzz(numberInclass):
    def result(self,n):
        if n % 9 == 0 and n % 25 == 0  and n <= 10000 :
            return "FizzFizzBuzzBuzz"

class NoFizzBuzz(numberInclass):
    def  result(self,n):
        if n % 3 != 0 and n % 5 != 0 and n % 9 != 0 and n % 25 != 0 and n <= 10000:
            return "NoFizzBuzz"

class Morethantenthousand(numberInclass):
    def  result(self,n):
        if n > 10000 :
            return "More Than 10,000 please insert new number"



