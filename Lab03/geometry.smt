; Use semi columns for comments
(set-option :produce-models true)

(declare-const xa Real)
(declare-const ya Real)
(declare-const xb Real)
(declare-const yb Real)

(declare-const x Real)
(declare-const m Real)
(declare-const q Real)

; Interpreted function
(define-fun f ((x Real)) Real (+ q (* m x)))

(assert (= xa 1))
(assert (= ya 3))
(assert (= xb 2))
(assert (= yb 7))

; Setting m and q (we can also set it using interpreted functions, try it by yourself)
(assert (= m (/ (- yb ya) (- xb xa))))
(assert (= q (- yb (* m xb))))
(assert (= (f x) 0))

(check-sat)
(get-model)
(exit)
