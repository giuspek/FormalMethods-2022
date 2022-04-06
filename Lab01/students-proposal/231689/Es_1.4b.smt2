;Variables: a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3
;A = 1, B = 2, C = 3, D = 4

(declare-const a1 Bool)
(declare-const a2 Bool)
(declare-const a3 Bool)
(declare-const b1 Bool)
(declare-const b2 Bool)
(declare-const b3 Bool)
(declare-const c1 Bool)
(declare-const c2 Bool)
(declare-const c3 Bool)
(declare-const d1 Bool)
(declare-const d2 Bool)
(declare-const d3 Bool)
(declare-const A Bool)
(declare-const B Bool)
(declare-const C Bool)
(declare-const D Bool)
(declare-const AA Bool)
(declare-const BB Bool)
(declare-const CC Bool)
(declare-const DD Bool)


;the password should be even
(assert (or b3 d3))


;Cannot use same digit three times
(assert (not(and a1 a2 a3)))
(assert (not(and b1 b2 b3)))
(assert (not(and c1 c2 c3)))
(assert (not(and d1 d2 d3)))

;It is possible to repeat the same digit twice, just make sure the two digits are not adjacent. 
(assert (not(and a1 a2)))
(assert (not(and a2 a3)))
(assert (not(and b1 b2)))
(assert (not(and b2 b3)))
(assert (not(and c1 c2)))
(assert (not(and c2 c3)))
(assert (not(and d1 d2)))
(assert (not(and d2 d3)))


;1 digit for every position
(assert (=> a1 (and (not b1) (not c1) (not d1))))
(assert (=> b1 (and (not a1) (not c1) (not d1))))
(assert (=> c1 (and (not b1) (not a1) (not d1))))
(assert (=> d1 (and (not b1) (not c1) (not a1))))

(assert (=> a2 (and (not b2) (not c2) (not d2))))
(assert (=> b2 (and (not a2) (not c2) (not d2))))
(assert (=> c2 (and (not b2) (not a2) (not d2))))
(assert (=> d2 (and (not b2) (not c2) (not a2))))

(assert (=> a3 (and (not b3) (not c3) (not d3))))
(assert (=> b3 (and (not a3) (not c3) (not d3))))
(assert (=> c3 (and (not b3) (not a3) (not d3))))
(assert (=> d3 (and (not b3) (not c3) (not a3))))

;all three digits must have at least a number
;(assert(and (or x11 x21 x31 x41) (or x12 x22 x32 x42)))
(assert(and (or a1 b1 c1 d1) (or a2 b2 c2 d2) (or a3 b3 c3 d3)))


;unicity of the model
(assert (not (and c1 d2 b3)))
;IT'S NOT UNIQUE

(check-sat)

(exit)