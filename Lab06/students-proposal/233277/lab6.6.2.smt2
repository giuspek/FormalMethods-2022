(set-option :produce-models true)
(set-option :opt.priority box)

(declare-const A Int)
(declare-const B Int)
(declare-const C Int)
(declare-const D Int)

(define-const AA Int 4)
(define-const AB Int 3)
(define-const AC Int 2)
(define-const AD Int 5)

(define-const BA Int (- 10))
(define-const BB Int 2)
(define-const BC Int 0)
(define-const BD Int (- 1))

(define-const CA Int 7)
(define-const CB Int 5)
(define-const CC Int 2)
(define-const CD Int 3)

(define-const DA Int 0)
(define-const DB Int 8)
(define-const DC Int (- 4))
(define-const DD Int (- 5))

(assert (or (= A AA) (= A AB) (= A AC) (= A AD)))
(assert (or (= B BA) (= B BB) (= B BC) (= B BD)))
(assert (or (= C CA) (= C CB) (= C CC) (= C CD)))
(assert (or (= D DA) (= D DB) (= D DC) (= D DD)))

(maxmin A B C D :id penalty)

(check-sat)
(get-objectives)
(get-model)
(exit)