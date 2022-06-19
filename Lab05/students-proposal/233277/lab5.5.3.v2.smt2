(set-option :produce-models true)
(set-option :opt.priority box)

(declare-const n1 Bool)
(declare-const n2 Bool)
(declare-const n3 Bool)
(declare-const n4 Bool)

(assert (xor n2 n3))

(assert-soft (not n1) :weight 1 :id size_clique)
(assert-soft (not n2) :weight 1 :id size_clique)
(assert-soft (not n3) :weight 1 :id size_clique)
(assert-soft (not n4) :weight 1 :id size_clique)

(maximize size_clique)

(check-sat)
(get-objectives)
(get-model)
(exit)