(set-option :produce-models true)

(declare-fun x () (Array Int Int))
(declare-fun end () (Array Int Int))

(assert (= (store x 1 6) x))

; ********************
; First transition
; ********************


(assert
	(=>
		(and
			(= (select x 1) 1)
			true
		)
		(and
			(= (store end 1 1) end)
            true
		)
	)
)

(assert
	(=>
		(and
			(= (mod (select x 1) 2) 1)
			(not (= (select x 1) 1))
		)
		(and
			(= (store end 1 0) end)
			(= (store x 2 (+ 1 (* 3 (select x 1)))) x)
		)
	)
)

(assert
	(=>
		(and
			(= (mod (select x 1) 2) 0)
			(not (= (select x 1) 1))
		)
		(and
			(= (store end 1 0) end)
			(= (store x 2 (div (select x 1) 2)) x)
		)
	)
)

; If stopped, the values of x, y, m remain the same in the next iterations
(assert
	(=>
		(= (select end 1) 1)
		(and
			(= (store x 2 (select x 1)) x)
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
			(= (select x 2) 1)

		)
		(and
			(= (store end 2 1) end)
            true
		)
	)
)

(assert
	(=>
		(and
			(= (select end 1) 0)
			(= (mod (select x 2) 2) 1)
			(not (= (select x 2) 1))
		)
		(and
			(= (store end 2 0) end)
			(= (store x 3 (+ 1 (* 3 (select x 2)))) x)
		)
	)
)

(assert
	(=>
		(and
			(= (select end 1) 0)
			(= (mod (select x 2) 2) 0)
			(not (= (select x 2) 1))
		)
		(and
			(= (store end 2 0) end)
			(= (store x 3 (div (select x 2) 2)) x)
		)
	)
)

; If stopped, the values of x, y, m remain the same in the next iterations
(assert
	(=>
		(or
			(= (select end 1) 1)
			(= (select end 2) 1)
		)
		(and
			(= (store x 3 (select x 2)) x)
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
			(= (select x 3) 1)

		)
		(and
			(= (store end 3 1) end)
            true
		)
	)
)

(assert
	(=>
		(and
			(= (select end 1) 0)
			(= (select end 2) 0)
			(= (mod (select x 3) 2) 1)
			(not (= (select x 3) 1))
		)
		(and
			(= (store end 3 0) end)
			(= (store x 4 (+ 1 (* 3 (select x 3)))) x)
		)
	)
)

(assert
	(=>
		(and
			(= (select end 1) 0)
			(= (select end 2) 0)
			(= (mod (select x 3) 2) 0)
			(not (= (select x 3) 1))
		)
		(and
			(= (store end 3 0) end)
			(= (store x 4 (div (select x 3) 2)) x)
		)
	)
)

; If stopped, the values of x, y, m remain the same in the next iterations
(assert
	(=>
		(or
			(= (select end 1) 1)
			(= (select end 2) 1)
			(= (select end 3) 1)
		)
		(and
			(= (store x 4 (select x 3)) x)
			(= (store end 4 1) end)
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
			(= (select x 4) 1)

		)
		(and
			(= (store end 4 1) end)
            true
		)
	)
)

(assert
	(=>
		(and
			(= (select end 1) 0)
			(= (select end 2) 0)
			(= (select end 3) 0)
			(= (mod (select x 4) 2) 1)
			(not (= (select x 4) 1))
		)
		(and
			(= (store end 4 0) end)
			(= (store x 5 (+ 1 (* 3 (select x 4)))) x)
		)
	)
)

(assert
	(=>
		(and
			(= (select end 1) 0)
			(= (select end 2) 0)
			(= (select end 3) 0)
			(= (mod (select x 4) 2) 0)
			(not (= (select x 4) 1))
		)
		(and
			(= (store end 4 0) end)
			(= (store x 5 (div (select x 4) 2)) x)
		)
	)
)

; If stopped, the values of x, y, m remain the same in the next iterations
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
			(= (store end 5 1) end)
		)
	)
)

; ********************
; Fifth (last) check
; ********************

(assert
	(=>
		(and
			(not (= (select x 5) 1))
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
			(= (select x 5) 1)
		)
		(and
			(= (store end 5 1) end)
            true
		)
	)
)

(check-sat)
(get-model)

(exit)