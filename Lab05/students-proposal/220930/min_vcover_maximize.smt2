; sat
; 
; (objectives
;  (not_in_vcover 4)
; )
; (model
;   (define-fun a () Bool false)
;   (define-fun b () Bool true)
;   (define-fun c () Bool false)
;   (define-fun d () Bool true)
;   (define-fun e () Bool true)
;   (define-fun f () Bool false)
;   (define-fun g () Bool false)
;   (define-fun not_in_vcover () Real (to_real 4))
; )

(set-option :produce-models true)

(declare-const a Bool)
(declare-const b Bool)
(declare-const c Bool)
(declare-const d Bool)
(declare-const e Bool)
(declare-const f Bool)
(declare-const g Bool)

(assert (or a b))
(assert (or b c))
(assert (or c d))
(assert (or c e))
(assert (or d e))
(assert (or d f))
(assert (or d g))
(assert (or e f))

; if "a" is false, i.e. "(not a)" is true, i.e. node "a" is not part of the vertex cover...
(assert-soft a :weight 1 :id not_in_vcover)
(assert-soft b :weight 1 :id not_in_vcover)
(assert-soft c :weight 1 :id not_in_vcover)
(assert-soft d :weight 1 :id not_in_vcover)
(assert-soft e :weight 1 :id not_in_vcover)
(assert-soft f :weight 1 :id not_in_vcover)
(assert-soft g :weight 1 :id not_in_vcover)

; maximize the nodes that are not part of the vertex cover
(maximize not_in_vcover)

(check-sat)
(get-objectives)
(get-model)
(exit)