(set-option :produce-models true)

(declare-const x1 Real)
(declare-const x2 Real)
(declare-const y1 Real)
(declare-const y2 Real)

(declare-const x Real)
(declare-const y Real)

(assert (= (/ (- y y1) (- y2 y1)) (/ (- x x1) (- x2 x1))))
(assert (= y 0))
(assert (= x1 1))
(assert (= x2 2))
(assert (= y1 3))
(assert (= y2 7))

(check-sat)

(get-model)

(exit)