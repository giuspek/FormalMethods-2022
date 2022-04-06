;coloring problem with 2 colors

(declare-const r1 Bool)
(declare-const r2 Bool)
(declare-const r3 Bool)
(declare-const r4 Bool)
(declare-const b1 Bool)
(declare-const b2 Bool)
(declare-const b3 Bool)
(declare-const b4 Bool)


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

(assert (or b1 r1))
(assert (or b2 r2))
(assert (or b3 r3))
(assert (or b4 r4))

(check-sat)
(exit)