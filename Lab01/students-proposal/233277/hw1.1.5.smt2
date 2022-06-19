(set-option :produce-models true)

(declare-const a Int)
(declare-const b Int)
(declare-const c Int)
(declare-const d Int)

; 3 colors => SAT
(assert (and (<= a 2) (>= a 0)))
(assert (and (<= b 2) (>= b 0)))
(assert (and (<= c 2) (>= c 0)))
(assert (and (<= d 2) (>= d 0)))

(assert (not (= a b)))
(assert (not (= a c)))
(assert (not (= a d)))

(assert (not (= b d)))

(assert (not (= c d)))

(check-sat)
(get-model)

; 2 colors => UNSAT
(assert (and (<= a 1) (>= a 0)))
(assert (and (<= b 1) (>= b 0)))
(assert (and (<= c 1) (>= c 0)))
(assert (and (<= d 1) (>= d 0)))

(check-sat)
(get-model)
(exit)