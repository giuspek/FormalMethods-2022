(set-option :produce-models true)

(declare-const A1 Bool)
(declare-const A2 Bool)
(declare-const A3 Bool)

(declare-const B1 Bool)
(declare-const B2 Bool)
(declare-const B3 Bool)

(declare-const C1 Bool)
(declare-const C2 Bool)
(declare-const C3 Bool)


; A does not want to sit next to C
(assert (and (not A2) (not C2)))

; A does not want to sit in the leftmost chair
(assert (not A1))

; B does not want to sit at the right of C
(assert (not (or (and B2 C1) (and B3 C2))))

; Each person sit at least 1 chair
(assert (or A1 A2 A3))
(assert (or B1 B2 B3))
(assert (or C1 C2 C3))

; Each person sit at most 1 chair
(assert (and A1 (not A2) (not A3)))
(assert (and A2 (not A1) (not A3)))
(assert (and A3 (not A1) (not A2)))

(assert (and B1 (not B2) (not B3)))
(assert (and B2 (not B1) (not B3)))
(assert (and B3 (not B1) (not B2)))

(assert (and C1 (not C2) (not C3)))
(assert (and C2 (not C1) (not C3)))
(assert (and C3 (not C1) (not C2)))

; No 2 person sit on the same chair
(assert (and A1 (not B1) (not C1)))
(assert (and B1 (not A1) (not C1)))
(assert (and C1 (not A1) (not B1)))

(assert (and A2 (not B2) (not C2)))
(assert (and B2 (not A2) (not C2)))
(assert (and C2 (not A2) (not B2)))

(assert (and A3 (not B3) (not C3)))
(assert (and B3 (not A3) (not C3)))
(assert (and C3 (not A3) (not B3)))

(check-sat)
(get-model)
(exit)





