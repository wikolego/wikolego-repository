# Wikipedia about operating systems

Now y are reading Wikipedia about operating systems

# Komendy

Now y will be looking at commands

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

Wypisuje drzewko katalogów i plików

| Option | Description    |
| ------ | -------------- |
| `-a`   | Wszystkie      |
| `-d`   | Tylko katalogi |

---

### ls

| Option | Description                  |
| ------ | ---------------------------- |
| `-a`   | Wszystko                     |
| `-l`   | W formie listy               |
| `-i`   | Pokazuje numer seryjny pliku |

---

### touch

Dotyka plik XD

---

### pwd

Aktualny katalog

---

### mkdir\rmdir

Tworzy\usuwa katalogi

| Option | Description                               |
| ------ | ----------------------------------------- |
| `-p`   | Tworzy\usuwa brakujące katalogi nadrzędne |

---

### cp

Kopiuje pliki

`cp arg1, arg2, ..., destination folder\`
`cp -r katalog1 katalog2`

| Option | Description              |
| ------ | ------------------------ |
| `-r`   | Rekurencyjnie            |
| `-i`   | Pyta przed nadpisywaniem |
| `-n`   | Nie nadpisuje            |

---

### rm

Usuwa pliki

| Option | Description              |
| ------ | ------------------------ |
| `-r`   | Rekurencyjnie            |
| `-i`   | Pyta przed nadpisywaniem |
| `-n`   | Nie nadpisuje            |

---

### mv

Przesuwa pliki

| Option | Description              |
| ------ | ------------------------ |
| `-i`   | Pyta przed nadpisywaniem |
| `-n`   | Nie nadpisuje            |

---

### Wzorce w nazwach plików

| Option   | Description                              |
| -------- | ---------------------------------------- |
| `*z`     | Wiele wyrażeń `z` (znak, lub znaki)      |
| `?z`     | Jeden znaków                             |
| `[...]`  | Wszystkie znaki zawarte w nawiasach      |
| `[^...]` | Wszystkie znaki, oprócz tych w nawiasach |

Elementy listy wzorców muszą być oddzielone znakiem `|`

| Option | Description                      |
| ------ | -------------------------------- |
| `?z`   | Zero lub jedno wystąpienie       |
| `*z`   | Zero lub więcej                  |
| `+z`   | Jedno lub więcej                 |
| `@`    | Jeden z podanych wzorców         |
| `!`    | Wszystko oprócz podanych wzorców |

---

### ln

Tworzy dowiązanie twarde do jakiegoś pliku, albo katalogu

`ln cel nazwa_linku`

| Option | Description        |
| ------ | ------------------ |
| `-s`   | Dowiązanie miękkie |

---

### chmod

Zmienianie uprawnień

chmod opcje plik1, plik2, ...

Opcje, to wsm znasz (u, g, o)\
a = ugo

---

### chown\chgrp

Zmienia właściciela\grupę plików\katalogów

| Option | Description |
| ------ | ----------- |
| `-R`   | Rekursywnie |

---

### find (się zaczyna XD)

Wyszukuje wg wzorca

`find dir options string`

#### Options

---

| Option   | Description                          |
| -------- | ------------------------------------ |
| `-name`  | Bierze pod uwagę wielkości liter     |
| `-iname` | Nie bierze pod uwagę wielkości liter |

---

- type - typy plików (np. d - directory)

---

| Option   | Description                               |
| -------- | ----------------------------------------- |
| `-mtime` | Ostatni czas zmiany wartości pliku        |
| `-atime` | Ostatni czas odczytu, zpisu lub wykonania |
| `-ctime` | Ostatni czas zmiany praw dostępu          |

---

| Option  | Description                            |
| ------- | -------------------------------------- |
| `-mmin` | To samo, co `-mtime`, tylko w minutach |
| `-amin` | To samo, co `-atime`, tylko w minutach |
| `-cmin` | To samo, co `-ctime`, tylko w minutach |

---

- newer - później zmodyfikowane, niż dany plik, folder itd.

---

| Option     | Description                    |
| ---------- | ------------------------------ |
| `-size +X` | Rozmiar pliku większy niż `X`  |
| `-size -X` | Rozmiar pliku mniejszy niż `X` |
| `-size Xk` | Rozmiar pliku w kilobajtach    |
| `-size Xc` | Rozmiar pliku w bajtach        |

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

| Option  | Description |
| ------- | ----------- |
| `!`     | negacja     |
| `-o`    | lub         |
| `(...)` | grupowanie  |

---

#### exec, ok

Pozwalają na wykonanie komendy dla znalezionych plików.\
`-ok` pyta zgodę, a `-exec` nie

`find ... -exec\-ok jakas_komenda{} \;`

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

---

### pstree

Hierarchia procesów

---

### top

users, proc, CPU, memory statistics, ps

---

### kill

Usuwanie procesów

`kill [-nazwa lub nr sygnalu] procid`

| Option | Number | Description |
| ------ | ------ | ----------- |
| HUP    | 1      | hung up     |
| TERM   | 2      | terminate   |
| KILL   | 9      | kill        |

---

### cat

Edytuje plik. Ma różne opcje.

`cat file`\
`cat file1 > file2`\
`cat file1 >> file2`

| Option       | Description                                                |
| ------------ | ---------------------------------------------------------- |
| `-n`         | Dodaje do lini indeksy od 1                                |
| `<< keyword` | Pobiera kolejne linie tekstu, dopóki nie wystąpi `keyword` |
| `-`          | Czyta z stdin                                              |

---

### head, tail

Wybiera linijki rozpoczynając od przodu\tyłu

| Option | Description |
| ------ | ----------- |
| `-n`   | Ilość lini  |

---

### tee

Pisze output do dodatkowo wybranych plików

| Option | Description                     |
| ------ | ------------------------------- |
| `-a`   | Dopisuje wyniki do danego pliku |

---

### sort

Coś tam sortuje

| Option  | Description                                       |
| ------- | ------------------------------------------------- |
| `-n`    | Ciągi znaków z cyframi interpretowane jako liczby |
| `-f`    | Pomiń wielkości liter                             |
| `-r`    | Sortowanie na odwrót                              |
| `-kX,X` | `k`-ta kolumna                                    |

---

### uniq

Usuwa sąsiednie, powtarzające się linie
Z `-d` duplikaty (I dunno man)

---

### wc

Policzenie liń\słów\znaków

| Option | Description   |
| ------ | ------------- |
| `-l`   | Liczba liń    |
| `-w`   | Liczba słów   |
| `-c`   | Liczba znaków |

---

### tr

Zmienia pewne znaki na inne

`tr 'inp_ciag' 'out_ciag'`

| Option | Description                              |
| ------ | ---------------------------------------- |
| `-d`   | Usuwa znaki, zamiast ich zmieniać        |
| `-s`   | Zmienia powtórzenia znaków na jeden znak |

---

### cut

Wybiera tylko pewne kolumny

| Option | Description                |
| ------ | -------------------------- |
| `-f`   | Indeks kolumn do usunięcia |

---

# Okej, przygotuj się na grep

### grep

Komenda

---
