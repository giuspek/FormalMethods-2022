; This implementation is not correct

; sat
; 
; (objectives
;  (ncolors 0)
; )
; (model
;   (define-fun x1 () Int 4)
;   (define-fun x2 () Int 3)
;   (define-fun x3 () Int 2)
;   (define-fun x4 () Int 1)
;   (define-fun x5 () Int 3)
;   (define-fun x6 () Int 4)
;   (define-fun x7 () Int 2)
;   (define-fun x8 () Int 1)
;   (define-fun ncolors () Real (to_real 0))
;   (define-fun I () Real (to_real 0))
; )

(set-option :produce-models true)

(declare-const x1 Int)
(declare-const x2 Int)
(declare-const x3 Int)
(declare-const x4 Int)
(declare-const x5 Int)
(declare-const x6 Int)
(declare-const x7 Int)
(declare-const x8 Int)

(assert (and (>= x1 1) (<= x1 8)))
(assert (and (>= x2 1) (<= x2 8)))
(assert (and (>= x3 1) (<= x3 8)))
(assert (and (>= x4 1) (<= x4 8)))
(assert (and (>= x5 1) (<= x5 8)))
(assert (and (>= x6 1) (<= x6 8)))
(assert (and (>= x7 1) (<= x7 8)))
(assert (and (>= x8 1) (<= x8 8)))

; if '(and (not (= x1 x2)) (not (= x1 x3)))' is false, i.e., x1 has the same color of x2 or the same color of x3... 
(assert-soft (and
    (not (= x1 x2)) (not (= x1 x3)))
    :weight 2 :id ncolors)
(assert-soft (and
    (not (= x2 x1)) (not (= x2 x3)) (not (= x2 x4)))
    :weight 3 :id ncolors)
(assert-soft (and
    (not (= x3 x1)) (not (= x3 x2)) (not (= x3 x4)) (not (= x3 x5)) (not (= x3 x6)) (not (= x3 x8)))
    :weight 6 :id ncolors)
(assert-soft (and
    (not (= x4 x2)) (not (= x4 x3)) (not (= x4 x5)))
    :weight 3 :id ncolors)
(assert-soft (and
    (not (= x5 x3)) (not (= x5 x4)) (not (= x5 x6)) (not (= x5 x7)))
    :weight 4 :id ncolors)
(assert-soft (and
    (not (= x6 x3)) (not (= x6 x5)) (not (= x6 x7)) (not (= x6 x8))))
    :weight 4 :id ncolors)
(assert-soft (and
    (not (= x7 x5)) (not (= x7 x6)) (not (= x7 x8)))
    :weight 3 :id ncolors)
(assert-soft (and
    (not (= x8 x3)) (not (= x8 x6)) (not (= x8 x7)))
    :weight 3 :id ncolors)

(minimize ncolors)
(check-sat)
(get-objectives)
(get-model)
(exit)