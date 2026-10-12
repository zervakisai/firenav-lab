# 🧭 Πρώτη φορά Git, GitHub και Python; Από εδώ!

**Στόχος:** να τρέξεις το FireNav και να κάνεις το ΠΡΩΤΟ σου Pull Request χωρίς προϋποθέσεις Git.

## 0. Τα βασικά σε 60 δευτερόλεπτα
- **Repository**: φάκελος project με ιστορικό.
- **Git**: το εργαλείο που παρακολουθεί τις αλλαγές.
- **GitHub**: η πλατφόρμα που φιλοξενεί repositories.
- **Issue / ticket**: δουλειά με σαφή κριτήρια ολοκλήρωσης.
- **Branch**: παράλληλη έκδοση εργασίας, χωρίς να χαλάς τη `main`.
- **Commit**: αποθηκευμένη αλλαγή με μήνυμα.
- **Push**: στέλνω τα commits στο GitHub.
- **Pull Request (PR)**: προτείνω να ενσωματωθεί η δουλειά μου στη `main`.

## 1. Δημιούργησε λογαριασμό και δικό σου project
1. Πήγαινε https://github.com και δημιούργησε λογαριασμό.
2. Άνοιξε https://github.com/zervakisai/firenav-lab .
3. Αν το repo έχει ενεργοποιημένο **Use this template**, επίλεξέ το → **Create a new repository** → βάλε όνομα `firenav-lab-myname`. Αν δεν είναι ενεργό, επίλεξε **Fork** → **Create fork**.
4. Επίλεξε **Public**, εκτός αν σου ζητήσει διαφορετικά ο εκπαιδευτής.
5. Το νέο repository είναι δικό σου. **Δεν τροποποιείς το κεντρικό**.

## 2. Εγκατάσταση
- Python 3.10 ή νεότερο: https://www.python.org/downloads/
- VS Code: https://code.visualstudio.com/
- Git: https://git-scm.com/downloads
- Προαιρετικά GitHub Desktop: https://desktop.github.com/ (οπτικό εργαλείο για Git).

Σε Windows επέλεξε **Add python.exe to PATH** στην εγκατάσταση Python (αν υπάρχει). Σε Ubuntu, αν δεν ανοίγει το γραφικό παράθυρο, εγκατάστησε `python3-tk`.

## 3. Κατέβασε το προσωπικό repository
GitHub → πράσινο **Code** → **HTTPS** → Copy URL.
Άνοιξε Terminal στο VS Code:
```bash
git clone https://github.com/YOUR_USERNAME/firenav-lab-myname.git
cd firenav-lab-myname
python app.py
```
Αν `python` δεν αναγνωρίζεται, δοκίμασε `python3` (Linux/macOS) ή `py` (Windows). Αν το Git ζητήσει σύνδεση, χρησιμοποίησε τον browser login / credential manager, **όχι** αποθήκευση κωδικού μέσα σε αρχείο.

## 4. Εκτέλεσε τους ελέγχους
```bash
python -m unittest discover -s tests -v
```
Τα αρχικά tests περνούν, αλλά **δεν** αποδεικνύουν ότι το A* ή το replanning έχουν υλοποιηθεί. Θα προσθέσεις δικά σου tests ανά ticket.

## 5. Πρώτο PR, χωρίς να γράψεις δύσκολο κώδικα
```bash
git switch -c docs/my-first-change
```
Άνοιξε το προσωπικό `README.md`, πρόσθεσε τη γραμμή `My goal: learn autonomous mission planning.`, αποθήκευσε:
```bash
git status
git add README.md
git commit -m "docs: add my learning goal"
git push -u origin docs/my-first-change
```
Πήγαινε στο προσωπικό σου repository → **Compare & pull request** → τίτλος `My first GitHub PR` → **Create pull request** → έλεγξε → **Merge pull request**.

Αν το Git ζητήσει όνομα/email:
```bash
git config --global user.name "Your Name"
git config --global user.email "your-github-email@example.com"
```
Χρησιμοποίησε το email που επιθυμείς να συνδέεται με το GitHub. Για προστασία ιδιωτικότητας μπορείς να χρησιμοποιήσεις το GitHub no-reply email.

## 6. Από ticket σε PR
Διάβασε το κεντρικό FIRE-001 και την αντιγραφή του στα `tickets/`. Άνοιξε ένα **δικό σου Issue** αν δεν δημιουργήθηκε αυτόματα στο προσωπικό repository. Δημιούργησε branch `feature/fire-001`, υλοποίησε μικρά βήματα, πρόσθεσε tests, commit, push, PR. Στο PR εξήγησε τα μαθηματικά και σύνδεσε το Issue με `Closes #N`, όπου N ο αριθμός στο **δικό σου** repository.

## 7. Όταν κολλήσεις
1. Διάβασε το error, όχι μόνο την τελευταία γραμμή.
2. Αναπαρήγαγε το πρόβλημα με μικρό παράδειγμα.
3. Τρέξε τα tests.
4. Δες τα βίντεο [εδώ](VIDEOS_AND_RESOURCES.md).
5. Άνοιξε τον [AI Tutor](AI_TUTOR_SUPERPROMPT_GR.md) και ζήτησε **μία υπόδειξη, όχι όλη τη λύση**.
6. Ζήτησε βοήθεια από συμφοιτητή — η συνεργασία επιτρέπεται.

## 8. Συνηθισμένα λάθη
- `git status`: σου δείχνει τι έχει αλλάξει.
- `git switch main` και `git pull`: συγχρόνισε τη main σου πριν από νέο ticket.
- Αν η εφαρμογή δεν ανοίγει σε headless server, τρέξε την σε υπολογιστή με γραφικό περιβάλλον.
- Μην κάνεις commit passwords, access tokens, προσωπικά δεδομένα ή πραγματικές συντεταγμένες περιστατικών.
- Μην κάνεις `git push --force` αν δεν καταλαβαίνεις ακριβώς γιατί χρειάζεται.

**Checkpoint ημέρας 1:** δικό σου repository + εφαρμογή που ανοίγει + ένα merged PR.
