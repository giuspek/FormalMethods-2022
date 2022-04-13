(set-option :opt.priority lex)

(declare-const x1 Int)
(declare-const x2 Int)

(assert (<= x1 10))
(assert (<= x2 10))
(assert (>= x1 (- 10)))
(assert (>= x2 (- 10)))
(assert (<= (- x2 2) 0))
(assert (<= (- (* x1 x1) x2) 0))

(minimize (- (* 2 x1) x2) :id c1)
(minimize (- x1) :id c2)

(check-sat)
(get-model)

(check-sat)
(get-model)

(check-sat)
(get-model)

(check-sat)
(get-model)

(check-sat)
(get-model)


