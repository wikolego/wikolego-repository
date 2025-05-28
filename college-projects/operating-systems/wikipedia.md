# Wikipedia about operating systems

Now y are reading Wikipedia about operating systems

## Komendy

### 2>/dev/null

Cool komenda. Jeżeli dodasz ją gdziekolwiek, to cały stderr będzie nie ważny

---

### uname

Wyświetla wszystkie informacje o systemie

- a - wszystkie informacje

---

### who

Wyświetla informacje, kto jest zalogowany

---

### id

Wyświelta identyfikatory użytkownika i grupy

---

### man

Nie ważne

---

### emacs

Edytor plików (u mnie na lapku go nie ma)

---

### nano

Też edytor plików, tyle że lepszy (bo u mnie na lapku jest XD)

---

### tree

- a - wszystkie
- d - tylko katalogi

---

### ls

- a - wszystko
- l - w formie listy
- i - pokazuje numer seryjny pliku

---

### touch

Dotyka plik XD

---

### pwd

Aktualny katalog

---

### mkdir\rmdir

- p - tworzy\usuwa brakujące katalogi nadrzędne

---

### cp

Kopiuje pliki

cp arg1, arg2, ..., destination folder\
cp -r katalog1 katalog2

- r - rekurencyjnie
- i - pyta przed nadpisywaniem
- n - nie nadpisuje

---

### rm

Usuwa pliki

- r - rekurencyjnie (hard)
- i - pyta przed nadpisywaniem
- n - nie nadpisuje

---

### mv

Przesuwa pliki

- i - pyta przed nadpisywaniem
- n - nie nadpisuje

---

### Wzorce w nazwach plików

- \* - wiele
- ? - jeden znak
- [...] - znaki
- [^...] - nie znaki

lista wzorców oddzielonych znakiem |

- ? - zero lub jedno wystąpienie
- \* - zero lub więcej
- \+ - jedno lub więcej
- @ - jeden z podanych wzorców
- ! - wszystko oprócz podanych wzorców

---

### ln

Tworzy dowiązanie twarde do jakiegoś pliku, albo katalogu
ln cel nazwa_linku

- s - dowiązanie miękkie

---

### chmod

Zmienianie uprawnień

chmod opcje plik1, plik2, ...

Opcje, to wsm znasz (u, g, o)\
a = ugo

---

### chown\chgrp

Zmienia właściciela\grupę plików\katalogów

- R - rekursywnie

---

### find (się zaczyna XD)

Wyszukuje wg wzorca

find dir options string

#### Options

---

- name - big\small letters different
- iname - big\small letters same

---

- type - typy plików (np. d - directory)

---

- mtime - modification time (zmiana zawartosci pliku)
- atime - access time (odczyt, zapis lub wykonanie)
- ctime - change status (eg. change access rights)

---

- mmin, amin, cmin - to samo, co time tylko, że w minutach

---

- newer - później zmodyfikowane, niż dany plik, folder itd.

---

- size - rozmiar pliku.\
  "\+" - większy\
  "\-" - mniejszy
- k - kilo bajty
- c - bajty

---

- user, group - właściciel pliku

---

- perm - prawa dostępu do pliku (podobne do chmod)

| Option        | Description                                       |
| ------------- | ------------------------------------------------- |
| `-perm mode`  | Dokładnie dopasowane uprawnienia                  |
| `-perm -mode` | Wszystkie podane bity muszą być ustawione         |
| `-perm /mode` | Dowolny z podanych bitów musi być ustawiony       |
| `-perm +mode` | Stara wersja równoważna `/mode`, już przestarzała |

---

Warunki złożone

| Option      | Description |
| ----------- | ----------- |
| !           | negacja     |
| -o          | lub         |
| \\( ... \\) | grupowanie  |

---

#### exec, ok

Pozwalają na wykonanie komendy dla znalezionych plików.\
`-ok` pyta zgodę, a `-exec` nie

find ... -exec\ok jakas_komenda{} \;

---

### ps

Wypisuje jakieś tam procesy

| Option   | Description                                 |
| -------- | ------------------------------------------- |
| `-A, -e` | wszystkie procesy                           |
| `-u`     | należące do użytkowników                    |
| `-f`     | pełny format atrybutów                      |
| `-l`     | długa lista atrybutów                       |
| `-x`     | procesy, które nie są związane z terminalem |
