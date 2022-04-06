;coloring problem with 3 colors

(declare-const r1 Bool)
(declare-const r2 Bool)
(declare-const r3 Bool)
(declare-const r4 Bool)
(declare-const b1 Bool)
(declare-const b2 Bool)
(declare-const b3 Bool)
(declare-const b4 Bool)
(declare-const g1 Bool)
(declare-const g2 Bool)
(declare-const g3 Bool)
(declare-const g4 Bool)


(assert (not (and r1 r2)))
(assert (not (and r1 r3)))
(assert (not (and r1 r4)))
(assert (not (and r4 r2)))
(assert (not (and r4 r3)))

(assert (not (and b1 b2)))
(assert (not (and b1 b3)))
(assert (not (and b1 b4)))
(assert (not (and b4 b2)))
(assert (not (and b4 b3)))

(assert (not (and g1 g2)))
(assert (not (and g1 g3)))
(assert (not (and g1 g4)))
(assert (not (and g4 g2)))
(assert (not (and g4 g3)))

(assert (or b1 r1 g1))
(assert (or b2 r2 g2))
(assert (or b3 r3 g3))
(assert (or b4 r4 g4))

(check-sat)
(exit)