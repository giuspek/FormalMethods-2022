(set-option :produce-models true)


(define-fun max ((x Int) (y Int)) Int ( ite (> x y) x y ))


(declare-const A Int)
(declare-const B Int)
(declare-const C Int)
(declare-const D Int)
(declare-const E Int)

(assert (< A 10))
(assert (>= A 0))

(assert (< B 10))
(assert (>= B 0))

(assert (< C 10))
(assert (>= C 0))

(assert (< D 10))
(assert (>= D 0))

(assert (= D (+ A C)))
(assert (= C (* A B)))
(assert (= B (- C B)))
(assert (= D (* A 4)))

;not said in the slides
(assert (distinct A B C D))


(assert (= E (max A (max B (max C D)))))

;(assert (not (and (= A 2) (= B 3) (= C 6) (= D 8))))

(check-sat)

(get-model)

(exit)