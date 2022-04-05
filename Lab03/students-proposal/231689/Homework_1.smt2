(set-option :produce-models true)


(declare-const a Int)
(declare-const b Int)
(declare-const c Int)

(declare-const d Int)
(declare-const e Int)

(assert (> a 0))
(assert (< a 10))

(assert (>= b 0))
(assert (< b 10))

(assert (> c 0))
(assert (< c 10))


(assert (= d (+ (* 100 a) (* 10 b) c)))
(assert (= e (+ (* 100 c) (* 10 b) a)))


(assert (= 0 (mod d 4)))
(assert (= 0 (mod e 4)))


(check-sat)

(get-model)

(exit)