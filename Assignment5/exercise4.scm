; CS152 Fall 2022 
; Hoc Can Huynh
; 014836757
; Homework assignment 5 
; Exercise 4

(define getNthElement 
    (lambda (list_number idx)
        (if(or (null? list_number)  (= idx 0))  
           #f
           (if (<= idx 1) (car list_number)
               (getNthElement (cdr list_number) (- idx 1))
            )
   )
  )
)


(display (getNthElement '(0 1 2 3 4 5 6 7 8 9 10) 40))
(newline)
(display (getNthElement '(0 1 2 3 4 5 6 7 8 9 10) 0))
(newline)
(display (getNthElement '(0 1 2 3 4 5 6 7 8 9 10) 4))
(newline)