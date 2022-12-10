; CS152 Fall 2022 
; Hoc Can Huynh
; 014836757
; Homework assignment 5 
; Exercise 2


(define countOccurrences
    (lambda (target list_number)
        (if(null? list_number)
                  0
                  (if(equal? target (car list_number))
                        (+ (countOccurrences target (cdr list_number)) 1 )
                        (countOccurrences target (cdr list_number))))))
                    
(display (countOccurrences 2 '(1 2 1 4 2 6 7 2 1 2))) 
(newline)
(display (countOccurrences 1 '(1 2 1 4 2 6 7 2 1 2))) 
(newline)
(display (countOccurrences 10 '(1 2 1 4 2 6 7 2 1 2))) 
(newline)