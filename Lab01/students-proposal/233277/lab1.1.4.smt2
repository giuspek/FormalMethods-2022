(set-option :produce-models true)

(declare-const A1 Bool)
(declare-const B1 Bool)

(declare-const A2 Bool)
(declare-const B2 Bool)

(declare-const A3 Bool)
(declare-const B3 Bool)

(declare-const A4 Bool)
(declare-const B4 Bool)

(assert (or (and A1 (not B2) (and B2 (not A1)))))
(assert (not (or A1 B4)))
(assert (or (and B4 (not A3) (not B3)) (and A3 (not A4) (not B4))))



(check-sat)
(get-model)
(exit)





