(set-option :produce-models true)

(declare-const a Int)
(declare-const b Int)
(declare-const c Int)

(assert (and (>= a 0) (<= a 4)))
(assert (and (>= b 0) (<= b 4)))
(assert (and (>= c 0) (<= c 4)))

(assert (or (= c 2) (= c 4)))

(assert (not (and (= a b) (= b c) (= a c))))

(assert (not (= a b)))

(assert (not (= b c)))

(check-sat)
(get-model)

; Check if unique
(assert (not (and (= a 4) (= b 3) (= c 2))))
(check-sat)
(get-model)

(exit)
