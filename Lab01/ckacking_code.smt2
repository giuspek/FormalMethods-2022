

(declare-const x11 Bool)
(declare-const x12 Bool)
(declare-const x21 Bool)
(declare-const x22 Bool)
(declare-const x31 Bool)
(declare-const x32 Bool)
(declare-const x41 Bool)
(declare-const x42 Bool)

; Clear conditions
(assert (or (and x11 (not x21) (not x22) ) (and x22 (not x11) (not x12))))
(assert (and (not x11) (not x12) (not x41) (not x42)))
(assert (or (and x31 (not x41) (not x42) ) (and x42 (not x31) (not x32))))

; Hidden conditions
(assert (or x11 x21 x31 x41))
(assert (=> x11 (and (not x21) (not x31) (not x41))))
(assert (=> x21 (and (not x11) (not x31) (not x41))))
(assert (=> x31 (and (not x21) (not x11) (not x41))))
(assert (=> x41 (and (not x21) (not x31) (not x11))))

(assert (or x12 x22 x32 x42))
(assert (=> x12 (and (not x22) (not x32) (not x42))))
(assert (=> x22 (and (not x12) (not x32) (not x42))))
(assert (=> x32 (and (not x22) (not x12) (not x42))))
(assert (=> x42 (and (not x22) (not x32) (not x12))))

(assert (or (not x31) (not x22)))
; (assert (not (and x31 x22)))

(check-sat)
(get-model)
(exit)
