;sat
;(model
;  (define-fun m () (Array Int Int) (store (store ((as const (Array Int Int)) 0) 2 4) 1 12))
;  (define-fun x () (Array Int Int) (store (store (store (store (store ((as const (Array Int Int)) 0) 5 12) 4 12) 3 12) 2 16) 1 60))
;  (define-fun y () (Array Int Int) (store (store (store (store (store ((as const (Array Int Int)) 0) 5 4) 4 4) 3 4) 2 12) 1 16))
;  (define-fun res () Int 4)
;)

(set-option :produce-models true)

(declare-const m (Array Int Int))
(declare-const x (Array Int Int))
(declare-const y (Array Int Int))
(declare-const res Int)

(assert (= (store x 1 60) x))
(assert (= (store y 1 16) y))

(assert (= (store m 1 (mod (select x 1) (select y 1))) m))

; ********************
; First transition
; ********************

(assert
	(=>
		(= (select m 1) 0)
		(= res (select y 1))
	)
)

; If stopped, the values of x, y, m remain the same in the next iterations
(assert
	(=>
		(= (select m 1) 0)
		(and
			(= (store x 2 (select x 1)) x)
			(= (store y 2 (select y 1)) y)
			(= (store m 2 (select m 1)) m)
		)
	)
)

(assert
	(=>
		(not (= (select m 1) 0))
		(and
			(= (store x 2 (select y 1)) x)
			(= (store y 2 (select m 1)) y)
			(= (store m 2 (mod (select x 2) (select y 2))) m)
		)
	)
)

; ********************
; Second transition
; ********************

(assert
	(=>
		(and
			(not (= (select m 1) 0))
			(= (select m 2) 0)
		)
		(= res (select y 2))
	)
)

(assert
	(=>
		(or
			(= (select m 1) 0)
			(= (select m 2) 0)
		)
		(and
			(= (store x 3 (select x 2)) x)
			(= (store y 3 (select y 2)) y)
			(= (store m 3 (select m 2)) m)
		)
	)
)

(assert
	(=>
		(and
			(not (= (select m 1) 0))
			(not (= (select m 2) 0))
		)
		(and
			(= (store x 3 (select y 2)) x)
			(= (store y 3 (select m 2)) y)
			(= (store m 3 (mod (select x 3) (select y 3))) m)
		)
	)
)

; ********************
; Third transition
; ********************

(assert
	(=>
		(and
			(not (= (select m 1) 0))
			(not (= (select m 2) 0))
			(= (select m 3) 0)
		)
		(= res (select y 3))
	)
)

(assert
	(=>
		(or
			(= (select m 1) 0)
			(= (select m 2) 0)
			(= (select m 3) 0)
		)
		(and
			(= (store x 4 (select x 3)) x)
			(= (store y 4 (select y 3)) y)
			(= (store m 4 (select m 3)) m)
		)
	)
)

(assert
	(=>
		(and
			(not (= (select m 1) 0))
			(not (= (select m 2) 0))
			(not (= (select m 3) 0))
		)
		(and
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
			(not (= (select m 1) 0))
			(not (= (select m 2) 0))
			(not (= (select m 3) 0))
			(= (select m 4) 0)
		)
		(= res (select y 4))
	)
)

(assert
	(=>
		(or
			(= (select m 1) 0)
			(= (select m 2) 0)
			(= (select m 3) 0)
			(= (select m 4) 0)
		)
		(and
			(= (store x 5 (select x 4)) x)
			(= (store y 5 (select y 4)) y)
			(= (store m 5 (select m 4)) m)
		)
	)
)

(assert
	(=>
		(and
			(not (= (select m 1) 0))
			(not (= (select m 2) 0))
			(not (= (select m 3) 0))
			(not (= (select m 4) 0))
		)
		(and
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
			(not (= (select m 1) 0))
			(not (= (select m 2) 0))
			(not (= (select m 3) 0))
			(not (= (select m 4) 0))
			(= (select m 5) 0)
		)
		(= res (select y 5))
	)
)

(assert
	(=>
		(and
			(not (= (select m 1) 0))
			(not (= (select m 2) 0))
			(not (= (select m 3) 0))
			(not (= (select m 4) 0))
			(not (= (select m 5) 0))
		)
		;No more iterations left
		false
	)
)

(check-sat)
(get-model)

(exit)