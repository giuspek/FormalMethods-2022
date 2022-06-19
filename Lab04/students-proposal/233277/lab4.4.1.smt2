(set-option :produce-models true)

(declare-const a (_ BitVec 32))
(declare-const b (_ BitVec 32))
(declare-const c (_ BitVec 32))
(declare-const password (_ BitVec 96))

; assert(isMultiple(a,5))
(assert (= (bvurem a (_ bv5 32)) (_ bv0 32)))

; assert(or(a,b) == 2022))
(assert (= (bvor a b) (_ bv2022 32)))

; assert(a - b > 1000)
(assert (bvugt (bvsub a b) (_ bv1000 32)))

; assert(isAverage(c, [a,b]))
(assert (= (bvmul c (_ bv2 32)) (bvadd a b)))

; assert(c<0x76543210)
(assert (bvult c 0x76543210))

; get password + login
(assert (= password (concat (concat a b) c)))

(check-sat)
(get-model)
(exit)