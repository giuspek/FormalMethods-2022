(set-option :produce-models true)

(declare-const x Int)
(declare-const y Int)
(define-fun prod () Int (* x (* y y)))

(assert (>= x 0))
(assert (>= y 0))
(assert (= (+ x y) 9))

(assert (>= prod 0))
(assert (<= prod 200))

(maximize prod)
(check-sat)
(get-objectives)
(get-model)
(exit)