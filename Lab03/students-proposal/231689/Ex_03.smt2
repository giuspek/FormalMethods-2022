; password requires all 4 pins
; no diagonal line 
; how many combination we need to try to unlock the phone?
; (check-allsat(var1 var2)) var1 and var2 can only be boolean variables

(declare-const x11 Bool)
(declare-const x12 Bool)
(declare-const x13 Bool)
(declare-const x14 Bool)

(declare-const x21 Bool)
(declare-const x22 Bool)
(declare-const x23 Bool)
(declare-const x24 Bool)

(declare-const x31 Bool)
(declare-const x32 Bool)
(declare-const x33 Bool)
(declare-const x34 Bool)

(declare-const x41 Bool)
(declare-const x42 Bool)
(declare-const x43 Bool)
(declare-const x44 Bool)

(assert (=> x11 (or x22 x32)))
(assert (=> x12 (or x23 x33)))
(assert (=> x13 (or x24 x34)))

(assert (=> x21 (or x12 x42)))
(assert (=> x22 (or x13 x43)))
(assert (=> x23 (or x14 x44)))

(assert (=> x31 (or x12 x42)))
(assert (=> x32 (or x13 x43)))
(assert (=> x33 (or x14 x44)))

(assert (=> x41 (or x22 x32)))
(assert (=> x42 (or x23 x33)))
(assert (=> x43 (or x24 x34)))

(assert (=> x11 (not (or x12 x13 x14))))
(assert (=> x21 (not (or x22 x23 x24))))
(assert (=> x31 (not (or x32 x33 x34))))
(assert (=> x41 (not (or x42 x43 x44))))

(assert (=> x12 (not (or x11 x13 x14))))
(assert (=> x22 (not (or x21 x23 x24))))
(assert (=> x32 (not (or x31 x33 x34))))
(assert (=> x42 (not (or x41 x43 x44))))

(assert (=> x13 (not (or x12 x11 x14))))
(assert (=> x23 (not (or x22 x21 x24))))
(assert (=> x33 (not (or x32 x31 x34))))
(assert (=> x43 (not (or x42 x41 x44))))

(assert (=> x14 (not (or x12 x13 x11))))
(assert (=> x24 (not (or x22 x23 x21))))
(assert (=> x34 (not (or x32 x33 x31))))
(assert (=> x44 (not (or x42 x43 x41))))

; redundant
; (assert (=> x21 (not x32)))
; (assert (=> x22 (not x33)))
; (assert (=> x23 (not x34)))

; (assert (=> x31 (not x22)))
; (assert (=> x32 (not x23)))
; (assert (=> x33 (not x24)))

; (assert (=> x11 (not x42)))
; (assert (=> x12 (not x43)))
; (assert (=> x13 (not x44)))

; (assert (=> x41 (not x12)))
; (assert (=> x42 (not x13)))
; (assert (=> x43 (not x14)))

;at least one
(assert (or x11 x12 x13 x14))
(assert (or x21 x22 x23 x24))
(assert (or x31 x32 x33 x34))
(assert (or x41 x42 x43 x44))

;at most one
(assert (=> x11 (not (or x21 x31 x41))))
(assert (=> x21 (not (or x11 x31 x41))))
(assert (=> x31 (not (or x21 x11 x41))))
(assert (=> x41 (not (or x21 x31 x11))))

(assert (=> x12 (not (or x22 x32 x42))))
(assert (=> x22 (not (or x12 x32 x42))))
(assert (=> x32 (not (or x22 x12 x42))))
(assert (=> x42 (not (or x22 x32 x12))))

(assert (=> x13 (not (or x23 x33 x43))))
(assert (=> x23 (not (or x13 x33 x43))))
(assert (=> x33 (not (or x23 x13 x43))))
(assert (=> x43 (not (or x23 x33 x13))))

(assert (=> x14 (not (or x24 x34 x44))))
(assert (=> x24 (not (or x14 x34 x44))))
(assert (=> x34 (not (or x24 x14 x44))))
(assert (=> x44 (not (or x24 x34 x14))))

(check-allsat (x11 x21 x31 x41 x12 x22 x32 x42 x13 x23 x33 x43 x14 x24 x34 x44))

(exit)