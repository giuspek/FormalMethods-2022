(set-option :produce-models true)

(declare-const x (Array Int Int))
(declare-const y (Array Int Int))
(declare-const m (Array Int Int))
(declare-const result Int)
(declare-const end (Array Int Int))

; Iteration 1
(assert (= x (store x 1 60)))
(assert (= y (store y 1 16)))
(assert (= m (store m 1 (mod (select x 1) (select y 1)))))

(assert (ite (= (select m 1) 0) (and (= result (select y 1)) (= end (store end 1 1))) (and (= end (store end 1 0)) (= x (store x 2 (select y 1))) (= y (store y 2 (select m 1))))))

; Iteration 2
(assert (= m (store m 2 (mod (select x 2) (select y 2)))))

(assert (ite (= (select m 2) 0) (and (= result (select y 2)) (= end (store end 2 1))) (and (= end (store end 2 0)) (= x (store x 3 (select y 2))) (= y (store y 3 (select m 2))))))

; Iteration 3
(assert (= m (store m 3 (mod (select x 3) (select y 3)))))

(assert (ite (= (select m 3) 0) (and (= result (select y 3)) (= end (store end 3 1))) (and (= end (store end 3 0)) (= x (store x 4 (select y 3))) (= y (store y 4 (select m 3))))))

; Iteration 4
(assert (= m (store m 4 (mod (select x 4) (select y 4)))))

(assert (ite (= (select m 4) 0) (and (= result (select y 4)) (= end (store end 4 1))) (and (= end (store end 4 0)) (= x (store x 5 (select y 4))) (= y (store y 5 (select m 4))))))

; Iteration 5
(assert (= m (store m 5 (mod (select x 5) (select y 5)))))

(assert (ite (= (select m 5) 0) (and (= result (select y 5)) (= end (store end 5 1))) (and (= end (store end 5 0)))))

; Check SAT
(assert (=> (and (= (select end 1) 0) (= (select end 2) 0) (= (select end 3) 0) (= (select end 4) 0) (= (select end 5) 0)) false))

(check-sat)
(get-model)
(exit)