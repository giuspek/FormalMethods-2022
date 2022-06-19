(set-option :produce-models true)

; Encode Int var
(declare-const a Int)
(declare-const b Int)
(declare-const c Int)
(declare-const abc Int)
(declare-const cba Int)

; Encode Boolean vars to specify which Int var take which value
(declare-const a1 Bool)
(declare-const a2 Bool)
(declare-const a3 Bool)
(declare-const a4 Bool)
(declare-const a5 Bool)
(declare-const a6 Bool)
(declare-const a7 Bool)
(declare-const a8 Bool)
(declare-const a9 Bool)

(declare-const b0 Bool)
(declare-const b1 Bool)
(declare-const b2 Bool)
(declare-const b3 Bool)
(declare-const b4 Bool)
(declare-const b5 Bool)
(declare-const b6 Bool)
(declare-const b7 Bool)
(declare-const b8 Bool)
(declare-const b9 Bool)

(declare-const c1 Bool)
(declare-const c2 Bool)
(declare-const c3 Bool)
(declare-const c4 Bool)
(declare-const c5 Bool)
(declare-const c6 Bool)
(declare-const c7 Bool)
(declare-const c8 Bool)
(declare-const c9 Bool)

(define-fun cal ((a Int) (b Int) (c Int)) Int (+ (* a 100) (* b 10) c))

; a, b, c are positive integers, a != 0, c != 0
(assert (and (<= a 9) (>= a 1)))
(assert (and (<= b 9) (>= b 0)))
(assert (and (<= c 9) (>= c 1)))

(assert (= abc (cal a b c)))
(assert (= cba (cal c b a)))

; abc is a multiples of 4
(assert (= 0 (mod abc 4)))

; cba is a multiples of 4
(assert (= 0 (mod cba 4)))

; Each Bool var corresponds to Int var value
; not xor = <->
(assert (not (xor a1 (= a 1))))
(assert (not (xor a2 (= a 2))))
(assert (not (xor a3 (= a 3))))
(assert (not (xor a4 (= a 4))))
(assert (not (xor a5 (= a 5))))
(assert (not (xor a6 (= a 6))))
(assert (not (xor a7 (= a 7))))
(assert (not (xor a8 (= a 8))))
(assert (not (xor a9 (= a 9))))

(assert (not (xor b0 (= b 0))))
(assert (not (xor b1 (= b 1))))
(assert (not (xor b2 (= b 2))))
(assert (not (xor b3 (= b 3))))
(assert (not (xor b4 (= b 4))))
(assert (not (xor b5 (= b 5))))
(assert (not (xor b6 (= b 6))))
(assert (not (xor b7 (= b 7))))
(assert (not (xor b8 (= b 8))))
(assert (not (xor b9 (= b 9))))

(assert (not (xor c1 (= c 1))))
(assert (not (xor c2 (= c 2))))
(assert (not (xor c3 (= c 3))))
(assert (not (xor c4 (= c 4))))
(assert (not (xor c5 (= c 5))))
(assert (not (xor c6 (= c 6))))
(assert (not (xor c7 (= c 7))))
(assert (not (xor c8 (= c 8))))
(assert (not (xor c9 (= c 9))))

(check-allsat (a1 a2 a3 a4 a5 a6 a7 a8 a9 b0 b1 b2 b3 b4 b5 b6 b7 b8 b9 c1 c2 c3 c4 c5 c6 c7 c8 c9))
(get-model)
(exit)