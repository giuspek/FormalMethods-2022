(declare-const a (_ BitVec 32))
(declare-const b (_ BitVec 32))
(declare-const c (_ BitVec 32)) 

(assert (= (bvurem a (_ bv5 32)) (_ bv0 32)))
(assert (= (bvor a b) (_ bv2022 32)))
(assert (bvugt (bvsub a b) ((_ to_bv 32) 1000)))
(assert (= c (bvudiv (bvadd a b) (_ bv2 32))))
(assert (bvult c #x76543210))

(check-sat) 
(exit)