(set-option :produce-models true)
(set-option :opt.priority box)

; Boolean variables represents whether a band can perform or not
(declare-const tb_perform Bool)
(declare-const ad_perform Bool)
(declare-const rs_perform Bool)
(declare-const kw_perform Bool)

; Boolean variables represents if a band can perform in that timeslot
(declare-fun tb18 () Bool)
(declare-fun tb19 () Bool)
(declare-fun tb20 () Bool)
(declare-fun tb21 () Bool)
(declare-fun tb22 () Bool)
(declare-fun tb23 () Bool)
(declare-fun ad18 () Bool)
(declare-fun ad19 () Bool)
(declare-fun ad20 () Bool)
(declare-fun ad21 () Bool)
(declare-fun ad22 () Bool)
(declare-fun ad23 () Bool)
(declare-fun rs18 () Bool)
(declare-fun rs19 () Bool)
(declare-fun rs20 () Bool)
(declare-fun rs21 () Bool)
(declare-fun rs22 () Bool)
(declare-fun rs23 () Bool)
(declare-fun kw18 () Bool)
(declare-fun kw19 () Bool)
(declare-fun kw20 () Bool)
(declare-fun kw21 () Bool)
(declare-fun kw22 () Bool)
(declare-fun kw23 () Bool)

; if enable these 4 assertions above: UNSAT
; (assert (and tb_perform (or (and tb19 tb20) (and tb22 tb23))))
; (assert (and ad_perform (or (and ad18 ad19 ad20) (and ad19 ad20 ad21) (and ad20 ad21 ad22) (and ad21 ad22 ad23))))
; (assert (and rs_perform (or rs18 rs23)))
; (assert (and kw_perform (or (= kw19 true) (= kw20 true) (= kw21 true) (= kw22 true))))

; The Beagles: from 19.00 to 21.00 or from 22.00 to 24.00
(assert (=> tb_perform (or (and tb19 tb20) (and tb22 tb23))))

; AC/DC++: 3 consecutive hours, no matter when
(assert (=> ad_perform (or (and ad18 ad19 ad20) (and ad19 ad20 ad21) (and ad20 ad21 ad22) (and ad21 ad22 ad23))))

; Rolling Stonks: from 18.00 to 19.00 or from 23.00 to 24.00
(assert (=> rs_perform (or rs18 rs23)))

; Kanji West: 1 hour among all the slots, excluding the first slot and the last one.
(assert (=> kw_perform (or (= kw19 true) (= kw20 true) (= kw21 true) (= kw22 true))))

; Each timeslot can be reserved for 1 band only
(assert (=> tb18 (not (or ad18 rs18 kw18))))
(assert (=> tb19 (not (or ad19 rs19 kw19))))
(assert (=> tb20 (not (or ad20 rs20 kw20))))
(assert (=> tb21 (not (or ad21 rs21 kw21))))
(assert (=> tb22 (not (or ad22 rs22 kw22))))
(assert (=> tb23 (not (or ad23 rs23 kw23))))

(assert (=> ad18 (not (or tb18 rs18 kw18))))
(assert (=> ad19 (not (or tb19 rs19 kw19))))
(assert (=> ad20 (not (or tb20 rs20 kw20))))
(assert (=> ad21 (not (or tb21 rs21 kw21))))
(assert (=> ad22 (not (or tb22 rs22 kw22))))
(assert (=> ad23 (not (or tb23 rs23 kw23))))

(assert (=> rs18 (not (or ad18 tb18 kw18))))
(assert (=> rs19 (not (or ad19 tb19 kw19))))
(assert (=> rs20 (not (or ad20 tb20 kw20))))
(assert (=> rs21 (not (or ad21 tb21 kw21))))
(assert (=> rs22 (not (or ad22 tb22 kw22))))
(assert (=> rs23 (not (or ad23 tb23 kw23))))

(assert (=> kw18 (not (or ad18 rs18 tb18))))
(assert (=> kw19 (not (or ad19 rs19 tb19))))
(assert (=> kw20 (not (or ad20 rs20 tb20))))
(assert (=> kw21 (not (or ad21 rs21 tb21))))
(assert (=> kw22 (not (or ad22 rs22 tb22))))
(assert (=> kw23 (not (or ad23 rs23 tb23))))

; AC/DC++ must perform
(assert (= ad_perform true))

; Maximize number of bands can perform live
(assert-soft (not tb_perform) :weight 1 :id num_bands)
(assert-soft (not ad_perform) :weight 1 :id num_bands)
(assert-soft (not rs_perform) :weight 1 :id num_bands)
(assert-soft (not kw_perform) :weight 1 :id num_bands)

(maximize num_bands)

; Maximum number of bands can perform live is 3: AC/DC ++: 18-21h, Kanji West: 22-23h, Rolling Stonks: 23-24h

(check-sat)
(get-objectives)
(get-model)
(exit)
