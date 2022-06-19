(set-option :produce-models true)

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

; All 4 pin must be connected
(assert (or x11 x12 x13 x14))
(assert (or x21 x22 x23 x24))
(assert (or x31 x32 x33 x34))
(assert (or x41 x42 x43 x44))

; Each bin connect once
(assert (=> x11 (not (or x12 x13 x14))))
(assert (=> x12 (not (or x11 x13 x14))))
(assert (=> x13 (not (or x12 x11 x14))))
(assert (=> x14 (not (or x12 x13 x11)))) 

(assert (=> x21 (not (or x22 x23 x24))))
(assert (=> x22 (not (or x21 x23 x24))))
(assert (=> x23 (not (or x22 x21 x24))))
(assert (=> x24 (not (or x22 x23 x21)))) 

(assert (=> x31 (not (or x32 x33 x34))))
(assert (=> x32 (not (or x31 x33 x34))))
(assert (=> x33 (not (or x32 x31 x34))))
(assert (=> x34 (not (or x32 x33 x31)))) 

(assert (=> x41 (not (or x42 x43 x44))))
(assert (=> x42 (not (or x41 x43 x44))))
(assert (=> x43 (not (or x42 x41 x44))))
(assert (=> x44 (not (or x42 x43 x41))))

; No 2 pin at the same time
(assert (=> x11 (not (or x21 x31 x41))))
(assert (=> x12 (not (or x22 x32 x42))))
(assert (=> x13 (not (or x23 x33 x43))))
(assert (=> x14 (not (or x24 x34 x44))))

(assert (=> x21 (not (or x11 x31 x41))))
(assert (=> x22 (not (or x12 x32 x42))))
(assert (=> x23 (not (or x13 x33 x43))))
(assert (=> x24 (not (or x14 x34 x44))))

(assert (=> x31 (not (or x21 x11 x41))))
(assert (=> x32 (not (or x22 x12 x42))))
(assert (=> x33 (not (or x23 x13 x43))))
(assert (=> x34 (not (or x24 x14 x44))))

(assert (=> x41 (not (or x21 x31 x11))))
(assert (=> x42 (not (or x22 x32 x12))))
(assert (=> x43 (not (or x23 x33 x13))))
(assert (=> x44 (not (or x24 x34 x14))))

; No diagonal
(assert (not (and x11 x42)))
(assert (not (and x12 x43)))
(assert (not (and x13 x44)))
(assert (not (and x12 x41)))
(assert (not (and x13 x42)))
(assert (not (and x14 x43)))

(assert (not (and x21 x32)))
(assert (not (and x22 x33)))
(assert (not (and x23 x34)))
(assert (not (and x22 x31)))
(assert (not (and x23 x32)))
(assert (not (and x24 x33)))

(check-allsat (x11 x12 x13 x14 x21 x22 x23 x24 x31 x32 x33 x34 x41 x42 x43 x44))