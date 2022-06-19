(set-option :produce-models true)
(set-option :opt.priority pareto)

(declare-const x1 Int)
(declare-const x2 Int)

(assert (and (>= x1 (- 10)) (<= x1 10)))
(assert (and (>= x2 (- 10)) (<= x2 10)))

(assert (<= (- x2 2) 0))
(assert (<= (- (* x1 x1) x2) 0))

(minimize (- (* 2 x1) x2) :id obj1)
(minimize (- x1) :id obj2)

(check-sat)
(get-objectives)
(get-model)

(assert (not (= x1 1)))
(assert (not (= x2 2)))

(minimize (- (* 2 x1) x2) :id obj1)
(minimize (- x1) :id obj2)

(check-sat)
(get-objectives)
(get-model)

(assert (not (= x1 0)))
(assert (not (= x2 1)))

(minimize (- (* 2 x1) x2) :id obj1)
(minimize (- x1) :id obj2)

(check-sat)
(get-objectives)
(get-model)

; => 2 Pareto solutions

(exit)
