class CitizenNo:
    """Kimlik Numarası Kontrolü

    Raises:
        ValueError: Kimlik numarasında sayı dışında değer varsa ve ERRORS sınıf değişkeni True ise
        ValueError: Kimlik numarası 11 rakamdan oluşmuyorsa ve ERRORS sınıf değişkeni True ise

    Returns:
        None: Hiçbir şey döndürmez, cls.result değişkeninden True ya da False değeri alınabilir. 
    """
    ERRORS = False

    def __init__(self, citizenNo: str):
        self.citizenNo = str(citizenNo).strip()

        if self.isNotBeginZero() and self.isLengthTrue():
            try:
                # Rakam çevrilip liste oluşturulmaı
                self.citizenNo = [int(c) for c in self.citizenNo]
            except ValueError:
                if CitizenNo.ERRORS:
                    raise ValueError("Kimlik Numarası Sadece Rakamlardan Oluşmalı.")
                else:
                    self.result = False
                    return
        else:
            if CitizenNo.ERRORS:
                raise ValueError("Kimlik Numarası 11 Rakamdan Oluşmalı")
            else:
                self.result = False
                return

        self.result = self.isControlTen() and self.isControlEleven()

    def __str__(self):
        if self.result:
            return f"{''.join(str(c) for c in self.citizenNo)} Numaralı TC Kimlik Numarası Doğru"
        else:
            return f"Girilen TC Kimlik Numarası Yanlış"

    def isNotBeginZero(self) -> bool:
        """Sıfır ile başlamadığının kontrolü

        Returns:
            bool: Sıfır ile başlamıyorsa True
        """
        return not self.citizenNo[0] == "0"

    def isLengthTrue(self) -> bool:
        """Kimlik numarası uzunluğu kontrolü

        Returns:
            bool: Kimlik numarası 11 rakama eşit mi
        """
        return len(self.citizenNo) == 11

    def isControlTen(self) -> bool:
        """10. Rakamın Kontrolü

        Returns:
            bool: (teklerToplamı * 7 - ciftlerToplamı) mod 10 onuncu rakama eşit mi
        """
        return self.citizenNo[9] == (
            ((7 * sum(self.citizenNo[:9:2])) - sum(self.citizenNo[1:9:2])) % 10
        )

    def isControlEleven(self) -> bool:
        """11. Rakamın Kontrolü

        Returns:
            bool: 10 Rakamın toplamının mod 10 u 11. rakama eşit mi?
        """
        return self.citizenNo[10] == (sum(self.citizenNo[:10]) % 10)

    @classmethod
    def control(cls, citizenNo: int) -> bool:
        """TC kimlik no kontrolü sonrası kontrol etmek için

        Args:
            citizenNo (str): Kimlik Numarası Bilgisi

        Returns:
            bool: Kimlik numarası doğru ise True döndürür
        """
        return cls(citizenNo).result

    @classmethod
    def multiControl(cls, *multiCitizenNo, returnType: str = "list"):
        """Verilen tüm TC kimlik numaralarını tek seferde kontrol eder.

        Args:
            rtype (str, optional): return type, "list" veya "dict" Değerleri alır. Defaults to "list".

        Returns:
            list | dict: Doğru olanlar için True yanlış olanlar için False içeren bir list veya dict oluşturur
        """
        if returnType == "list":
            return [cls.control(citizenNo) for citizenNo in multiCitizenNo]
        elif returnType == "dict":
            return {citizenNo: cls.control(citizenNo) for citizenNo in multiCitizenNo}

    @classmethod
    def getFromConsole(cls) -> None:
        """Konsoldan TC Kimlik Numarası Almak İçin"""
        while True:
            citizenNo = input("TC Kimlik Numarası(çıkmak için q): ")
            if citizenNo == "q":
                return
            else:
                print(cls(citizenNo))


def main():
    CitizenNo.getFromConsole()


if __name__ == "__main__":
    main()
