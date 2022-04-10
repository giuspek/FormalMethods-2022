(set-option :produce-models true)

(declare-fun m () (Array Int Int))
(declare-fun x () (Array Int Int))
(declare-fun y () (Array Int Int))
(declare-const res Int)
(declare-fun end () (Array Int Int))

(assert (= (store x 1 60) x))
(assert (= (store y 1 16) y))

(assert (= (store m 1 (mod (select x 1) (select y 1))) m))

; ********************
; First transition
; ********************

(assert
	(=>
		(= (select m 1) 0)
		(and
			(= res (select y 1))
			(= (store end 1 1) end)
		)
	)
)

(assert
	(=>
		(and
			(not (= (select m 1) 0))
			true
		)
		(and
			(= (store end 1 0) end)
			(= (store x 2 (select y 1)) x)
			(= (store y 2 (select m 1)) y)
			(= (store m 2 (mod (select x 2) (select y 2))) m)
		)
	)
)

; If stopped, the values of x, y, m remain the same in the next iterations
(assert
	(=>
		(= (select end 1) 1)
		(and
			(= (store x 2 (select x 1)) x)
			(= (store y 2 (select y 1)) y)
			(= (store m 2 (select m 1)) m)
			(= (store end 2 1) end)
		)
	)
)


; ********************
; Second transition
; ********************


(assert
	(=>
		(and
			(= (select end 1) 0)
			(= (select m 2) 0)

		)
		(and
			(= res (select y 2))
			(= (store end 2 1) end)
		)
	)
)

(assert
	(=>
		(and
			(= (select end 1) 0)
			(not (= (select m 2) 0))
		)
		(and
			(= (store end 2 0) end)
			(= (store x 3 (select y 2)) x)
			(= (store y 3 (select m 2)) y)
			(= (store m 3 (mod (select x 3) (select y 3))) m)
		)
	)
)

(assert
	(=>
		(or
			(= (select end 1) 1)
			(= (select end 2) 1)
		)
		(and
			(= (store x 3 (select x 2)) x)
			(= (store y 3 (select y 2)) y)
			(= (store m 3 (select m 2)) m)
			(= (store end 3 1) end)
		)
	)
)

; ********************
; Third transition
; ********************

(assert
	(=>
		(and
			(= (select end 1) 0)
			(= (select end 2) 0)
			(= (select m 3) 0)
		)
		(and
			(= res (select y 3))
			(= (store end 3 1) end)
		)
	)
)

(assert
	(=>
		(or
			(= (select end 1) 1)
			(= (select end 2) 1)
			(= (select end 3) 1)
		)
		(and
			(= (store x 4 (select x 3)) x)
			(= (store y 4 (select y 3)) y)
			(= (store m 4 (select m 3)) m)
			(= (store end 4 1) end)
		)
	)
)

(assert
	(=>
		(and
			(= (select end 1) 0)
			(= (select end 2) 0)
			(not (= (select m 3) 0))
		)
		(and
			(= (store end 3 0) end)
			(= (store x 4 (select y 3)) x)
			(= (store y 4 (select m 3)) y)
			(= (store m 4 (mod (select x 4) (select y 4))) m)
		)
	)
)


; ********************
; Fourth transition
; ********************

(assert
	(=>
		(and
			(= (select end 1) 0)
			(= (select end 2) 0)
			(= (select end 3) 0)
			(= (select m 4) 0)
		)
		(and
			(= res (select y 4))
			(= (store end 4 1) end)
		)
	)
)

(assert
	(=>
		(or
			(= (select end 1) 1)
			(= (select end 2) 1)
			(= (select end 3) 1)
			(= (select end 4) 1)
		)
		(and
			(= (store x 5 (select x 4)) x)
			(= (store y 5 (select y 4)) y)
			(= (store m 5 (select m 4)) m)
			(= (store end 5 1) end)
		)
	)
)

(assert
	(=>
		(and
			(= (select end 1) 0)
			(= (select end 2) 0)
			(= (select end 3) 0)
			(not (= (select m 4) 0))
		)
		(and
			(= (store end 4 0) end)
			(= (store x 5 (select y 4)) x)
			(= (store y 5 (select m 4)) y)
			(= (store m 5 (mod (select x 5) (select y 5))) m)
		)
	)
)

; ********************
; Fifth (last) check
; ********************

(assert
	(=>
		(and
			(not (= (select m 5) 0))
			(= (select end 1) 0)
			(= (select end 2) 0)
			(= (select end 3) 0)
			(= (select end 4) 0)
		)
		false
	)
)

(assert
	(=>
		(and
			(= (select end 1) 0)
			(= (select end 2) 0)
			(= (select end 3) 0)
			(= (select end 4) 0)
			(= (select m 5) 0)
		)
		(and
			(= res (select y 5))
			(= (store end 5 1) end)
		)
	)
)

(check-sat)
(get-model)

(exit)