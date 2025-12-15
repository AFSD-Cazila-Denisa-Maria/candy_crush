# CandyCrush Automator – Tkinter

## Descriere
Aplicația implementează un joc de tip Candy Crush (match-3) pe o grilă 11×11, conform cerințelor de laborator.  
Jocul detectează formațiuni valide, aplică gravitația, reumple tabla și calculează scorul.  
Proiectul include interfață grafică Tkinter și simulare automată pe 100 de jocuri cu raportare CSV.

---

## Configurația jocului
- Tablă: matrice 11 rânduri × 11 coloane
- Valori posibile pe celule:
  - 0 – gol
  - 1 – roșu
  - 2 – galben
  - 3 – verde
  - 4 – albastru
- Inițializare: valori generate aleator din {1,2,3,4}
- Formațiunile existente după inițializare sunt eliminate automat

---

## Formațiuni și punctaj
- Linie de 3 (orizontală sau verticală) → 5 puncte
- Linie de 4 → 10 puncte
- Linie de 5 → 50 puncte
- Formațiune L (3+3) → 20 puncte
- Formațiune T (3+3) → 30 puncte

### Regula anti-dublare
În cadrul unei cascade, fiecare celulă poate contribui la cel mult o formațiune, prioritar cea cu punctaj mai mare.

---

## Pașii de joc
1. Detectarea formațiunilor valide
2. Eliminarea bomboanelor și actualizarea scorului
3. Aplicarea gravitației
4. Reumplerea tablei
5. Repetarea pașilor până la stabilizare

---

## Condiții de oprire (simulare automată)
- Scor ≥ 10.000 puncte → REACHED_TARGET
- Nu mai există mutări valide → NO_MOVES

---

## Interfață grafică
Interfața este realizată cu Tkinter și oferă:
- grilă 11×11 cu pătrate colorate
- control cu mouse-ul
- animație de cădere
- evidențiere swap
- afișare scor și nivel
- butoane: Pause, Step, Reset, Auto

Pentru compatibilitate cu macOS, celulele sunt implementate folosind `Label` în loc de `Button`.
## Simulare automată și CSV
Aplicația poate rula automat 100 de jocuri și generează fișierul:results/summary.csv
Format CSV:
game_id,points,swaps,total_cascades,reached_target,stopping_reason,moves_to_10000
candy_crush
├── src
│ ├── board.py # logica tablei
│ ├── engine.py # logica jocului
│ ├── gui.py # interfață Tkinter
│ ├── play_candycrush.py
│ └── simulator.py # rulare automată 100 jocuri
├── results
│ └── summary.csv
├── README.md
