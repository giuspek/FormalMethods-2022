(set-option :produce-models true)
(set-logic QF_NRA)

(define-const xA Real 1)
(define-const xB Real 2)
(define-const yA Real 3)
(define-const yB Real 7)

(declare-const m Real)
(declare-const q Real)

(declare-const x0 Real)

(define-fun intersec_Ox ((m Real) (q Real)) Real (/ (- q) m))

; m = (yB - yA) / (xB - xA)
(assert (= m (/ (- yB yA) (- xB xA)))))

; q = yA - m * xA
(assert (= q (- yA (* m xA))))

; 0 = m * x0 + q => x0 = -q / m
; (assert (= x0 (/ (- q) m)))
(assert (= x0 (intersec_Ox m q)))

(check-sat)
(get-model)
(exit)