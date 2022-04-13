(set-option :opt.priority box)

(define-const AA Int 4)
(define-const AB Int 3)
(define-const AC Int 2)
(define-const AD Int 5)

(define-const BA Int (- 10))
(define-const BB Int 2)
(define-const BC Int 4)
(define-const BD Int (- 1))

(define-const CA Int 7)
(define-const CB Int 5)
(define-const CC Int 2)
(define-const CD Int 3)

(define-const DA Int 0)
(define-const DB Int 8)
(define-const DC Int (- 4))
(define-const DD Int (- 5))

(declare-const rA Int)
(assert (or (= rA AA) (= rA AB) (= rA AC) (= rA AD) ))

(declare-const rB Int)
(assert (or (= rB BA) (= rB BB) (= rB BC) (= rB BD) ))

(declare-const rC Int)
(assert (or (= rC CA) (= rC CB) (= rC CC) (= rC CD) ))

(declare-const rD Int)
(assert (or (= rD DA) (= rD DB) (= rD DC) (= rD DD) ))

(maxmin rA rB rC rD :id penalty)

(check-sat)
(get-objectives)
(get-model)

(exit)