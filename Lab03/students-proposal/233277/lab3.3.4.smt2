(set-option :produce-models true)

(declare-const AB Bool)
(declare-const BC Bool)
(declare-const CD Bool)
(declare-const DA Bool)

(assert (or AB DA))
(assert (or AB BC))
(assert (or BC CD))
(assert (or CD DA))

(assert (or AB CD))
(assert (or BC DA))

(check-allsat (AB BC CD DA))
(exit)