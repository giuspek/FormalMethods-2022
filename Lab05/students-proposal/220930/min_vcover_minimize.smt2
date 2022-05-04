; sat
; 
; (objectives
;  (vcover 3)
; )
; (model
;   (define-fun a () Bool false)
;   (define-fun b () Bool true)
;   (define-fun c () Bool false)
;   (define-fun d () Bool true)
;   (define-fun e () Bool true)
;   (define-fun f () Bool false)
;   (define-fun g () Bool false)
;   (define-fun vcover () Real (to_real 3))
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

; if "(not a)" is false, i.e. "a" is true, i.e. node "a" is selected to be part of the vertex cover...
(assert-soft (not a) :weight 1 :id vcover)
(assert-soft (not b) :weight 1 :id vcover)
(assert-soft (not c) :weight 1 :id vcover)
(assert-soft (not d) :weight 1 :id vcover)
(assert-soft (not e) :weight 1 :id vcover)
(assert-soft (not f) :weight 1 :id vcover)
(assert-soft (not g) :weight 1 :id vcover)

; minimize the nodes that are part of the vertex cover
(minimize vcover)

(check-sat)
(get-objectives)
(get-model)
(exit)