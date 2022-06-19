(set-option :produce-models true)
(set-logic QF_NIA)

(declare-const a Int)
(declare-const b Int)
(declare-const c Int)
(declare-const d Int)

(declare-const e Int)

(define-fun max ((x Int) (y Int)) Int (ite (>= x y) x y))

; Single digit numbers
(assert (and (<= 0 a) (>= 9 a)))
(assert (and (<= 0 b) (>= 9 b)))
(assert (and (<= 0 c) (>= 9 c)))
(assert (and (<= 0 d) (>= 9 d)))

; a + c = d
(assert (= (+ a c) d))

; a * b = c
(assert (= (* a b) c))

; c - b = b
(assert (= (- c b) b))

; a * 4 = d 
(assert (= (* a 4) d))

; distinct a b c d
(assert (distinct a b c d))

(assert (= e (max a (max b (max c d)))))

(check-sat)
(get-model)
(exit)
