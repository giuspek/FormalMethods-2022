(set-option :produce-models true)
(set-option :opt.priority box)

(declare-const n1 Int)
(declare-const n2 Int)
(declare-const n3 Int)
(declare-const n4 Int)

(assert (and (>= n1 0) (<= n1 1)))
(assert (and (>= n2 0) (<= n2 1)))
(assert (and (>= n3 0) (<= n3 1)))
(assert (and (>= n4 0) (<= n4 1)))

(assert (<= (+ n2 n3) 1))

(assert-soft (= n1 0) :weight 1 :id size-clique)
(assert-soft (= n2 0) :weight 1 :id size-clique)
(assert-soft (= n3 0) :weight 1 :id size-clique)
(assert-soft (= n4 0) :weight 1 :id size-clique)

(maximize size-clique)

(check-sat)
(get-objectives)
(get-model)
(exit)

