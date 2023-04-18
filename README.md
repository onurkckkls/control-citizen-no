# Project Summary
**TR:** Bu proje pythonda TC kimlik numaralarının doğruluğunu, mevcut güvenlik önlemleri üzerinden kontrol edebilmek için yazılmış, benim de mevcut projelerimde kullandığım bir sınıftan oluşan kod paketi.

**EN:** This project coded for control the correctness of Turkish citizen numbers over existing security measures.


# Easy Usage
**TR**
- Programınızda herhangi bir yere ekleyin
- Sınıfı çağırın `from citizenNo import CitizenNo`
- Kullanım opsiyonları
    1. `CitizenNo.control("10000000146")`
    2. `citizenNo = CitizenNo("10000000146")` daha sonra `citizenNo.result`'dan D/Y değerine ulaşabilirsiniz
    3. `CitizenNo.multiControl(list)` sonucu list olarak almak için, ya da dictionary olarak almak için `CitizenNo.multiControl(list, 'dict')` kodu kullanılabilir

**EN**
- Add anywhere in your program
- Import the class `from citizenNo import CitizenNo`
- Using options
    1. `CitizenNo.control("10000000146")`
    2. `citizenNo = CitizenNo("10000000146")` then you can take boolean in `citizenNo.result` variable
    3. `CitizenNo.multiControl(list)` for list return, or you can use `CitizenNo.multiControl(list, 'dict')` code for dictionary return


# Requirement
- python 3.5+


# Test Knowledge
**TR:** Test için pytest ve test_citizenNo.py kullanılabilir.

**EN:** You can use pytest and test_citizenNo.py for testing code


# 18.04.2023 Changes
**TR:** Yanlış girilen vatandaş numaralarını, potansiyel olarak doğru olanları bulmak için bir sınıf eklendi.

**Kullanımı:**
    - Sınıfın çağırılması `from potantial import Potantial`
    - `Potantial("1000000014").potantials` sonuç liste olarak gelir

**EN:** Added a class to find incorrectly entered citizen numbers, potential correct ones.

**Usage:**
    - Import the class `from potantial import Potantial`
    - `Potantial("1000000014").potantials` the result comes as a list
    