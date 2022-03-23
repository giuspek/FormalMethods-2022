(set-option :produce-models true)

(define-fun max ((a Int) (b Int)) Int (ite (>= a b) a b))

(declare-const e Int)

(declare-const a Int)
(declare-const b Int)
(declare-const c Int)
(declare-const d Int)

(assert (>= a 0))
(assert (<= a 9))
(assert (>= b 0))
(assert (<= b 9))
(assert (>= c 0))
(assert (<= c 9))
(assert (>= d 0))
(assert (<= d 9))

(assert (= d (+ a c)))
(assert (= c (* a b)))
(assert (= b (- c b)))
(assert (= d (* a 4)))

(assert (distinct a b c d))

(assert (= e (max a (max b (max c d))) ))

(check-sat)
(get-model)
(exit)