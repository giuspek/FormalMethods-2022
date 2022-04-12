(set-option :produce-models true)

(declare-const n1 Int)
(declare-const n2 Int)
(declare-const n3 Int)
(declare-const n4 Int)

(assert (>= n1 0))
(assert (<= n1 1))
(assert (>= n2 0))
(assert (<= n2 1))
(assert (>= n3 0))
(assert (<= n3 1))
(assert (>= n4 0))
(assert (<= n4 1))

(assert (<= (+ n2 n3) 1))

(assert-soft (= n1 0) :weight 1 :id size_clique)
(assert-soft (= n2 0) :weight 1 :id size_clique)
(assert-soft (= n3 0) :weight 1 :id size_clique)
(assert-soft (= n4 0) :weight 1 :id size_clique)

(maximize size_clique)
(check-sat)
(get-objectives)
(get-model)
(exit)