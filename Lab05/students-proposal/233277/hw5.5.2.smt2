(set-option :produce-models true)
(set-option :opt.priority box)

(declare-const x Int)
(declare-const y Int)

; 2 non-negative numbers
(assert (>= x 0))
(assert (>= y 0))

; their sum is 9
(assert (= (+ x y) 9))

; product of one and the square of the other is maximum in range (0, 200)
; because x and y's role is equally in this problem, without loss of generality,
; let objective function = x * square(y)

(define-const obj_func Int (* x (* y y)))

(assert (and (> obj_func 0) (< obj_func 200)))

(maximize obj_func)

(check-sat)
(get-objectives)
(get-model)
(exit)