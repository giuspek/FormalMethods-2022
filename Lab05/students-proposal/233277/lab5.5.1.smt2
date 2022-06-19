(set-option :produce-models true)
(set-option :opt.priority box)

(define-const base_tree Int 50)
(declare-const add_tree Int)
(declare-const apple_per_tree Int)
(declare-const total_apple Int)

(assert (= apple_per_tree (- 800 (* 10 add_tree))))
(assert (= total_apple (* apple_per_tree (+ base_tree add_tree))))

(maximize total_apple)

(check-sat)
(get-objectives)
(get-model)
(exit)