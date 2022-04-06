(declare-const n1 Bool)
(declare-const n2 Bool)
(declare-const n3 Bool)
(declare-const n4 Bool)

(assert (or (not n2) (not n3)))

; If the assert-soft condition is false, then the cost function "penalty" increases by weight 1
(assert-soft n1 :weight 1 :id penalty)
(assert-soft n2 :weight 1 :id penalty)
(assert-soft n3 :weight 1 :id penalty)
(assert-soft n4 :weight 1 :id penalty)

(minimize penalty)
(check-allsat (n1 n2 n3 n4))
(get-objectives)
(get-model)
(exit)