(set-option :produce-models true)

(declare-const add_tree Int)
(define-fun tot_trees () Int (+ 50 add_tree))
(define-fun apple_per_tree () Int (- 800 (* 10 add_tree)))

(maximize (* tot_trees apple_per_tree) :id cost)
(check-sat)
(get-objectives)
(get-model)
(exit)