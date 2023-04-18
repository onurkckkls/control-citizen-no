import itertools
from citizenNo import CitizenNo

class Potantial:
    """Eksiklik veya fazlalık yüzünden yanlış olan TC kimlik numarasından,
    olası tüm TC kontrol algoritmasına uyan TC kimlik numaralarını bulma

    Returns:
        None: Hiçbir şey döndürmez, potansiyel TC kimlik no bulabilirse self.potantials'e ekler.
    """
    
    def __init__(self, citizenNo) -> None:
        self.citizenNo = str(citizenNo).strip()
        self.citizenNo = "".join([c for c in self.citizenNo if c.isnumeric()])
        self.calculatePotantials()

    @property
    def potantials(self):
        return list(self._potantials)

    def calculatePotantials(self) -> list:
        """TC kimlik numarasını eksiklik veya fazlalık durumuna göre fonksiyonlara yönlendirir.

        Returns:
            list: Potansiyel tüm TC kimlik numaraları döndürür, yoksa boş set objesi döndürür.
        """
        self.lenCitizenNo = len(self.citizenNo)
        self._potantials = set()

        if self.lenCitizenNo < 11:
            self.findDeficentNumber()
        elif self.lenCitizenNo > 11:
            self.findExcessNumber()
        elif self.lenCitizenNo == 11 and CitizenNo(self.citizenNo).result:
            self._potantials.add(self.citizenNo)
        elif self.lenCitizenNo == 11 and not CitizenNo(self.citizenNo).result: 
            print("Henüz tamamlanmamış potansiyel TC bulma metodu")
            
            
    def findDeficentNumber(self) -> None:
        """TC kimlik numarasındaki eksikliği bulabilmek için, 
        Eksiklik sayısını hesaplar, eksiklik kadar karakteri ekleneceği tüm olasılıklarda
        oluşan TC'nin, TC kontrol algoritmasına uyup uymadığını test eder.

        Returns:
            None: Hiçbir şey döndürmez, potansiyel TC kimlik no bulabilirse self.potantials'e ekler
        """
        deficent = 11 - self.lenCitizenNo

        for number in itertools.product(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], repeat=deficent):
            for position in itertools.permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], r=deficent):
                zippedList = list(zip(position, number))
                sortedZippedList = sorted(zippedList, key=lambda x: x[0])
                newCitizenNo = self.citizenNo
                for posNum in sortedZippedList:
                    pos = int(posNum[0])
                    num = posNum[1]

                    newCitizenNo = newCitizenNo[0:pos] + num + newCitizenNo[pos:]

                if CitizenNo(newCitizenNo).result:
                    self._potantials.add(newCitizenNo)
    
    def findExcessNumber(self) -> None:
        """TC kimlik numarasındaki fazlalığı bulabilmek için, 
        Fazlalık sayısını hesaplar, fazlalık kadar karakteri tüm olasılıklarda seçip,
        mevcuttan çıkartarak yeni TC'nin, TC kontrol algoritmasına uyup uymadığını test eder.

        Returns:
            None: Hiçbir şey döndürmez, potansiyel TC kimlik no bulabilirse self.potantials'e ekler
        """
        excess = self.lenCitizenNo - 11
        
        for number in itertools.permutations(enumerate(self.citizenNo), r=excess): # return tuple in tuple, example for excess 2 ((0, '5'), (1, '0'))
            newCitizenNo = self.citizenNo
            sortedNumber = sorted(number, key=lambda x: x[0], reverse=True)
            for letter in sortedNumber:
                newCitizenNo = newCitizenNo[:letter[0]] + newCitizenNo[letter[0]+1:]
                
            if CitizenNo(newCitizenNo).result:
                self._potantials.add(newCitizenNo)

           
    @classmethod
    def getFromConsole(cls) -> None:
        """Konsoldan TC Kimlik Numarası Almak İçin"""
        while True:
            citizenNo = input("TC Kimlik Numarası(çıkmak için q): ")
            if citizenNo == "q":
                return
            else:
                print(cls(citizenNo).potantials)


def main():
    Potantial.getFromConsole()


if __name__ == "__main__":
    main()
