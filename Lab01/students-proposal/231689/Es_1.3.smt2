(declare-const Ai Bool) ;A innocent
(declare-const Ag Bool) ;A guilty
(declare-const Bi Bool) ;B innocent
(declare-const Bg Bool) ;B guilty
(declare-const Ci Bool) ;C innocent
(declare-const Cg Bool) ;C guilty

(assert (and Bg Ci))
(assert (=> Ag Cg)) ;assert (or (not Ag) Cg)
(assert (and Ci (or (and Ag Bg) (and Ag Bi) (and Ai Bg))))
(assert (or (and Ag (not Ai)) (and (not Ag) Ai)))
(assert (or (and Bg (not Bi)) (and (not Bg) Bi)))
(assert (or (and Cg (not Ci)) (and (not Cg) Ci)))

(check-sat)
(exit)