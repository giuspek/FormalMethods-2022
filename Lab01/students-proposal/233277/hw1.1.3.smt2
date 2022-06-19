(set-option :produce-models true)

(declare-const A Bool)
(declare-const B Bool)
(declare-const C Bool)

(assert (and (not B) C))
(assert (=> (not A) (not C)))
(assert (and C (or (not B) (not A))))

(check-sat)
(get-model)
(exit)