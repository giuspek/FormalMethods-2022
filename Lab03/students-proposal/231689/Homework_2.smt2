(set-option :produce-models true)


(declare-const o Int)
(declare-const b Int)
(declare-const g Int)
(declare-const r Int)
(declare-const v Int)

(declare-const s1 Bool)
(declare-const s2 Bool)
(declare-const s3 Bool)
(declare-const s4 Bool)

(assert (= (+ o (* 2 b) g) (+ r v v)))
(assert (= (+ (* 2 b) r) (+ g o (* 2 b))))
(assert (= s1 (= (+ v v v) (+ o (* 2 b) o))))
(assert (= s2 (= (+ v v v) (+ (* 2 b) o))))
(assert (= s3 (= (+ v v v) (* 3 b))))
(assert (= s4 (= (+ v v v) (+ r o))))

(check-sat)

(get-model)

(exit)