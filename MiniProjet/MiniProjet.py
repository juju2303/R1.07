import sys, random, time
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QColor, QPen, QBrush
from PyQt5.QtCore import Qt

DIM_LABY = 3
DIM_FENETRE = 600
DIM_CASE = max(4, DIM_FENETRE // DIM_LABY)
NORD, EST, SUD, OUEST = 1, 2, 3, 4

def initialise_case(lig, col):
    numero = lig * DIM_LABY + col
    coul = QColor(random.randint(128,255), random.randint(128,255), random.randint(128,255))
    return [numero, True, True, True, True, coul]

def initialise_ligne(lig):
    ligne = []
    for col in range(DIM_LABY):
        ligne.append(initialise_case(lig, col))
    return ligne

def initialise_laby():
    tab = []
    for lig in range(DIM_LABY):
        tab.append(initialise_ligne(lig))
    return tab

def dessine_case(scene, case, x, y):
    scene.addRect(x, y, DIM_CASE, DIM_CASE, QPen(Qt.NoPen), QBrush(case[5]))
    if case[0] >= 0:
        t = scene.addText(str(case[0]))
        t.setDefaultTextColor(Qt.black)
        scale = DIM_CASE / 50.0
        if scale <= 0: scale = 0.1
        t.setPos(x + DIM_CASE/3, y + DIM_CASE/4)
        t.setScale(scale)
    epaisseur = 1 + (79 // max(1, DIM_LABY))
    pen = QPen(Qt.black, epaisseur, Qt.SolidLine, Qt.RoundCap)
    if case[1]: scene.addLine(x, y, x + DIM_CASE, y, pen)
    if case[2]: scene.addLine(x + DIM_CASE, y, x + DIM_CASE, y + DIM_CASE, pen)
    if case[3]: scene.addLine(x, y + DIM_CASE, x + DIM_CASE, y + DIM_CASE, pen)
    if case[4]: scene.addLine(x, y, x, y + DIM_CASE, pen)

def dessine_laby(scene, laby):
    scene.clear()
    for lig in range(DIM_LABY):
        for col in range(DIM_LABY):
            x = col * DIM_CASE
            y = lig * DIM_CASE
            dessine_case(scene, laby[lig][col], x, y)

def voisin_valide(l, c):
    if l == 0 and c == 0: return random.choice([EST, SUD])
    if l == 0 and c == DIM_LABY-1: return random.choice([OUEST, SUD])
    if l == DIM_LABY-1 and c == 0: return random.choice([EST, NORD])
    if l == DIM_LABY-1 and c == DIM_LABY-1: return random.choice([OUEST, NORD])
    if l == 0: return random.choice([EST, SUD, OUEST])
    if l == DIM_LABY-1: return random.choice([EST, NORD, OUEST])
    if c == 0: return random.choice([EST, SUD, NORD])
    if c == DIM_LABY-1: return random.choice([OUEST, SUD, NORD])
    return random.choice([NORD, EST, SUD, OUEST])

def select_cases(laby):
    while True:
        l = random.randrange(DIM_LABY)
        c = random.randrange(DIM_LABY)
        m = voisin_valide(l, c)
        if m == NORD:
            l2, c2 = l-1, c
        elif m == SUD:
            l2, c2 = l+1, c
        elif m == EST:
            l2, c2 = l, c+1
        else:
            l2, c2 = l, c-1
        if 0 <= l2 < DIM_LABY and 0 <= c2 < DIM_LABY:
            if laby[l][c][0] != laby[l2][c2][0]:
                return [l, c, m]

def agglomere_cases(sel, laby):
    l, c, m = sel
    num_base = laby[l][c][0]
    coul_base = laby[l][c][5]
    if m == NORD:
        l2, c2 = l-1, c
    elif m == SUD:
        l2, c2 = l+1, c
    elif m == EST:
        l2, c2 = l, c+1
    else:
        l2, c2 = l, c-1
    num_voisin = laby[l2][c2][0]
    laby[l][c][m] = False
    mur_oppose = {NORD: SUD, SUD: NORD, EST: OUEST, OUEST: EST}
    laby[l2][c2][mur_oppose[m]] = False
    for L in range(DIM_LABY):
        for C in range(DIM_LABY):
            if laby[L][C][0] == num_voisin:
                laby[L][C][0] = num_base
                laby[L][C][5] = coul_base

def nettoie_laby(laby):
    for L in range(DIM_LABY):
        for C in range(DIM_LABY):
            laby[L][C][0] = -1

def entree_sortie(laby):
    e = random.randrange(DIM_LABY)
    s = random.randrange(DIM_LABY)
    laby[e][0][4] = False
    laby[e][0][5] = QColor(255,0,0)
    laby[s][DIM_LABY-1][2] = False
    laby[s][DIM_LABY-1][5] = QColor(0,255,0)

def projet():
    laby = initialise_laby()
    app = QApplication(sys.argv)
    view = QGraphicsView()
    scene = QGraphicsScene()
    view.setScene(scene)
    view.setWindowTitle("Labyrinthe")
    view.setGeometry(100, 100, DIM_FENETRE + 4, DIM_FENETRE + 4)
    scene.setBackgroundBrush(QBrush(QColor(200, 200, 200)))
    view.show()
    dessine_laby(scene, laby)
    nb = 0
    cible = DIM_LABY * DIM_LABY - 1
    while nb < cible:
        end_time = time.time() + 10 / max(1, DIM_LABY ** 2)
        while time.time() < end_time:
            QApplication.processEvents()
        sel = select_cases(laby)
        agglomere_cases(sel, laby)
        nb += 1
        dessine_laby(scene, laby)
    nettoie_laby(laby)
    entree_sortie(laby)
    dessine_laby(scene, laby)
    sys.exit(app.exec_())

projet()
