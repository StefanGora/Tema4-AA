# Tema4-AA

Pentru crearea acestei teme am folosit documentatia oferita de acest Pdf :
http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.32.3730&rep=rep1&type=pdf
In acesta se prezinta la subpunctul 4.2.1 o metoda de rezolvare a transformarii k vertex cover - Sat
pri obtinerea uni multimi X si a unei formule F.
In cadrul formulei F sunt utilizate doaua formule prezentate in primele pagini ale Pdf-ului:
- at_least_one ce presupune crearea unui for loop de la 1 la un numar x, in care se face sau logic
intre toti termenii din for loop
-at_most_one presupune utilizarea a doua for loop-uri unul care porneste de la i = 1 la un numar x,
iar cel de al doilea j = i + 1 pana la accelasi numar x. Cele doua loop-uri au ca scop crearea unei seri
de si logici intre toate perechile de tip (~termen_i V ~termen_j).
- Pentru transformarea k vertex - Sat am generat multimea X cu perechi de tip (nod, indice) unde
1 <= indice <= k. Am folosit functia Sort pentru a sorta multimea X dupa al doilea element din fiecare
perche pentru a avea perechiile ordonate de la cel mai mic indice la cel mai mare. Cardinalul multimi
X este egal cu nr_noduir * k ce determina numarul maxim de literali din formula Sat, iar fiecare
perche corespunde unui literal.
- In construirea formulei F1 pe care am denumit-o Sat in codul meu am impartit procesul e crearea a
doua formule F1 sI F2 care au generat stringuri pe care le-am concatenat.
-functia build_F1 consta intr-un for loop de la 0 la k ce apeleaza at_most_one de k ori pe o serie de
submultimi ale lui X ce au cardinalul egal cu numarul de noduri.- Pentru formula F2 am folosit doua functii: build_condition si build_F2 In documentatie F2 consta
intr-un for loop de la 0 la numarul de muchii in care se apeleaza at_least_one pe o multime de tip
{ (u, i), (v,i)/ 1<= i <= k}; u = nod_inceput, v=nod_sfarsit pentru o muchie.
Functia build_condition construieste multimea de perechi si asociaza fiecarei perechi un literal iar
apoi build_F2 apeleaza at_least_one de E ori pe rezultatul returnat de build_condition.
-Timpul de rulare este proportional cu numarul de aparitie a literalilor in clause iar transformarea
genereaza n^3 clause de unde rezulta complexitatea transformarii este O(n^3).
