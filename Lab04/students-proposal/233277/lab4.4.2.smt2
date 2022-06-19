(set-option :produce-models true)

(declare-const a Bool)
(declare-const b Bool)
(declare-const c Bool)

(declare-const ara Bool)
(declare-const bra Bool)
(declare-const cra Bool)

(declare-const arb Bool)
(declare-const brb Bool)
(declare-const crb Bool)

(declare-const arc Bool)
(declare-const brc Bool)
(declare-const crc Bool)

(declare-const aha Bool)
(declare-const bha Bool)
(declare-const cha Bool)

(declare-const ahb Bool)
(declare-const bhb Bool)
(declare-const chb Bool)

(declare-const ahc Bool)
(declare-const bhc Bool)
(declare-const chc Bool)

; One of them killed Agatha
(assert (or a b c))

; A killer always hates his victim and is never richer than his victim
(assert (=> a (and aha (not ara))))
(assert (=> b (and bha (not bra))))
(assert (=> c (and cha (not cra))))

; Charles hates no one that Aunt Agatha hates
(assert (=> aha (not cha)))
(assert (=> ahb (not chb)))
(assert (=> ahc (not chc)))

; Agatha hates everyone except the butler
(assert (and aha ahc (not ahb)))

; The butler hates everyone not richer than Aunt Agatha
(assert (=> (not ara) bha))
(assert (=> (not bra) bhb))
(assert (=> (not cra) bhc))

; The butler hates everyone Aunt Agatha hates
(assert (=> aha bha))
(assert (=> ahb bhb))
(assert (=> ahc bhc))

; No one hates everyone
(assert (not (and aha ahb ahc)))
(assert (not (and bha bhb bhc)))
(assert (not (and cha chb chc)))

; No one richer than him/herself
(assert (not ara))
(assert (not brb))
(assert (not crc))

; x richer than y than y not richer than x 
(assert (=> ara (not ara)))
(assert (=> arb (not bra)))
(assert (=> arc (not cra)))

(assert (=> bra (not arb)))
(assert (=> brb (not brb)))
(assert (=> brc (not crb)))

(assert (=> cra (not arc)))
(assert (=> crb (not brc)))
(assert (=> crc (not crc)))

(check-sat)
(get-model)
(exit)