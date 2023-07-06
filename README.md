# CompareLogs

Przygotowanie logów:
1. Przygotuj plik *.txt z logami z systemu na którym otrzymano wszystkie transakcje. Logi systemowe należy umieścić w jednym pliku (np. pierwszy.txt)

2. Oddzielnie przygotuj podobny plik *.txt z transakcjiami z systemu na którym nie otrzymaliśmy wszystikch (np. drugi.txt)

3. Upewnij się że zapisane logi są w formacie:

  "<DEBU> (00:00:01)> Przeczytano obiekt typu 5 CDC=3690, sn=180874394, date=16-CZE-2023:23:52:52, dateUTC=16-CZE-2023:21:52:52, dateCDC=3690"

4. Upewnij się, że w skopiowanych plikach znajdują się wszystkie transakcje między minSequence oraz maxSequence (odczytaj w raporcie dziennym jakie były)

5. Utworzone pliki umieść w katalogu z source code aplikacji CompareLogs (np. C:\Users\user_name\CompareLogs\pierwszy_plik.txt)

6. Odpal program w VS (RUN/DEBUG)

7. Program w konsoli zapyta o nazwy plików, które chcesz porównać, podaj ich nazwę bez rozszerzenia. (np. "pierwszy" lub "drugi")

8. Program w konsoli zapyta o cdc dnia, z którego chcesz porównać logi.

9. Po wprowadzeniu powyższych danych program utworzy plik o nazwie diff-cdc_date.txt w którym wyszczególnione będą różnice w obu plikach.

UWAGA!
Aby ponownie skorzystać z aplikacji należy powtórzyć wszystkie kroki. Logi w plikach tekstowych należy przygotować ponownie, gdyż po odpaleniu programu program usuwa zbędne logi (o złym cdc itp.) i przycina linię wycinając zbędne dane. Przetwarzane pliki są nadpisywane, dlatego przed przetwarzaniem zaleca się utworzenie kopii.  
