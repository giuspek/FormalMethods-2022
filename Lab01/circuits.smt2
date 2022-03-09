; Circuit common variables

(declare-const A Bool)
(declare-const B Bool)
(declare-const C Bool)

; First circuit additional variables
(declare-const O1 Bool)
(declare-const X1 Bool)
(declare-const X2 Bool)
(declare-const X3 Bool)
(declare-const X4 Bool)

; Second circuit variables additional variables
(declare-const O2 Bool)
(declare-const H1 Bool)

; First circuit encoding
(assert (= X1 (and A B)))
(assert (= X2 (or B C)))
(assert (= X3 (and B C)))
(assert (= X4 (and X2 X3)))
(assert (= O1 (or X1 X4)))

; Second circuit encoding
(assert (= H1 (or A C)))
(assert (= O2 (and H1 B)))

(assert (not (= O1 O2)))
(check-sat)
(exit)