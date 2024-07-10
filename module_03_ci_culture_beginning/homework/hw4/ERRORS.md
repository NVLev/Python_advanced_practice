## Virheet ja korjaukset:

1.  >Error NameError:  name 'datetime' is not defined

***Ratkaisu*** - datetime-moduulin tuonti
***

2.  *get_age* virhe: 

Alkuperäinen `get_age`-funktio vähensi nykyisen vuoden syntymävuodesta, mikä johti negatiiviseen ikään. 

***Ratkaisu*** - oikea logiikka on vähentää syntymävuosi nykyisestä vuodesta.

    def get_age(self) -> int:
        now: datetime.datetime = datetime.datetime.now()
        return now.year - self.yob
***
3.  *set_name* virhe:

Alkuperäinen `set_name`- metodi ei todellisuudessa päivittänyt nimiattribuuttia. Se käytti virheellisesti `self.name = self.name`, mikä ei käytännössä tehnyt mitään. 

***Ratkaisu*** - Korjattu koodi käyttää nyt `self.name = name` uuden nimen antamiseen.

    def set_name(self, name: str) -> None:
        self.name = name
***
4. *set_address* virhe:

>address == address. 

Tämän olisi pitänyt olla `self.address = address`, jotta osoite olisi todella annettu.

***Ratkaisu:*** 

    def set_address(self, address: str) -> None:
        self.address = address
***

5.  *is_homeless* virhe: 

Alkuperäinen `is_homeless`-metodi ei tarkistanut oikeaa attribuuttia. Logiikka käytti address is `None`- muuttujaa, joka tarkistaa, onko address-muuttuja `None`, mutta todellinen attribuutti on `self.addres`.

***Ratkaisu:*** 

    def is_homeless(self) -> bool:
        '''
        returns True if address is not set, false in other case
        '''
        return self.address == ''

