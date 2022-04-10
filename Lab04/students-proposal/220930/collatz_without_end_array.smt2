(set-option :produce-models true)

(declare-const x (Array Real Real))

(assert (= (store x 1 16) x))

; Iteration 1

(assert
    (ite
        (= (select x 1) 1)
        (= (store x 2 1) x)
        (ite
            (= (mod (select x 1) 2) 1)
            (= (store x 2 (+ (* (select x 1) 3) 1)) x) ; x odd
            (= (store x 2 (/ (select x 1) 2)) x) ; x even
        )
    )
)

; Iteration 2

(assert
    (ite
        (= (select x 2) 1)
        (= (store x 3 1) x)
        (ite
            (= (mod (select x 2) 2) 1)
            (= (store x 3 (+ (* (select x 2) 3) 1)) x) ; x odd
            (= (store x 3 (/ (select x 2) 2)) x) ; x even
        )
    )
)

; Iteration 3

(assert
    (ite
        (= (select x 3) 1)
        (= (store x 4 1) x)
        (ite
            (= (mod (select x 3) 2) 1)
            (= (store x 4 (+ (* (select x 3) 3) 1)) x) ; x odd
            (= (store x 4 (/ (select x 3) 2)) x) ; x even
        )
    )
)

; Iteration 4

(assert
    (ite
        (= (select x 4) 1)
        (= (store x 5 1) x)
        (ite
            (= (mod (select x 4) 2) 1)
            (= (store x 5 (+ (* (select x 4) 3) 1)) x) ; x odd
            (= (store x 5 (/ (select x 4) 2)) x) ; x even
        )
    )
)

; Iteration 5

(assert (= (select x 5) 1))

(check-sat)
(get-value ((select x 1) (select x 2) (select x 3) (select x 4) (select x 5)))

(exit)