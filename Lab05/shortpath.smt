(set-option :produce-models true)
(set-option :opt.priority box)

(declare-const A Int)
(declare-const B Int)
(declare-const C Int)
(declare-const D Int)
(declare-const E Int)
(declare-const F Int)
(define-fun G () Int 0)
(declare-const H Int)

(assert (or (= F (+ D 5)) (= F (+ G 9))))
(assert (or (= A (+ D 2)) (= A (+ B 4))))
(assert (or (= B (+ A 4)) (= B (+ C 4)) (= B (+ E 6))))
(assert (or (= C (+ B 4)) (= C (+ E 7))))
(assert (or (= D (+ A 2)) (= D (+ E 3)) (= D (+ F 5))))
(assert (or (= H (+ E 8)) (= H (+ G 3))))
(assert (or (= E (+ B 6)) (= E (+ C 7)) (= E (+ D 3)) (= E (+ H 8))))

; Do not write it!
;(assert (or (= G (+ F 9)) (= G (+ H 3))))

; In this case they are redundant
(assert (>= A 0))
(assert (>= B 0))
(assert (>= C 0))
(assert (>= D 0))
(assert (>= E 0))
(assert (>= F 0))
(assert (>= H 0))

(minimize B)
(check-sat)
(get-objectives)
(get-model)
(exit)
