(set-option :produce-models true)

(declare-const A Bool)
(declare-const B Bool)
(declare-const C Bool)

(declare-const X1 Bool)
(declare-const X2 Bool)
(declare-const X3 Bool)
(declare-const X4 Bool)
(declare-const O1 Bool)

(declare-const X5 Bool)
(declare-const O2 Bool)

; Original circuit
(assert (= X1 (and A B)))
(assert (= X2 (or B C)))
(assert (= X3 (and B C)))
(assert (= X4 (and X2 X3)))

; Simplified circuit
(assert (= X5 (or A C)))

; Compare 2 circuit, check if not equivalent is satisfiable. If yes => not equivalent, if no => equivalent
(assert (not (= (or X1 X4) (and X5 B))))


(check-sat)
(get-model)
(exit)





