(set-option :produce-models true)

(declare-const x (Array Int Int))

(assert (= x (store x 1 16)))

; Iteration 1
(assert (ite (= (mod (select x 1) 2) 0) (= x (store x 2 (div (select x 1) 2))) (= x (store x 2 (+ (* (select x 1) 3) 1)))))

; Iteration 2
(assert (ite (= (mod (select x 2) 2) 0) (= x (store x 3 (div (select x 2) 2))) (= x (store x 3 (+ (* (select x 2) 3) 1)))))

; Iteration 3
(assert (ite (= (mod (select x 3) 2) 0) (= x (store x 4 (div (select x 3) 2))) (= x (store x 4 (+ (* (select x 3) 3) 1)))))

; Iteration 4
(assert (ite (= (mod (select x 4) 2) 0) (= x (store x 5 (div (select x 4) 2))) (= x (store x 5 (+ (* (select x 4) 3) 1)))))

; Check if ends in 5 turns
(assert (=> (and (not (= (select x 1) 1)) (not (= (select x 2) 1)) (not (= (select x 3) 1)) (not (= (select x 4) 1)) (not (= (select x 5) 1))) false))

(check-sat)
(get-model)
(exit)