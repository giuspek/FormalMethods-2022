(set-option :produce-models true)
(set-option :produce-unsat-cores true)

(declare-const d Int)

(declare-sort my_sort 0)
(declare-fun f (Int) my_sort)


(declare-const V (Array Int Int))
(declare-const x Int)
(declare-const i Int)

; (d ≥ 0)
(assert (!
    (>= d 0)
:named A))

; (d < 1)
(assert (!
    (< d 1)
:named B))

; ((f(d) = f(0)) → (read(write(V, i, x), i + d) = x + 1))
(assert (!
    (=>
        (= (f d) (f 0))
        (= (select (store V i x) (+ i d)) (+ x 1))
    )
:named C))


(check-sat)
(get-unsat-core)

(exit)